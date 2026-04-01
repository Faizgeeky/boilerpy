"""Project generator from templates."""
import os
import shutil
import re
import logging
from pathlib import Path
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TemplateGeneratorError(Exception):
    """Base exception for template generator errors."""
    pass


class TemplateGenerator:
    """Generates projects from templates with security and validation."""

    # Valid project name pattern: alphanumeric, hyphens, underscores
    PROJECT_NAME_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')
    MAX_PROJECT_NAME_LENGTH = 100

    def __init__(self, framework: str, template_key: str, project_name: str):
        """Initialize the generator.

        Args:
            framework: Framework name (fastapi, flask)
            template_key: Template identifier (api, auth, sql, etc.)
            project_name: Name of the project to create

        Raises:
            TemplateGeneratorError: If validation fails
        """
        self.framework = framework
        self.template_key = template_key
        self.project_name = self._validate_project_name(project_name)
        self.project_dir = self._get_safe_project_dir(project_name)

        # Template source directory
        package_dir = Path(__file__).parent
        self.template_dir = package_dir / "template_files" / framework / template_key

        logger.info(f"Initializing generator for {framework}/{template_key}: {project_name}")

    def _validate_project_name(self, name: str) -> str:
        """Validate project name for security.

        Args:
            name: Project name to validate

        Returns:
            Validated project name

        Raises:
            TemplateGeneratorError: If validation fails
        """
        if not name or not name.strip():
            raise TemplateGeneratorError("Project name cannot be empty")

        name = name.strip()

        if len(name) > self.MAX_PROJECT_NAME_LENGTH:
            raise TemplateGeneratorError(
                f"Project name too long (max {self.MAX_PROJECT_NAME_LENGTH} characters)"
            )

        if not self.PROJECT_NAME_PATTERN.match(name):
            raise TemplateGeneratorError(
                "Project name can only contain letters, numbers, hyphens, and underscores"
            )

        # Prevent directory traversal attacks
        if '..' in name or '/' in name or '\\' in name:
            raise TemplateGeneratorError("Invalid characters in project name")

        # Prevent hidden directories or special names
        if name.startswith('.') or name in {'', '.', '..', 'CON', 'PRN', 'AUX', 'NUL'}:
            raise TemplateGeneratorError(f"Invalid project name: {name}")

        return name

    def _get_safe_project_dir(self, name: str) -> Path:
        """Get project directory with safety checks.

        Args:
            name: Project name

        Returns:
            Safe project directory path

        Raises:
            TemplateGeneratorError: If path is unsafe
        """
        try:
            project_dir = (Path.cwd() / name).resolve()

            # Ensure project dir is within current directory
            if not str(project_dir).startswith(str(Path.cwd().resolve())):
                raise TemplateGeneratorError("Project directory must be within current directory")

            return project_dir
        except Exception as e:
            raise TemplateGeneratorError(f"Invalid project path: {e}")

    def generate(self) -> None:
        """Generate the project from the template with rollback on failure.

        Raises:
            TemplateGeneratorError: If generation fails
        """
        created_successfully = False

        try:
            # Check if project directory already exists
            if self.project_dir.exists():
                raise TemplateGeneratorError(
                    f"Directory '{self.project_name}' already exists"
                )

            # Check if template directory exists
            if not self.template_dir.exists():
                raise TemplateGeneratorError(
                    f"Template not found: {self.framework}/{self.template_key}"
                )

            logger.info(f"Creating project directory: {self.project_dir}")

            # Create project directory
            self.project_dir.mkdir(parents=True, mode=0o755)

            # Copy template files
            logger.info("Copying template files...")
            self._copy_template_files()

            # Replace template variables in files
            logger.info("Processing template variables...")
            self._replace_template_variables()

            # Create .gitignore if not exists
            self._create_gitignore()

            created_successfully = True
            logger.info(f"Project created successfully: {self.project_name}")

        except Exception as e:
            logger.error(f"Error during project generation: {e}")

            # Rollback: remove partially created directory
            if self.project_dir.exists() and not created_successfully:
                logger.warning(f"Rolling back: removing {self.project_dir}")
                try:
                    shutil.rmtree(self.project_dir)
                except Exception as cleanup_error:
                    logger.error(f"Failed to cleanup: {cleanup_error}")

            # Re-raise as TemplateGeneratorError
            if isinstance(e, TemplateGeneratorError):
                raise
            else:
                raise TemplateGeneratorError(f"Failed to generate project: {e}") from e

    def _copy_template_files(self) -> None:
        """Copy all files from template directory to project directory with security checks."""
        files_copied = 0

        for item in self.template_dir.rglob('*'):
            if item.is_file():
                # Skip cache files and hidden files
                if item.name.startswith('.') and item.name not in {'.env.example', '.gitignore'}:
                    continue
                if '__pycache__' in item.parts:
                    continue

                try:
                    # Calculate relative path from template directory
                    relative_path = item.relative_to(self.template_dir)

                    # Create destination path
                    dest_path = self.project_dir / relative_path

                    # Security check: ensure dest_path is within project_dir
                    dest_path_resolved = dest_path.resolve()
                    if not str(dest_path_resolved).startswith(str(self.project_dir.resolve())):
                        logger.warning(f"Skipping unsafe path: {relative_path}")
                        continue

                    # Create parent directories if needed
                    dest_path.parent.mkdir(parents=True, exist_ok=True, mode=0o755)

                    # Copy file with appropriate permissions
                    shutil.copy2(item, dest_path)

                    # Set secure permissions (read/write for owner, read for group/others)
                    os.chmod(dest_path, 0o644)

                    files_copied += 1

                except Exception as e:
                    logger.error(f"Failed to copy {item}: {e}")
                    raise TemplateGeneratorError(f"Failed to copy template file: {e}") from e

        logger.info(f"Copied {files_copied} files")

    def _replace_template_variables(self) -> None:
        """Replace template variables in files with security checks."""
        replacements = {
            '{{project_name}}': self.project_name,
            '{{PROJECT_NAME}}': self.project_name.upper(),
            '{{project_name_snake}}': self.project_name.replace('-', '_').replace(' ', '_').lower(),
        }

        # File extensions to process
        text_extensions = {
            '.py', '.txt', '.md', '.env', '.yml', '.yaml',
            '.ini', '.toml', '.json', '.sh', '.cfg'
        }

        files_processed = 0

        for file_path in self.project_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix in text_extensions:
                try:
                    # Security check: ensure file is within project directory
                    if not str(file_path.resolve()).startswith(str(self.project_dir.resolve())):
                        continue

                    # Read with explicit encoding
                    content = file_path.read_text(encoding='utf-8')

                    # Replace all template variables
                    for old, new in replacements.items():
                        content = content.replace(old, new)

                    # Write back with explicit encoding
                    file_path.write_text(content, encoding='utf-8')
                    files_processed += 1

                except UnicodeDecodeError:
                    logger.warning(f"Skipping binary file: {file_path}")
                except Exception as e:
                    logger.error(f"Could not process {file_path}: {e}")
                    raise TemplateGeneratorError(f"Failed to process template: {e}") from e

        logger.info(f"Processed {files_processed} template files")

    def _create_gitignore(self) -> None:
        """Create a comprehensive .gitignore file if it doesn't exist."""
        gitignore_path = self.project_dir / '.gitignore'

        if gitignore_path.exists():
            logger.info(".gitignore already exists, skipping")
            return

        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Environment variables
.env
.env.local
.env.*.local

# Database
*.db
*.sqlite
*.sqlite3

# Logs
*.log
logs/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Docker
.dockerignore

# OS
Thumbs.db
"""

        try:
            gitignore_path.write_text(gitignore_content, encoding='utf-8')
            os.chmod(gitignore_path, 0o644)
            logger.info("Created .gitignore file")
        except Exception as e:
            logger.warning(f"Could not create .gitignore: {e}")
