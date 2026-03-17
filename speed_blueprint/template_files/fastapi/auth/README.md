# {{project_name}}

FastAPI project with JWT authentication generated with BoilerPy.

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

3. Copy environment file and update SECRET_KEY:
```bash
cp .env.example .env
# Edit .env and change the SECRET_KEY to a secure random string
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Authentication

This template includes JWT-based authentication:

1. **Register a new user:**
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"password123"}'
```

2. **Login:**
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login?username=testuser&password=password123"
```

3. **Access protected endpoints:**
```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Demo Account

Username: `demo`
Password: `demo123`

## Project Structure

```
app/
├── main.py              # Application entry point
├── api/
│   └── v1/
│       ├── router.py    # API router
│       └── endpoints/   # API endpoints
│           ├── auth.py  # Authentication endpoints
│           └── users.py # User endpoints
├── core/
│   ├── config.py        # Configuration
│   ├── security.py      # JWT & password utilities
│   └── dependencies.py  # FastAPI dependencies
├── models/              # Database models (add your models here)
└── schemas/             # Pydantic schemas
    ├── user.py
    └── token.py
```

## Security Notes

- Change the `SECRET_KEY` in production to a secure random string
- Use a proper database instead of the in-memory fake_users_db
- Implement proper password validation
- Consider adding rate limiting for auth endpoints
- Use HTTPS in production
