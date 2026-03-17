# {{project_name}}

FastAPI project with SQLAlchemy, PostgreSQL, and Alembic migrations generated with BoilerPy.

## Setup

### 1. Start PostgreSQL with Docker

```bash
docker-compose up -d
```

This will start a PostgreSQL database on port 5432.

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Copy environment file

```bash
cp .env.example .env
```

### 5. Run database migrations

```bash
# Create initial migration
alembic revision --autogenerate -m "Initial migration"

# Apply migrations
alembic upgrade head
```

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
app/
├── main.py              # Application entry point
├── api/
│   └── v1/
│       ├── router.py    # API router
│       └── endpoints/   # API endpoints
│           ├── items.py # Item CRUD endpoints
│           └── health.py # Health check
├── core/
│   ├── config.py        # Configuration
│   └── database.py      # Database session
├── models/              # SQLAlchemy models
│   ├── base.py
│   └── item.py
├── schemas/             # Pydantic schemas
│   └── item.py
├── crud/                # CRUD operations
│   └── item.py
└── db/                  # Database utilities
    └── init_db.py
alembic/                 # Alembic migrations
```

## API Endpoints

### Items
- `GET /api/v1/items` - List all items
- `GET /api/v1/items/{id}` - Get item by ID
- `POST /api/v1/items` - Create new item
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

### Health
- `GET /api/v1/health` - Health check with database connectivity test

## Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1

# Show current migration
alembic current

# Show migration history
alembic history
```

## Database Management

```bash
# Stop PostgreSQL
docker-compose down

# Stop and remove data
docker-compose down -v

# View logs
docker-compose logs -f postgres
```

## Development

Add new models in `app/models/`, schemas in `app/schemas/`, and CRUD operations in `app/crud/`.
After adding models, create a migration:

```bash
alembic revision --autogenerate -m "Add new model"
alembic upgrade head
```
