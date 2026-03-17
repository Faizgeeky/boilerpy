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

- ✅ **5+ Professional Templates** - API-only, Auth, SQL, MongoDB, CRM
- ⚡ **Lightning Fast** - Generate projects in < 5 seconds
- 🎨 **Clean Architecture** - Industry best practices built-in
- 🔧 **Zero Configuration** - Works out of the box
- 🐍 **Python 3.9+** - Modern Python support

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

Select template (1-5): 3
Enter project name: my-awesome-api

🚀 Creating SQL project: my-awesome-api
✅ Project created successfully!
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
*Coming soon!*

## 🎨 Features

- 🏗️ **Production-Ready** - All templates follow industry best practices
- 📁 **Clean Structure** - Organized, scalable architecture
- 🔐 **Security** - JWT authentication, password hashing built-in
- 🗄️ **Database Ready** - SQLAlchemy, PostgreSQL, MongoDB support
- 🐳 **Docker Included** - docker-compose.yml for databases
- 📝 **Type Hints** - Full typing support with Pydantic
- 🧪 **Testing Ready** - Structured for easy testing
- 📖 **Documentation** - Comprehensive README in each project

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

Visit http://localhost:8000/docs for API documentation.

### Project Structure

Every generated project includes:
- ✅ `requirements.txt` - All dependencies
- ✅ `.env.example` - Environment variables template
- ✅ `.gitignore` - Git ignore rules
- ✅ `README.md` - Complete setup guide
- ✅ `docker-compose.yml` - Database setup (SQL/MongoDB templates)

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
