# {{project_name}}

Flask API with JWT Authentication and user management.

## Features

- ✅ JWT Authentication (Access & Refresh tokens)
- ✅ User registration and login
- ✅ Password hashing with werkzeug
- ✅ Protected routes
- ✅ CORS configuration
- ✅ Security best practices

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user
- `GET /api/v1/auth/me` - Get current user (protected)

### Users
- `GET /api/v1/users/profile` - Get user profile (protected)

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your settings
```

4. Run the application:
```bash
flask run
```

## Usage Examples

### Register
```bash
curl -X POST http://localhost:5000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "secure123", "full_name": "John Doe"}'
```

### Login
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "secure123"}'
```

### Access Protected Route
```bash
curl -X GET http://localhost:5000/api/v1/auth/me \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## License

MIT
