"""Project generator from templates."""
import os
import shutil
from pathlib import Path


class TemplateGenerator:
    """Generates projects from templates."""

    def __init__(self, framework, template_key, project_name):
        """Initialize the generator.

        Args:
            framework: Framework name (fastapi, flask)
            template_key: Template identifier (api, auth, sql, etc.)
            project_name: Name of the project to create
        """
        self.framework = framework
        self.template_key = template_key
        self.project_name = project_name
        self.project_dir = Path.cwd() / project_name

        # Template source directory
        package_dir = Path(__file__).parent
        self.template_dir = package_dir / "template_files" / framework / template_key

    def generate(self):
        """Generate the project from the template."""
        # Check if project directory already exists
        if self.project_dir.exists():
            raise FileExistsError(f"Directory '{self.project_name}' already exists")

        # Check if template directory exists
        if not self.template_dir.exists():
            raise FileNotFoundError(
                f"Template not found: {self.framework}/{self.template_key}"
            )

        # Create project directory
        self.project_dir.mkdir(parents=True)

        # Copy template files
        self._copy_template_files()

        # Replace template variables in files
        self._replace_template_variables()

    def _copy_template_files(self):
        """Copy all files from template directory to project directory."""
        for item in self.template_dir.rglob('*'):
            if item.is_file():
                # Calculate relative path from template directory
                relative_path = item.relative_to(self.template_dir)

                # Create destination path
                dest_path = self.project_dir / relative_path

                # Create parent directories if needed
                dest_path.parent.mkdir(parents=True, exist_ok=True)

                # Copy file
                shutil.copy2(item, dest_path)

    def _replace_template_variables(self):
        """Replace template variables in files."""
        replacements = {
            '{{project_name}}': self.project_name,
            '{{PROJECT_NAME}}': self.project_name.upper(),
            '{{project_name_snake}}': self.project_name.replace('-', '_').replace(' ', '_').lower(),
        }

        # File extensions to process
        text_extensions = {'.py', '.txt', '.md', '.env', '.yml', '.yaml', '.ini', '.toml', '.json'}

        for file_path in self.project_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix in text_extensions:
                try:
                    content = file_path.read_text()

                    # Replace all template variables
                    for old, new in replacements.items():
                        content = content.replace(old, new)

                    file_path.write_text(content)
                except Exception as e:
                    print(f"Warning: Could not process {file_path}: {e}")
