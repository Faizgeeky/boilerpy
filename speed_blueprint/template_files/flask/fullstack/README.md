# {{project_name}} - Flask Fullstack Application

A production-ready Flask fullstack web application with Jinja2 templates, authentication, and modern frontend.

## Features

- **Flask 3.0** - Modern Python web framework
- **Jinja2 Templates** - Dynamic HTML rendering
- **Flask-Login** - User authentication and session management
- **Flask-WTF** - Form handling with CSRF protection
- **WTForms** - Form validation
- **Responsive Design** - Mobile-friendly custom CSS
- **JavaScript Enhancements** - Better user experience
- **Error Handling** - Custom 404 and 500 error pages
- **Security** - Password hashing, CSRF protection, secure sessions
- **Production Ready** - Configured for production with Gunicorn

## Project Structure

```
{{project_name}}/
├── app/
│   ├── __init__.py              # Application factory
│   ├── core/
│   │   └── config.py            # Configuration settings
│   ├── models/
│   │   └── user.py              # User model
│   ├── forms/
│   │   └── auth.py              # Authentication forms
│   ├── routes/
│   │   ├── main.py              # Main routes
│   │   └── auth.py              # Authentication routes
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # Custom CSS
│   │   └── js/
│   │       └── main.js          # JavaScript
│   └── templates/
│       ├── base.html            # Base template
│       ├── index.html           # Home page
│       ├── about.html           # About page
│       ├── dashboard.html       # User dashboard
│       ├── auth/
│       │   ├── login.html       # Login page
│       │   └── register.html    # Registration page
│       └── errors/
│           ├── 404.html         # 404 error page
│           └── 500.html         # 500 error page
├── .env.example                 # Environment variables template
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Quick Start

### Prerequisites

- Python 3.11+
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

5. **Run the application:**
   ```bash
   flask run
   # Or for production:
   gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
   ```

The application will be available at `http://localhost:5000`

## Pages and Routes

### Public Routes

- **Home** (`/`) - Landing page with features
- **About** (`/about`) - About the application
- **Login** (`/auth/login`) - User login
- **Register** (`/auth/register`) - User registration

### Protected Routes (Login Required)

- **Dashboard** (`/dashboard`) - User dashboard

### Authentication Routes

- **Logout** (`/auth/logout`) - Logout user

## Features in Detail

### User Authentication

- **Registration**: Users can create accounts with email, username, and password
- **Login**: Secure login with "Remember Me" option
- **Session Management**: Persistent sessions with Flask-Login
- **Password Security**: Passwords are hashed using PBKDF2-SHA256
- **Protected Routes**: Use `@login_required` decorator for protected pages

### Form Validation

All forms include:
- CSRF token protection
- Server-side validation with WTForms
- Custom validators (email format, username uniqueness, etc.)
- Real-time client-side validation with JavaScript
- Password strength indicator
- Password match confirmation

### User Interface

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Custom CSS**: No dependencies, fully customizable
- **Flash Messages**: User feedback with auto-dismiss
- **Clean Layout**: Modern, professional design
- **Accessibility**: Semantic HTML and ARIA attributes

### Security Features

1. **Password Hashing**: PBKDF2-SHA256 with salt
2. **CSRF Protection**: All forms protected with CSRF tokens
3. **Secure Sessions**: HttpOnly, SameSite cookies
4. **Input Validation**: Server-side and client-side validation
5. **SQL Injection Prevention**: (Add database in production)
6. **XSS Protection**: Jinja2 auto-escaping
7. **Session Timeout**: Configurable session lifetime

## Configuration

Edit `.env` file to configure:

- `DEBUG` - Enable debug mode (True/False)
- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 5000)
- `SECRET_KEY` - Secret key for session management (required)

### Generating a Secret Key

```python
import secrets
print(secrets.token_hex(32))
```

## Customization

### Adding New Pages

1. **Create a template** in `app/templates/`:
   ```html
   {% extends "base.html" %}
   {% block title %}My Page{% endblock %}
   {% block content %}
       <h1>My Content</h1>
   {% endblock %}
   ```

2. **Add a route** in `app/routes/main.py`:
   ```python
   @bp.route('/mypage')
   def mypage():
       return render_template('mypage.html')
   ```

### Adding Database Support

To add database support (PostgreSQL, SQLite, etc.):

1. Install SQLAlchemy:
   ```bash
   pip install Flask-SQLAlchemy
   ```

2. Update `app/models/user.py` to use SQLAlchemy models

3. Add database configuration to `app/core/config.py`

4. Initialize database in `app/__init__.py`

### Customizing Styles

Edit `app/static/css/style.css`:
- Modify CSS variables in `:root` for colors
- Add custom classes for your components
- Responsive breakpoints at 768px

### Adding JavaScript Features

Edit `app/static/js/main.js`:
- Add event listeners
- Create AJAX requests
- Enhance user interactions

## Production Deployment

### Using Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

### Using Docker

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
```

Build and run:
```bash
docker build -t {{project_name}} .
docker run -p 5000:5000 -e SECRET_KEY=your-key {{project_name}}
```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/{{project_name}}/app/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### Environment Variables for Production

```bash
export DEBUG=False
export SECRET_KEY=your-production-secret-key-min-32-characters
export SESSION_COOKIE_SECURE=True
```

## Testing

### Manual Testing

1. **Register a new user:**
   - Go to `/auth/register`
   - Fill in the form
   - Check validation

2. **Login:**
   - Go to `/auth/login`
   - Enter credentials
   - Test "Remember Me"

3. **Access protected route:**
   - Try accessing `/dashboard` without login
   - Login and access `/dashboard`

4. **Test error pages:**
   - Visit non-existent page for 404
   - Trigger error for 500 (if debug is off)

### Adding Unit Tests

Install pytest:
```bash
pip install pytest pytest-flask
```

Create `tests/test_auth.py`:
```python
def test_register(client):
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123'
    })
    assert response.status_code == 302  # Redirect after success
```

## User Storage

By default, users are stored in memory (for demo purposes). For production:

### Option 1: SQLite (Simple)
```python
# Add Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
```

### Option 2: PostgreSQL (Production)
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/dbname'
```

### Option 3: MongoDB (NoSQL)
```python
from flask_pymongo import PyMongo
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydb'
```

## Troubleshooting

**Import errors:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**Templates not found:**
- Check template paths in `app/templates/`
- Ensure Flask can find the app directory

**Static files not loading:**
- Clear browser cache
- Check static file paths
- Ensure `static` folder exists

**CSRF token missing:**
- Ensure `{{ form.hidden_tag() }}` is in form
- Check SECRET_KEY is set

**Session not persisting:**
- Set SECRET_KEY
- Check cookie settings
- Clear browser cookies

## License

MIT License - feel free to use this project for your applications.
