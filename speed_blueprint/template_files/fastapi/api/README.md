# {{project_name}}

FastAPI project generated with Speed Blueprint.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy environment file:
```bash
cp .env.example .env
```

4. Run the application:
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
├── core/
│   └── config.py        # Configuration
└── schemas/             # Pydantic models
```

## Endpoints

- `GET /` - Root endpoint
- `GET /api/v1/health` - Health check
