# Образ Python
FROM python:3.8-slim

# Установка рабочей директории
WORKDIR /app

# Установка всех библиотек зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY . .

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
