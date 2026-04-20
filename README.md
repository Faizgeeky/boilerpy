# 🚀 BoilerPy

<div align="center">

**Lightning-fast FastAPI & Flask project scaffolding CLI**

[![PyPI version](https://badge.fury.io/py/boilerpy.svg)](https://badge.fury.io/py/boilerpy)
[![Python Version](https://img.shields.io/pypi/pyversions/boilerpy.svg)](https://pypi.org/project/boilerpy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/boilerpy)](https://pepy.tech/project/boilerpy)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Installation](#-installation) •
[Quick Start](#-quick-start) •
[Templates](#-templates) •
[Documentation](#-documentation)

</div>

---

## 🎯 Why BoilerPy?

Stop wasting time setting up the same project structure over and over. **BoilerPy** generates production-ready FastAPI and Flask projects in seconds with:

- ✅ **10 Professional Templates** - 5 FastAPI + 5 Flask templates
- 🔒 **Security First** - JWT auth, password hashing, CORS, input validation
- ⚡ **Lightning Fast** - Generate projects in < 5 seconds
- 🎨 **Clean Architecture** - Industry best practices built-in
- 🛡️ **Production Ready** - Error handling, logging, rollback on failure
- 🔧 **Zero Configuration** - Works out of the box
- 🐍 **Python 3.9+** - Modern Python support
- 🐳 **Docker Ready** - Docker Compose for databases

## 📦 Installation

### Using pipx (Recommended)
```bash
pipx install boilerpy
```

### Using pip
```bash
pip install boilerpy
```

### From source
```bash
git clone https://github.com/Faizgeeky/boilerpy.git
cd boilerpy
pip install -e .
```

## 🚀 Quick Start

### 1. List available templates
```bash
bpy list
```

### 2. Create a new project
```bash
bpy init fastapi
```

### 3. Follow the interactive prompts
- Select your template (1-5)
- Enter project name
- Done! Your project is ready 🎉

### Example
```bash
$ bpy init fastapi

============================================================
  Available FASTAPI Templates
============================================================

1. API Only
   Basic FastAPI project with routers and clean architecture

2. Authentication
   FastAPI with JWT authentication, user management

3. SQL (SQLAlchemy + PostgreSQL)
   FastAPI with SQLAlchemy, PostgreSQL, and Alembic migrations

Select template (1-5): 2
Enter project name: my-awesome-api

🚀 Creating Authentication project: my-awesome-api
✅ Project created successfully!

📚 Next steps:
  cd my-awesome-api
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  uvicorn app.main:app --reload

📖 API Docs: http://localhost:8000/docs
```

## 📚 Templates

### 🔷 FastAPI Templates

#### 1. **API Only** - Clean REST API
Perfect for microservices and REST APIs
```
app/
├── main.py              # FastAPI application
├── api/v1/
│   ├── router.py        # API router
│   └── endpoints/       # API endpoints
├── core/
│   └── config.py        # Configuration
└── schemas/             # Pydantic models
```

#### 2. **Authentication** - JWT Auth System
Production-ready authentication with JWT tokens
```
app/
├── main.py
├── api/v1/endpoints/
│   ├── auth.py          # Login, register
│   └── users.py         # User management
├── core/
│   ├── security.py      # JWT utilities
│   └── dependencies.py  # Auth dependencies
└── schemas/
    ├── user.py
    └── token.py
```

#### 3. **SQL** - SQLAlchemy + PostgreSQL
Full database setup with migrations
```
app/
├── models/              # SQLAlchemy models
├── crud/                # CRUD operations
├── core/
│   └── database.py      # Database config
├── alembic/             # Migrations
└── docker-compose.yml   # PostgreSQL setup
```

#### 4. **MongoDB** - Motor Async Driver
MongoDB integration with async support
```
app/
├── core/
│   └── database.py      # MongoDB connection
├── models/              # MongoDB models
└── crud/                # Database operations
```

#### 5. **CRM** - Complete Application
Full CRM with users, customers, products, orders
```
app/
├── models/
│   ├── user.py
│   ├── customer.py
│   ├── product.py
│   └── order.py
├── api/v1/endpoints/
│   ├── auth.py
│   ├── customers.py
│   └── orders.py
└── core/
    ├── database.py
    └── security.py
```

### 🔶 Flask Templates

#### 1. **API Only** - Clean REST API
Blueprint-based Flask API with CORS and clean architecture
```
app/
├── api/v1/
│   ├── endpoints/       # API endpoints
│   │   └── items.py     # CRUD operations
│   └── __init__.py      # Blueprint registration
├── core/
│   └── config.py        # Configuration
└── schemas/             # Data validation
```

#### 2. **Authentication** - JWT Auth System
Flask with JWT authentication and user management
```
app/
├── api/v1/endpoints/
│   ├── auth.py          # Register, login
│   └── users.py         # User management
├── core/
│   ├── security.py      # JWT + password hashing
│   └── config.py        # JWT settings
└── models/              # User models
```

#### 3. **SQL** - SQLAlchemy + PostgreSQL
Flask with SQLAlchemy 2.0 and PostgreSQL
```
app/
├── models/              # SQLAlchemy models
├── crud/                # CRUD operations
├── schemas/             # Validation schemas
├── core/
│   └── database.py      # SQLAlchemy setup
└── docker-compose.yml   # PostgreSQL
```

#### 4. **MongoDB** - PyMongo Integration
Flask with PyMongo and advanced querying
```
app/
├── core/
│   └── database.py      # MongoDB connection
├── models/              # MongoDB models
├── api/v1/endpoints/
│   └── items.py         # CRUD with filtering
└── docker-compose.yml   # MongoDB
```

#### 5. **Full-Stack** - Complete Web App
Flask with Jinja2 templates and authentication
```
app/
├── routes/
│   ├── main.py          # Main routes
│   └── auth.py          # Auth routes
├── templates/           # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   └── auth/            # Login, register
├── static/
│   ├── css/style.css    # Modern responsive CSS
│   └── js/main.js       # Form validation
├── models/              # User models
└── forms/               # WTForms

## 🎨 Features

### Core Features
- 🏗️ **Production-Ready** - All templates follow industry best practices
- 📁 **Clean Structure** - Organized, scalable architecture
- ⚡ **Async Support** - FastAPI with async/await, Motor for MongoDB
- 🐳 **Docker Included** - docker-compose.yml for databases
- 📝 **Type Hints** - Full typing support with Pydantic
- 🧪 **Testing Ready** - Structured for easy testing
- 📖 **Documentation** - Comprehensive README in each project

### Security Features
- 🔐 **JWT Authentication** - Access & refresh tokens
- 🔒 **Password Hashing** - PBKDF2-SHA256 with Werkzeug/Passlib
- 🛡️ **Input Validation** - Server-side validation with detailed errors
- 🌐 **CORS Configuration** - Configurable allowed origins
- 🔑 **CSRF Protection** - Built into fullstack templates
- 🚫 **SQL Injection Prevention** - Parameterized queries/ORM
- 📋 **Security Headers** - X-Frame-Options, X-Content-Type-Options

### Reliability Features
- 📊 **Comprehensive Logging** - Structured logging throughout
- 🔄 **Rollback on Failure** - Automatic cleanup if generation fails
- ✅ **Input Validation** - Project name validation, path security
- 🛡️ **Directory Traversal Protection** - Secure file operations
- ⚠️ **Error Handling** - Comprehensive error messages
- 🔍 **Verbose Mode** - `--verbose` flag for debugging

### Database Support
- 🗄️ **PostgreSQL** - SQLAlchemy with Alembic migrations
- 🍃 **MongoDB** - Motor (async) & PyMongo support
- 🔄 **Database Migrations** - Alembic configured
- 🐳 **Docker Compose** - One-command database setup
- 📊 **Connection Pooling** - Optimized database connections

## 📖 Documentation

### After Creating a Project

```bash
cd my-awesome-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

**FastAPI Projects:**
```bash
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs for interactive API documentation.

**Flask Projects:**
```bash
flask run
```
Visit http://localhost:5000 for your application.

### Project Structure

Every generated project includes:
- ✅ `requirements.txt` - All dependencies
- ✅ `.env.example` - Environment variables template
- ✅ `.gitignore` - Comprehensive Python gitignore (auto-generated)
- ✅ `README.md` - Complete setup guide with examples
- ✅ `docker-compose.yml` - Database setup (SQL/MongoDB templates)
- ✅ Secure file permissions - Proper file modes set automatically

### CLI Options

```bash
# Basic usage
bpy init fastapi              # Interactive template selection
bpy init flask my-project     # Specify project name upfront
bpy list                      # List all available templates

# With verbose logging
bpy --verbose init fastapi    # See detailed generation logs

# Get help
bpy --help                    # Show all commands
bpy init --help               # Show init command help
```

## 🚦 Version History

### v1.0.1 (Latest)
- ✅ Added 5 Flask templates (API, Auth, SQL, MongoDB, Full-Stack)
- ✅ Enhanced security: input validation, directory traversal protection
- ✅ Added logging and error handling with rollback
- ✅ Auto-generated .gitignore files
- ✅ Improved CLI with verbose mode
- ✅ Added MongoDB and CRM templates for FastAPI
- ✅ Enhanced documentation

### v0.1.0
- Initial release with 3 FastAPI templates

## 🔐 Security Best Practices

All templates include security features out of the box:

### Authentication Templates
- Password hashing with PBKDF2-SHA256
- JWT tokens with configurable expiration
- Secure secret key management via environment variables
- Protected routes with authentication middleware

### API Security
- CORS configuration with allowed origins
- Input validation with Pydantic (FastAPI) or WTForms (Flask)
- SQL injection prevention via ORM
- Security headers (X-Frame-Options, X-Content-Type-Options)

### File Security
- Directory traversal attack prevention
- Secure file permissions (644 for files, 755 for directories)
- Validation of project names and paths
- Safe template variable replacement

### Production Checklist
Before deploying to production:
1. ✅ Change `SECRET_KEY` in `.env` (min 32 characters)
2. ✅ Set `DEBUG=False`
3. ✅ Configure production database URLs
4. ✅ Set up HTTPS/SSL certificates
5. ✅ Configure allowed CORS origins
6. ✅ Set up monitoring and logging
7. ✅ Use environment-specific configs

## 🛠️ Development

### Requirements
- Python 3.9+
- pip or pipx

### Contributing
We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Building from Source
```bash
git clone https://github.com/Faizgeeky/boilerpy.git
cd boilerpy
python -m build
```

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🤝 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/Faizgeeky/boilerpy/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Faizgeeky/boilerpy/discussions)
- ⭐ **Star us on GitHub**: [github.com/Faizgeeky/boilerpy](https://github.com/Faizgeeky/boilerpy)

## 🙏 Acknowledgments

Built with ❤️ by [Faiz](https://github.com/Faizgeeky)

Inspired by:
- create-react-app
- vue-cli
- cookiecutter

---

<div align="center">

**[⬆ back to top](#-boilerpy)**

Made with ❤️ for the Python community

</div>

S<h2>🚀 FastAPI Event Booking REST API with Payment Gateway</h2>

<p>👋 Hi, I’m Faiz — Tech Lead Engineer and open-source builder.</p>

<p>In this post, I’ll walk you through how to build a <strong>scalable Event Booking REST API</strong> using <strong>FastAPI</strong>, including <strong>payment gateway integration</strong>, clean architecture, and production-ready practices.</p>

<hr/>

<h3>📦 What you'll learn</h3>
<ul>
  <li>Designing REST APIs with FastAPI</li>
  <li>Event booking & seat management logic</li>
  <li>Payment gateway integration flow</li>
  <li>Database design & optimization</li>
  <li>Production-ready backend structure</li>
</ul>

<hr/>

<h3>💻 Source Code</h3>
<p>
👉 <a href="https://github.com/Faizgeeky" target="_blank">
View full project on GitHub
</a>
</p>

<hr/>

<h3>☕ Support My Work</h3>
<p>
I build free tools and open-source projects for developers:
</p>

<ul>
  <li>🌐 <a href="https://webtoolz365.com/" target="_blank">40+ Free Web Tools</a></li>
  <li>⚙️ FastAPI / Flask Boilerplates</li>
  <li>📦 Open-source libraries</li>
</ul>

<p>
If this guide helps you or saves your time, consider supporting:
</p>

<p>
👉 <a href="https://buymeacoffee.com/geekyfaiz" target="_blank" style="font-weight:bold;">
Buy me a coffee ☕
</a>
</p>

<hr/>

<h3>🚀 Let’s build something awesome!</h3>
<p>
Feel free to connect, contribute, or give feedback.
</p>

👉. Buy me a coffee ☕
