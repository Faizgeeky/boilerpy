# Contributing to BoilerPy

Thank you for your interest in contributing to BoilerPy! 🎉

## How to Contribute

### Adding New Templates

1. Create a new directory under `speed_blueprint/template_files/{framework}/{template_name}/`
2. Add your template files with `{{project_name}}` placeholders where needed
3. Update `speed_blueprint/templates.py` with template metadata
4. Test your template by generating a project
5. Submit a pull request

### Template Variables

Use these variables in your templates:
- `{{project_name}}` - Project name (e.g., "my-api")
- `{{PROJECT_NAME}}` - Uppercase version
- `{{project_name_snake}}` - Snake case version (e.g., "my_api")

### Reporting Issues

Found a bug? Please open an issue with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your Python version and OS

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit (`git commit -m 'Add amazing feature'`)
6. Push (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/Faizgeeky/boilerpy.git
cd boilerpy
python -m venv venv
source venv/bin/activate
pip install -e .
```

## Code Style

- Follow PEP 8
- Use type hints where possible
- Keep functions small and focused
- Add docstrings to public functions

## Questions?

Open a [Discussion](https://github.com/Faizgeeky/boilerpy/discussions) and we'll help!
