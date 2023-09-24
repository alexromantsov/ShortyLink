# app/utils.py
import random
import string
import httpx


# Генерация короткого URL
def generate_short_url() -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(5))


async def is_url_alive(url: str) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            # Таймаут на случай долгого ответа
            response = await client.get(url, timeout=10)

            # Возвращаем False, если статус начинается на 4 или 5
            if str(response.status_code).startswith(('4', '5')):
                return False
            return True
    except Exception:
        return False

