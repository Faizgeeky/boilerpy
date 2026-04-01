# {{project_name}} - Flask with SQLAlchemy & PostgreSQL

A production-ready Flask REST API with SQLAlchemy ORM and PostgreSQL database.

## Features

- **Flask 3.0** - Modern Python web framework
- **SQLAlchemy 2.0** - Powerful ORM with typed mappings
- **PostgreSQL** - Robust relational database
- **CORS Support** - Cross-origin resource sharing
- **Docker Support** - Easy deployment with Docker Compose
- **Input Validation** - Request validation with dataclasses
- **Password Hashing** - Secure password storage with Werkzeug
- **Database Migrations** - Schema management with Alembic
- **Production Ready** - Configured for production with Gunicorn

## Project Structure

```
{{project_name}}/
├── app/
│   ├── __init__.py              # Application factory
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py      # API v1 blueprint
│   │       └── endpoints/
│   │           └── users.py     # User CRUD endpoints
│   ├── core/
│   │   ├── config.py            # Configuration settings
│   │   └── database.py          # Database setup
│   ├── crud/
│   │   └── user.py              # User CRUD operations
│   ├── models/
│   │   └── user.py              # SQLAlchemy models
│   └── schemas/
│       └── user.py              # Request/response schemas
├── .env.example                 # Environment variables template
├── docker-compose.yml           # Docker services configuration
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 16+ (or use Docker)
- pip

### Installation

1. **Clone and navigate to the project:**
   ```bash
   cd {{project_name}}
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Start PostgreSQL (using Docker):**
   ```bash
   docker-compose up -d db
   ```

6. **Run the application:**
   ```bash
   flask run
   # Or for production:
   gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
   ```

The API will be available at `http://localhost:5000`

## Using Docker Compose

Run the entire stack (PostgreSQL + Flask app):

```bash
docker-compose up -d
```

This will:
- Start PostgreSQL on port 5432
- Start the Flask app on port 5000
- Create all necessary database tables

## API Endpoints

### Health Check

```bash
GET /health
```

### Users

**List Users**
```bash
GET /api/v1/users?skip=0&limit=10
```

**Get User**
```bash
GET /api/v1/users/{user_id}
```

**Create User**
```bash
POST /api/v1/users
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123",
  "full_name": "John Doe"
}
```

**Update User**
```bash
PUT /api/v1/users/{user_id}
Content-Type: application/json

{
  "email": "newemail@example.com",
  "full_name": "John Smith"
}
```

**Delete User**
```bash
DELETE /api/v1/users/{user_id}
```

**Authenticate User**
```bash
POST /api/v1/users/authenticate
Content-Type: application/json

{
  "username": "johndoe",
  "password": "securepassword123"
}
```

## Database Migrations

This project includes Alembic for database migrations:

**Initialize Alembic (first time only):**
```bash
alembic init alembic
```

**Generate a migration:**
```bash
alembic revision --autogenerate -m "Add user table"
```

**Apply migrations:**
```bash
alembic upgrade head
```

**Rollback migration:**
```bash
alembic downgrade -1
```

## Configuration

Edit `.env` file to configure:

- `DEBUG` - Enable debug mode (True/False)
- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 5000)
- `SECRET_KEY` - Secret key for session management
- `ALLOWED_ORIGINS` - CORS allowed origins
- `DATABASE_URL` - PostgreSQL connection string

## Security Features

- **Password Hashing** - Passwords are hashed using PBKDF2-SHA256
- **Input Validation** - All inputs are validated using schemas
- **SQL Injection Protection** - SQLAlchemy ORM prevents SQL injection
- **CORS Configuration** - Configurable CORS for API security
- **Environment Variables** - Sensitive data in environment variables

## Database Schema

### Users Table

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | Primary Key |
| email | VARCHAR(255) | Unique, Not Null, Indexed |
| username | VARCHAR(100) | Unique, Not Null, Indexed |
| full_name | VARCHAR(255) | Nullable |
| hashed_password | VARCHAR(255) | Not Null |
| is_active | BOOLEAN | Default: True |
| is_superuser | BOOLEAN | Default: False |
| created_at | TIMESTAMP | Default: NOW() |
| updated_at | TIMESTAMP | Auto-update |

## Production Deployment

### Using Docker

```bash
docker-compose up -d
```

### Manual Deployment

1. **Set production environment variables:**
   ```bash
   export DEBUG=False
   export SECRET_KEY=your-production-secret-key
   export DATABASE_URL=postgresql://user:pass@host:5432/dbname
   ```

2. **Run with Gunicorn:**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
   ```

3. **Use a reverse proxy (Nginx):**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## Testing

Example curl commands:

**Create a user:**
```bash
curl -X POST http://localhost:5000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "testpass123",
    "full_name": "Test User"
  }'
```

**Authenticate:**
```bash
curl -X POST http://localhost:5000/api/v1/users/authenticate \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

## Troubleshooting

**Database connection errors:**
- Ensure PostgreSQL is running: `docker-compose ps`
- Check DATABASE_URL in .env file
- Verify PostgreSQL credentials

**Import errors:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**Port already in use:**
- Change PORT in .env file
- Or kill process using the port: `lsof -ti:5000 | xargs kill`

## License

MIT License - feel free to use this project for your applications.
