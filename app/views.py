# app/views.py
from fastapi import HTTPException, Path, APIRouter, status
from fastapi.responses import RedirectResponse

from .models import Url
from .utils import generate_short_url, is_url_alive
from .database import redis_cache, db


router = APIRouter()


@router.post(
    "/generate_short_url/",
    tags=["links"],
    summary="Создать короткую ссылку из длинной",
    description="Принимает длинную URL-ссылку и возвращает сгенерированную короткую ссылку.",
    response_description="Сгенерированная короткая ссылка",
)
async def create_short_url(url: Url):
    # Проверяем существование URL
    if not await is_url_alive(url.long_url):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="URL doesn't exist or is unreachable")

    # Проверяем, есть ли уже такая длинная ссылка в базе данных
    existing_entry = await db.links.find_one({"long_url": url.long_url})
    if existing_entry:
        return {"short_url": existing_entry["_id"]}

    # Иначе, создать новую короткую ссылку
    short_url = generate_short_url()
    await db.links.insert_one({"_id": short_url, "long_url": url.long_url, "count": 0})

    return {"short_url": short_url}


@router.get(
    "/get_long_url/{short_url}",
    tags=["links"],
    summary="Получить длинную ссылку из короткой",
    description="По заданной короткой ссылке возвращает соответствующую длинную ссылку.",
    response_description="Длинная URL-ссылка, соответствующая короткой",
)
async def get_long_url(
    short_url: str = Path(..., min_length=5, max_length=5, description="Короткая ссылка, для которой требуется получить длинный URL")
):
    # Получаем длинную ссылку из кэша Redis
    cached_url = redis_cache.get(short_url)
    if cached_url:
        return {"long_url": cached_url.decode()}

    # Если длинной ссылки нет в кэше, ищем ее в базе данных
    long_url_data = await db.links.find_one({"_id": short_url})
    if not long_url_data:
        raise HTTPException(status_code=404, detail="Short URL not found")

    # Кэшируем длинную ссылку в Redis
    redis_cache.setex(short_url, 3600, long_url_data["long_url"])  # Время указываем в секундах
    return {"long_url": long_url_data["long_url"]}


@router.get(
    "/{short_url}",
    tags=["links"],
    summary="Редирект по короткой ссылке на длинный URL",
    description="Перенаправляет пользователя на длинный URL, соответствующий заданной короткой ссылке.",
)
async def redirect(
    short_url: str = Path(..., min_length=5, max_length=5, description="Короткая ссылка для редиректа на длинный URL")
):
    # Ищем длинную ссылку в базе данных для редиректа
    long_url_data = await db.links.find_one({"_id": short_url})
    if not long_url_data:
        raise HTTPException(status_code=404, detail="Short URL not found")

    # Увеличиваем счетчик переходов по ссылке
    await db.links.update_one({"_id": short_url}, {"$inc": {"count": 1}})

    # Выполняем редирект на длинный URL
    return RedirectResponse(url=long_url_data["long_url"])


@router.get(
    "/count/{short_url}",
    tags=["links"],
    summary="Получить количество переходов по короткой ссылке",
    description="Показывает, сколько раз пользователи переходили по заданной короткой ссылке.",
    response_description="Количество переходов по короткой ссылке",
)
async def get_count(
    short_url: str = Path(..., min_length=5, max_length=5, description="Короткая ссылка, для которой требуется узнать количество переходов")
):
    # Получаем количество переходов по данной короткой ссылке из базы данных
    url_data = await db.links.find_one({"_id": short_url})
    if not url_data:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"count": url_data["count"]}