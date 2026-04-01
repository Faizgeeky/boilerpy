# {{project_name}} - CRM API

A comprehensive CRM (Customer Relationship Management) API built with FastAPI, featuring user authentication, customer management, product catalog, and order processing.

## Features

### Core Features
- **User Authentication & Authorization**: JWT-based authentication with role-based access control (admin/user)
- **Customer Management**: Complete CRUD operations for managing customer information
- **Product Catalog**: Inventory management with stock tracking
- **Order Management**: Create and manage orders with automatic stock updates
- **Database Migrations**: Alembic for schema version control
- **Security**: Password hashing with bcrypt, JWT tokens, CORS protection

### Technical Features
- **FastAPI**: Modern, fast web framework with automatic API documentation
- **SQLAlchemy 2.0**: Powerful ORM with relationship support
- **Pydantic v2**: Data validation with type hints
- **PostgreSQL**: Robust relational database
- **Docker**: PostgreSQL and pgAdmin included

## Prerequisites

- Python 3.8+
- PostgreSQL (or use Docker Compose)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd {{project_name}}
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Start PostgreSQL:
```bash
docker-compose up -d
```

6. Run database migrations:
```bash
alembic upgrade head
```

7. Start the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Interactive API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Quick Start

### 1. Register a User

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@example.com",
    "password": "securepassword123",
    "full_name": "Admin User",
    "is_admin": true
  }'
```

### 2. Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@example.com&password=securepassword123"
```

Response:
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

### 3. Create a Customer

```bash
curl -X POST "http://localhost:8000/api/v1/customers/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Acme Corporation",
    "email": "contact@acme.com",
    "phone": "+1-555-0123",
    "company": "Acme Corp",
    "address": "123 Main St, City, State 12345"
  }'
```

### 4. Create a Product

```bash
curl -X POST "http://localhost:8000/api/v1/products/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Premium Widget",
    "description": "High-quality widget",
    "sku": "WIDGET-001",
    "price": 99.99,
    "stock": 100
  }'
```

### 5. Create an Order

```bash
curl -X POST "http://localhost:8000/api/v1/orders/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "items": [
      {"product_id": 1, "quantity": 2}
    ],
    "notes": "Urgent delivery"
  }'
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get token

### Users
- `GET /api/v1/users/me` - Get current user
- `GET /api/v1/users/` - List all users (admin only)
- `GET /api/v1/users/{user_id}` - Get user by ID (admin only)
- `PUT /api/v1/users/{user_id}` - Update user (admin only)
- `DELETE /api/v1/users/{user_id}` - Delete user (admin only)

### Customers
- `POST /api/v1/customers/` - Create customer
- `GET /api/v1/customers/` - List customers (with search)
- `GET /api/v1/customers/count` - Count customers
- `GET /api/v1/customers/{customer_id}` - Get customer
- `PUT /api/v1/customers/{customer_id}` - Update customer
- `DELETE /api/v1/customers/{customer_id}` - Delete customer

### Products
- `POST /api/v1/products/` - Create product
- `GET /api/v1/products/` - List products (with filtering)
- `GET /api/v1/products/count` - Count products
- `GET /api/v1/products/{product_id}` - Get product
- `PUT /api/v1/products/{product_id}` - Update product
- `DELETE /api/v1/products/{product_id}` - Delete product

### Orders
- `POST /api/v1/orders/` - Create order
- `GET /api/v1/orders/` - List orders (with filtering by customer, status, date)
- `GET /api/v1/orders/count` - Count orders
- `GET /api/v1/orders/statistics` - Get order statistics (admin only)
- `GET /api/v1/orders/{order_id}` - Get order
- `PUT /api/v1/orders/{order_id}` - Update order
- `DELETE /api/v1/orders/{order_id}` - Delete order

## Database Schema

### Users
- User authentication and authorization
- Fields: email, password, full_name, is_active, is_admin

### Customers
- Customer contact information
- Fields: name, email, phone, company, address, notes

### Products
- Product catalog with inventory
- Fields: name, description, sku, price, stock, is_active

### Orders
- Order tracking with status
- Fields: customer_id, user_id, status, total_amount, notes
- Status: pending, processing, shipped, delivered, cancelled

### Order Items
- Line items for orders
- Fields: order_id, product_id, quantity, unit_price, subtotal

## Database Migrations

### Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations:
```bash
alembic upgrade head
```

### Rollback migration:
```bash
alembic downgrade -1
```

### View migration history:
```bash
alembic history
```

## Project Structure

```
{{project_name}}/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── core/
│   │   ├── config.py          # Configuration settings
│   │   ├── database.py        # Database connection
│   │   ├── security.py        # JWT & password utilities
│   │   └── dependencies.py    # Dependency injection
│   ├── models/
│   │   ├── base.py            # Model registration
│   │   ├── user.py            # User model
│   │   ├── customer.py        # Customer model
│   │   ├── product.py         # Product model
│   │   └── order.py           # Order & OrderItem models
│   ├── schemas/
│   │   ├── token.py           # Token schemas
│   │   ├── user.py            # User schemas
│   │   ├── customer.py        # Customer schemas
│   │   ├── product.py         # Product schemas
│   │   └── order.py           # Order schemas
│   ├── crud/
│   │   ├── user.py            # User CRUD operations
│   │   ├── customer.py        # Customer CRUD operations
│   │   ├── product.py         # Product CRUD operations
│   │   └── order.py           # Order CRUD operations
│   └── api/
│       └── v1/
│           ├── router.py      # API router aggregation
│           └── endpoints/
│               ├── auth.py    # Authentication endpoints
│               ├── users.py   # User endpoints
│               ├── customers.py  # Customer endpoints
│               ├── products.py   # Product endpoints
│               └── orders.py     # Order endpoints
├── alembic/
│   ├── env.py                 # Alembic configuration
│   └── versions/              # Migration files
├── alembic.ini                # Alembic settings
├── requirements.txt
├── docker-compose.yml
├── .env.example
└── README.md
```

## Security Best Practices

### Implemented Security Features

1. **Password Security**
   - Bcrypt hashing with salt
   - Minimum password length enforcement
   - Password validation in Pydantic schemas

2. **JWT Authentication**
   - Token-based authentication
   - Configurable expiration time
   - Secure token generation with HS256

3. **Authorization**
   - Role-based access control (admin/user)
   - Endpoint protection with dependencies
   - User ownership validation for orders

4. **CORS Protection**
   - Configurable allowed origins
   - Credentials support
   - Preflight request handling

5. **Database Security**
   - SQL injection protection via SQLAlchemy
   - Parameterized queries
   - Connection pooling

### Production Checklist

- [ ] Change SECRET_KEY to a strong random value
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS/TLS
- [ ] Set appropriate CORS origins
- [ ] Use strong database credentials
- [ ] Enable database SSL connections
- [ ] Set up proper logging
- [ ] Configure rate limiting
- [ ] Use a reverse proxy (nginx)
- [ ] Set up monitoring and alerts

## Advanced Usage

### Filtering Orders

```bash
# Get orders by customer
curl "http://localhost:8000/api/v1/orders/?customer_id=1" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Get orders by status
curl "http://localhost:8000/api/v1/orders/?status=pending" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Get orders by date range
curl "http://localhost:8000/api/v1/orders/?start_date=2024-01-01&end_date=2024-12-31" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Search Functionality

```bash
# Search customers
curl "http://localhost:8000/api/v1/customers/?search=acme" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Search products
curl "http://localhost:8000/api/v1/products/?search=widget" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Order Statistics (Admin Only)

```bash
curl "http://localhost:8000/api/v1/orders/statistics" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

Response:
```json
{
  "total_orders": 150,
  "total_revenue": 15000.50,
  "by_status": {
    "pending": 10,
    "processing": 20,
    "shipped": 30,
    "delivered": 85,
    "cancelled": 5
  }
}
```

## Testing

Create a test file `test_main.py`:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
```

Run tests:
```bash
pytest
```

## Docker Deployment

### Build and run with Docker:

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t {{project_name}} .
docker run -p 8000:8000 {{project_name}}
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| PROJECT_NAME | Project name | {{project_name}} |
| API_V1_STR | API version prefix | /api/v1 |
| DATABASE_URL | PostgreSQL connection URL | postgresql://postgres:postgres@localhost:5432/{{project_name}}_db |
| SECRET_KEY | JWT secret key | (change in production) |
| ALGORITHM | JWT algorithm | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration time | 30 |
| ALLOWED_ORIGINS | CORS allowed origins | ["http://localhost:3000"] |
| RATE_LIMIT_PER_MINUTE | API rate limit | 60 |

## Troubleshooting

### Database Connection Issues

```bash
# Check if PostgreSQL is running
docker-compose ps

# View PostgreSQL logs
docker-compose logs postgres

# Restart PostgreSQL
docker-compose restart postgres
```

### Migration Issues

```bash
# Check current migration version
alembic current

# View migration history
alembic history

# Reset database (CAUTION: destroys data)
alembic downgrade base
alembic upgrade head
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Support

For issues and questions, please open an issue on GitHub.
