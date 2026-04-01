# {{project_name}} - Flask with MongoDB

A production-ready Flask REST API with MongoDB NoSQL database using PyMongo.

## Features

- **Flask 3.0** - Modern Python web framework
- **MongoDB** - NoSQL document database
- **Flask-PyMongo** - Flask extension for MongoDB
- **CORS Support** - Cross-origin resource sharing
- **Docker Support** - Easy deployment with Docker Compose
- **Input Validation** - Request validation with dataclasses
- **Advanced Querying** - Text search, filtering, and pagination
- **Bulk Operations** - Create multiple items at once
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
│   │           └── items.py     # Item CRUD endpoints
│   ├── core/
│   │   ├── config.py            # Configuration settings
│   │   └── database.py          # MongoDB setup
│   ├── models/
│   │   └── item.py              # Item model
│   └── schemas/
│       └── item.py              # Request/response schemas
├── .env.example                 # Environment variables template
├── docker-compose.yml           # Docker services configuration
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Quick Start

### Prerequisites

- Python 3.11+
- MongoDB 7.0+ (or use Docker)
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

5. **Start MongoDB (using Docker):**
   ```bash
   docker-compose up -d mongodb
   ```

6. **Run the application:**
   ```bash
   flask run
   # Or for production:
   gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
   ```

The API will be available at `http://localhost:5000`

## Using Docker Compose

Run the entire stack (MongoDB + Flask app):

```bash
docker-compose up -d
```

This will:
- Start MongoDB on port 27017
- Start the Flask app on port 5000
- Set up authentication and database

## API Endpoints

### Health Check

```bash
GET /health
```

### Items

**List Items (with filtering and pagination)**
```bash
GET /api/v1/items?skip=0&limit=10&category=electronics&min_price=10&max_price=100&search=phone
```

**Get Item**
```bash
GET /api/v1/items/{item_id}
```

**Create Item**
```bash
POST /api/v1/items
Content-Type: application/json

{
  "title": "Laptop",
  "description": "High-performance laptop",
  "price": 999.99,
  "quantity": 10,
  "category": "electronics"
}
```

**Update Item**
```bash
PUT /api/v1/items/{item_id}
Content-Type: application/json

{
  "price": 899.99,
  "quantity": 15
}
```

**Delete Item**
```bash
DELETE /api/v1/items/{item_id}
```

**Bulk Create Items**
```bash
POST /api/v1/items/bulk
Content-Type: application/json

[
  {
    "title": "Item 1",
    "description": "Description 1",
    "price": 10.00,
    "quantity": 5,
    "category": "category1"
  },
  {
    "title": "Item 2",
    "description": "Description 2",
    "price": 20.00,
    "quantity": 10,
    "category": "category2"
  }
]
```

## Query Parameters

### List Items

- `skip` - Number of items to skip (default: 0)
- `limit` - Maximum items to return (1-100, default: 100)
- `category` - Filter by category
- `min_price` - Minimum price filter
- `max_price` - Maximum price filter
- `search` - Search in item titles (case-insensitive)

**Example:**
```bash
curl "http://localhost:5000/api/v1/items?category=electronics&min_price=100&max_price=500&search=laptop&skip=0&limit=20"
```

## Configuration

Edit `.env` file to configure:

- `DEBUG` - Enable debug mode (True/False)
- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 5000)
- `SECRET_KEY` - Secret key for session management
- `ALLOWED_ORIGINS` - CORS allowed origins
- `MONGO_URI` - MongoDB connection string
- `MONGO_DBNAME` - MongoDB database name

## MongoDB Connection String Format

```
mongodb://[username:password@]host[:port]/[database][?options]
```

**Examples:**

Local without auth:
```
mongodb://localhost:27017/mydb
```

Local with auth:
```
mongodb://admin:password@localhost:27017/mydb?authSource=admin
```

Atlas (cloud):
```
mongodb+srv://username:password@cluster.mongodb.net/mydb
```

## Security Features

- **Input Validation** - All inputs are validated using schemas
- **NoSQL Injection Protection** - BSON ObjectId validation
- **CORS Configuration** - Configurable CORS for API security
- **Environment Variables** - Sensitive data in environment variables
- **Connection String Security** - Proper authentication handling

## MongoDB Document Schema

### Items Collection

```json
{
  "_id": ObjectId("..."),
  "title": "string (required, max 200 chars)",
  "description": "string (optional, max 1000 chars)",
  "price": "number (non-negative)",
  "quantity": "number (non-negative integer)",
  "category": "string (optional, max 100 chars)",
  "created_at": "ISODate",
  "updated_at": "ISODate"
}
```

## Indexes

For better performance, create indexes on frequently queried fields:

```javascript
// In MongoDB shell or Compass
db.items.createIndex({ "title": "text" })
db.items.createIndex({ "category": 1 })
db.items.createIndex({ "price": 1 })
db.items.createIndex({ "created_at": -1 })
```

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
   export MONGO_URI=mongodb://user:pass@host:27017/dbname
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

### MongoDB Atlas (Cloud)

For production, consider using MongoDB Atlas:

1. Create a free cluster at https://www.mongodb.com/cloud/atlas
2. Get your connection string
3. Update `MONGO_URI` in `.env`:
   ```
   MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/{{project_name}}
   ```

## Testing

Example curl commands:

**Create an item:**
```bash
curl -X POST http://localhost:5000/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Item",
    "description": "This is a test item",
    "price": 29.99,
    "quantity": 100,
    "category": "test"
  }'
```

**Search items:**
```bash
curl "http://localhost:5000/api/v1/items?search=test&category=test"
```

**Bulk create:**
```bash
curl -X POST http://localhost:5000/api/v1/items/bulk \
  -H "Content-Type: application/json" \
  -d '[
    {"title": "Item 1", "price": 10, "quantity": 5},
    {"title": "Item 2", "price": 20, "quantity": 10}
  ]'
```

## Troubleshooting

**Database connection errors:**
- Ensure MongoDB is running: `docker-compose ps`
- Check MONGO_URI in .env file
- Verify MongoDB authentication credentials

**Authentication errors:**
- Ensure using `authSource=admin` in connection string
- Verify username/password are correct

**Import errors:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**Port already in use:**
- Change PORT in .env file
- Or kill process using the port: `lsof -ti:5000 | xargs kill`

## MongoDB Tools

**MongoDB Compass:**
- GUI tool for MongoDB: https://www.mongodb.com/products/compass

**mongosh (MongoDB Shell):**
```bash
mongosh "mongodb://admin:admin@localhost:27017/{{project_name}}?authSource=admin"
```

## License

MIT License - feel free to use this project for your applications.
