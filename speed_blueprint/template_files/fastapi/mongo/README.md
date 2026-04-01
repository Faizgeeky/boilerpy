# {{project_name}}

A FastAPI application with MongoDB (Motor async driver) for high-performance document storage and retrieval.

## Features

- **Async MongoDB**: Motor async driver for non-blocking database operations
- **Modern FastAPI**: Built with FastAPI and async/await patterns
- **CRUD Operations**: Complete Create, Read, Update, Delete operations
- **Pagination**: Built-in pagination support for listing items
- **Filtering**: Filter items by status and other attributes
- **Data Validation**: Pydantic v2 models with comprehensive validation
- **CORS**: Configured CORS middleware
- **Docker**: MongoDB and Mongo Express included in docker-compose
- **Type Safety**: Full type hints throughout the codebase

## Prerequisites

- Python 3.8+
- MongoDB (or use Docker Compose)

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
# Edit .env with your MongoDB credentials
```

## Running with Docker

Start MongoDB and Mongo Express:
```bash
docker-compose up -d
```

This will start:
- MongoDB on port 27017
- Mongo Express (Web UI) on port 8081

Access Mongo Express at http://localhost:8081 to view your database.

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Interactive API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Items

- `POST /api/v1/items/` - Create a new item
- `GET /api/v1/items/` - List all items (with pagination and filtering)
- `GET /api/v1/items/count` - Count items
- `GET /api/v1/items/{item_id}` - Get a specific item
- `PUT /api/v1/items/{item_id}` - Update an item
- `DELETE /api/v1/items/{item_id}` - Delete an item

### Example Requests

**Create an item:**
```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Premium Widget",
    "description": "High-quality widget",
    "price": 29.99,
    "quantity": 100,
    "is_active": true
  }'
```

**List items with pagination:**
```bash
curl "http://localhost:8000/api/v1/items/?skip=0&limit=10&is_active=true"
```

**Update an item:**
```bash
curl -X PUT "http://localhost:8000/api/v1/items/{item_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 24.99,
    "quantity": 150
  }'
```

**Count items:**
```bash
curl "http://localhost:8000/api/v1/items/count?is_active=true"
```

## Project Structure

```
{{project_name}}/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point with lifespan
│   ├── core/
│   │   ├── config.py          # Configuration settings
│   │   └── database.py        # MongoDB connection manager
│   ├── models/
│   │   └── item.py            # MongoDB document models
│   ├── schemas/
│   │   └── item.py            # Pydantic schemas for validation
│   ├── crud/
│   │   └── item.py            # Async CRUD operations
│   └── api/
│       └── v1/
│           ├── router.py      # API router aggregation
│           └── endpoints/
│               └── items.py   # Item endpoints
├── requirements.txt
├── docker-compose.yml
├── .env.example
└── README.md
```

## MongoDB Connection

The application uses Motor, an async MongoDB driver for Python. The connection is managed through the application lifespan:

- **Startup**: Connects to MongoDB
- **Shutdown**: Gracefully closes the connection

Connection pooling is handled automatically by Motor.

## Data Model

### Item

```python
{
  "_id": "ObjectId",
  "name": "string",
  "description": "string (optional)",
  "price": "float",
  "quantity": "integer",
  "is_active": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black app/
isort app/
```

### Type Checking

```bash
mypy app/
```

## MongoDB Operations

### Indexes

Create indexes for better performance:

```javascript
// Connect to MongoDB
use {{project_name}}_db

// Create indexes
db.items.createIndex({ "name": 1 })
db.items.createIndex({ "is_active": 1 })
db.items.createIndex({ "created_at": -1 })
```

### Aggregation Example

```python
# Add to crud/item.py for advanced queries
async def get_active_items_stats():
    collection = mongodb.get_collection(settings.ITEMS_COLLECTION)
    pipeline = [
        {"$match": {"is_active": True}},
        {"$group": {
            "_id": None,
            "total_quantity": {"$sum": "$quantity"},
            "avg_price": {"$avg": "$price"},
            "count": {"$sum": 1}
        }}
    ]
    cursor = collection.aggregate(pipeline)
    result = await cursor.to_list(length=1)
    return result[0] if result else None
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| PROJECT_NAME | Project name | {{project_name}} |
| API_V1_STR | API version prefix | /api/v1 |
| MONGODB_URL | MongoDB connection URL | mongodb://localhost:27017 |
| MONGODB_DB_NAME | Database name | {{project_name}}_db |
| ITEMS_COLLECTION | Items collection name | items |
| ALLOWED_ORIGINS | CORS allowed origins | ["http://localhost:3000"] |

## Production Deployment

### Security Considerations

1. **Use strong MongoDB credentials**
2. **Enable MongoDB authentication**
3. **Use connection string with credentials**
4. **Enable SSL/TLS for MongoDB connections**
5. **Set proper CORS origins**
6. **Use environment variables for sensitive data**

### Recommended MongoDB Setup

```yaml
# docker-compose.prod.yml
version: '3.8'
services:
  mongodb:
    image: mongo:7.0
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_USER}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASSWORD}
    volumes:
      - mongodb_data:/data/db
    command: --auth
```

### Performance Tips

1. **Create appropriate indexes** on frequently queried fields
2. **Use projection** to limit returned fields
3. **Implement connection pooling** (handled by Motor)
4. **Enable query profiling** in MongoDB
5. **Monitor slow queries**

## License

MIT License
