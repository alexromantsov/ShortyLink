# app/models.py
from pydantic import BaseModel


# Модель для длинного URL
class Url(BaseModel):
    long_url: str

