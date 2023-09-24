# app/database.py
from redis import Redis
import motor.motor_asyncio

# Инициализация кэша Redis
redis_cache = Redis(host="cache", port=6379)

# Инициализация MongoDB
mongo_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://db/:27017")
db = mongo_client.shortlinker
