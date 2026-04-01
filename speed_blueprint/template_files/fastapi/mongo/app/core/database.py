"""Database configuration for MongoDB."""
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.core.config import settings


class MongoDB:
    """MongoDB database manager."""

    client: Optional[AsyncIOMotorClient] = None
    database: Optional[AsyncIOMotorDatabase] = None

    async def connect_to_database(self):
        """Create database connection."""
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.database = self.client[settings.MONGODB_DB_NAME]
        print(f"Connected to MongoDB at {settings.MONGODB_URL}")

    async def close_database_connection(self):
        """Close database connection."""
        if self.client:
            self.client.close()
            print("Closed MongoDB connection")

    def get_collection(self, collection_name: str):
        """Get a collection from the database."""
        if self.database is None:
            raise RuntimeError("Database not initialized")
        return self.database[collection_name]


mongodb = MongoDB()
