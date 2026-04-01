# {{project_name}}

Flask REST API project with clean architecture and best practices.

## Features

- ✅ Flask 3.0 with Blueprint architecture
- ✅ CORS configuration
- ✅ RESTful API structure
- ✅ Environment-based configuration
- ✅ Security headers
- ✅ Clean code organization

## Project Structure

```
{{project_name}}/
├── app/
│   ├── __init__.py          # Application factory
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py  # Blueprint registration
│   │       └── endpoints/   # API endpoints
│   ├── core/
│   │   └── config.py        # Configuration
│   └── schemas/             # Data models
├── requirements.txt
├── .env.example
└── README.md
```

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

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

4. Run the application:
```bash
flask run
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/docs` - API documentation
- `GET /api/v1/items` - List all items
- `GET /api/v1/items/<id>` - Get item by ID
- `POST /api/v1/items` - Create new item
- `PUT /api/v1/items/<id>` - Update item
- `DELETE /api/v1/items/<id>` - Delete item

## Development

Run in development mode:
```bash
export FLASK_ENV=development
flask run --reload
```

## Production

Run with Gunicorn:
```bash
gunicorn "app:create_app()" -w 4 -b 0.0.0.0:8000
```

## Testing

```bash
pip install pytest pytest-flask
pytest
```

## License

MIT
