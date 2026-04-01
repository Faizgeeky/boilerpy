# Changelog

All notable changes to BoilerPy will be documented in this file.

## [1.0.1] - 2024-04-01

### 🎉 Major Release - Production Ready

#### Added - Flask Support (5 Templates)
- **Flask API** - REST API with Blueprints and CORS
- **Flask Auth** - JWT authentication with Flask-JWT-Extended
- **Flask SQL** - SQLAlchemy 2.0 + PostgreSQL with CRUD operations
- **Flask MongoDB** - PyMongo with advanced querying and bulk operations
- **Flask Full-Stack** - Complete web app with Jinja2 templates, authentication, and modern UI

#### Added - FastAPI Templates (2 New)
- **FastAPI MongoDB** - Motor async driver with complete async CRUD
- **FastAPI CRM** - Complete CRM with users, customers, products, orders, and authentication

#### Enhanced - Security Features
- Input validation with regex patterns for project names
- Directory traversal attack prevention
- Secure file permissions (644 for files, 755 for directories)
- Safe path resolution and validation
- Password hashing with PBKDF2-SHA256
- JWT authentication in auth templates
- CORS configuration in all templates
- Security headers (X-Frame-Options, X-Content-Type-Options)
- CSRF protection in fullstack templates

#### Enhanced - Reliability Features
- Comprehensive logging system with structured logs
- Error handling with automatic rollback on failure
- Project name validation (max length, allowed characters)
- Verbose mode (`--verbose` flag) for debugging
- Better error messages with troubleshooting guidance
- Cleanup of partial projects on generation failure

#### Enhanced - CLI Features
- Updated version display to 1.0.1
- Better error messages and user guidance
- Support for both FastAPI and Flask frameworks
- Interactive template selection with structure preview
- Project name validation before generation
- Exit codes for better script integration

#### Enhanced - Project Generation
- Auto-generated .gitignore files with comprehensive rules
- Template variable replacement in more file types (.sh, .cfg)
- UTF-8 encoding enforcement for all text files
- Skip hidden files and __pycache__ during copy
- Secure file copy operations with validation

#### Enhanced - Documentation
- Comprehensive README with all 10 templates
- Security best practices section
- Production deployment checklist
- CLI usage examples
- Version history
- Template structure diagrams
- Setup instructions for both frameworks

#### Technical Improvements
- Type hints throughout codebase
- Custom exception class (TemplateGeneratorError)
- Logging configuration with levels
- Context managers for safe operations
- Path validation using pathlib
- Regex-based validation patterns

### All Templates Include
- ✅ Production-ready code structure
- ✅ Security best practices
- ✅ Comprehensive README
- ✅ Environment variable configuration
- ✅ Docker Compose for databases
- ✅ Requirements.txt with specific versions
- ✅ .env.example files
- ✅ Proper error handling

### Template Statistics
- **Total Templates**: 10 (5 FastAPI + 5 Flask)
- **Total Files Created**: 200+ template files
- **Frameworks Supported**: FastAPI 0.104+, Flask 3.0+
- **Databases Supported**: PostgreSQL, MongoDB
- **Auth Methods**: JWT, Flask-Login
- **Python Versions**: 3.9, 3.10, 3.11, 3.12

## [0.1.0] - 2024-03-17

### Initial Release
- FastAPI API Only template
- FastAPI Authentication template
- FastAPI SQL template
- Basic CLI with init and list commands
- Template registry system
- Project generation from templates

---

## Upgrade Guide

### From 0.1.0 to 1.0.1

1. **Update the package:**
   ```bash
   pip install --upgrade boilerpy
   # or
   pipx upgrade boilerpy
   ```

2. **New features available:**
   - Use `bpy init flask` for Flask templates
   - Use `bpy --verbose init <framework>` for detailed logs
   - All new projects include .gitignore automatically
   - Better error messages guide you to solutions

3. **Breaking changes:**
   - None! Fully backward compatible

4. **New templates to explore:**
   ```bash
   bpy init fastapi  # Now includes mongo and crm options
   bpy init flask    # All 5 Flask templates available
   ```

## Future Plans

- [ ] Add testing templates (pytest, unittest)
- [ ] Add Docker deployment templates
- [ ] Add CI/CD configurations (GitHub Actions, GitLab CI)
- [ ] Add GraphQL templates
- [ ] Add WebSocket templates
- [ ] Add Celery task queue templates
- [ ] Template customization options
- [ ] Plugin system for custom templates

---

**Full Changelog**: https://github.com/Faizgeeky/boilerpy/compare/v0.1.0...v1.0.1
