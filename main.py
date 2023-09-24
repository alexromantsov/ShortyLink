from fastapi import FastAPI
from app import views, database, docs

app = FastAPI(
    title=docs.API_TITLE,
    description=docs.API_DESCRIPTION,
    version=docs.API_VERSION,
)


# Инициализация кэша и базы данных
redis_cache = database.redis_cache
db = database.db

# Добавление маршрутов из views.py
app.include_router(views.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
