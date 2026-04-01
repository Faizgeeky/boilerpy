"""CLI module for boilerpy."""
import sys
import click
import logging
from speed_blueprint.generator import TemplateGenerator, TemplateGeneratorError
from speed_blueprint.templates import TEMPLATE_REGISTRY

# Configure logging
logging.basicConfig(
    level=logging.WARNING,  # Only show warnings and errors by default
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version="1.0.1", prog_name="bpy")
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
def main(verbose):
    """BoilerPy - Quickly scaffold FastAPI and Flask projects with security and best practices."""
    if verbose:
        logging.getLogger().setLevel(logging.INFO)


@main.command()
@click.argument('framework', type=click.Choice(['fastapi', 'flask'], case_sensitive=False))
@click.argument('project_name', required=False)
def init(framework, project_name):
    """Initialize a new project with the selected framework.

    Example:
        sb init fastapi
        sb init fastapi my-api-project
    """
    framework = framework.lower()

    # Get available templates for the framework
    templates = TEMPLATE_REGISTRY.get(framework, [])

    if not templates:
        click.echo(f"No templates available for {framework}")
        return

    # Display template options with directory structure
    click.echo(f"\n{'='*60}")
    click.echo(f"  Available {framework.upper()} Templates")
    click.echo(f"{'='*60}\n")

    for idx, template in enumerate(templates, 1):
        click.echo(f"{idx}. {template['name']}")
        click.echo(f"   {template['description']}\n")

        # Display directory structure
        for line in template['structure']:
            click.echo(f"   {line}")
        click.echo()

    # Prompt user to select a template
    choice = click.prompt(
        f"Select template (1-{len(templates)})",
        type=click.IntRange(1, len(templates))
    )

    selected_template = templates[choice - 1]

    # Get project name if not provided
    if not project_name:
        project_name = click.prompt(
            "Enter project name",
            default=f"my-{framework}-app"
        )

    # Validate project name early
    if not project_name or not project_name.strip():
        click.echo("❌ Error: Project name cannot be empty", err=True)
        sys.exit(1)

    # Generate the project
    click.echo(f"\n🚀 Creating {selected_template['name']} project: {project_name}")

    try:
        generator = TemplateGenerator(framework, selected_template['key'], project_name)
        generator.generate()

        click.echo(f"\n✅ Project '{project_name}' created successfully!")
        click.echo(f"\n📚 Next steps:")
        click.echo(f"  cd {project_name}")
        click.echo(f"  python -m venv venv")
        click.echo(f"  source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
        click.echo(f"  pip install -r requirements.txt")

        if framework == 'fastapi':
            click.echo(f"  uvicorn app.main:app --reload")
            click.echo(f"\n📖 API Docs: http://localhost:8000/docs")
        else:
            click.echo(f"  flask run")
            click.echo(f"\n📖 App URL: http://localhost:5000")

        click.echo(f"\n💡 Tip: Check README.md for detailed setup instructions")

    except TemplateGeneratorError as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        sys.exit(1)
    except KeyboardInterrupt:
        click.echo("\n\n⚠️  Operation cancelled by user", err=True)
        sys.exit(130)
    except Exception as e:
        logger.exception("Unexpected error occurred")
        click.echo(f"\n❌ Unexpected error: {e}", err=True)
        click.echo("Please report this issue at: https://github.com/Faizgeeky/boilerpy/issues")
        sys.exit(1)


@main.command()
def list():
    """List all available templates."""
    for framework, templates in TEMPLATE_REGISTRY.items():
        click.echo(f"\n{framework.upper()} Templates:")
        click.echo("-" * 40)
        for template in templates:
            click.echo(f"  • {template['name']}: {template['description']}")


if __name__ == '__main__':
    main()
