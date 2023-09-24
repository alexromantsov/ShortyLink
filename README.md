# ShortyLink: API-сервис сокращения ссылок на FastAPI

### Описание
_ShortyLink_ - это API-сервис на FastAPI для сокращения длинных URL-ссылок. Он использует MongoDB для хранения данных и Redis для кэширования. Пользователи могут предоставлять длинные URL-ссылки, и сервис вернет короткую ссылку, которая будет перенаправлять на оригинальный URL. Сервис также предоставляет возможность отслеживать, сколько раз была посещена каждая короткая ссылка.

### Основные возможности
* Генерация коротких URL-ссылок из длинных.
* Редирект с короткой ссылки на оригинальный URL.
* Отслеживание количества переходов по короткой ссылке.

### API Endpoints
1. Создать короткую ссылку:

* **Method**: POST
* **Endpoint**: `/generate_short_url/`
* **Body**: JSON с длинной ссылкой, например: `{"long_url": "https://github.com/alexromantsov/ShortyLink"}`


2. Получить длинную ссылку из короткой:

* **Method**: GET
* **Endpoint**: `/get_long_url/{short_url}`

3. Редирект по короткой ссылке:

* **Method**: GET
* **Endpoint**: `/{short_url}`

4. Получить количество переходов по короткой ссылке:

* **Method**: GET
* **Endpoint**: `/count/{short_url}`

### Демонстрационная Версия
Для ознакомления с ShortyLink, вы можете посетить демонстрационную версию API-сервера по следующей ссылке:
* [Swagger UI](http://185.4.74.136:5005/docs)
* [ReDoc](http://185.4.74.136:5005/redoc)


### Установка и запуск с использованием **Docker**
1. Необходимо убедитесь, что установлен Docker и Docker Compose.
2. Клонируем репозиторий:
```bash
git clone https://github.com/alexromantsov/ShortyLink.git
```
3. Переходим в папку проекта:
```bash
cd ShortyLink
```
4. Собираем образ и запускаем контейнеры
```bash
docker-compose up --build -d
```

### Документация API
* Swagger UI: [http://localhost:5005/docs](http://localhost:5005/docs)
* ReDoc: [http://localhost:5005/redoc](http://localhost:5005/redoc)


### Контакты
Если есть вопросы или предложения по улучшению проекта, пожалуйста, свяжитесь со мной.
<div>
    <div style="float: left; padding-top: 20px;">
        <img src="https://avatars.githubusercontent.com/u/64366980?v=4" style="width: 100px; height: 100px; border-radius: 50%; hspace: 20;">
    </div>
    <div style="float: left; padding-top: 20px;">
        <h3><a style="text-decoration: none; color: #696969" href="mailto:alekseyromantsov@gmail.com">Алексей Романцов<br></a></h3>
        👨‍💻 Все проекты: <a href="https://github.com/alexromantsov" target="_blank">https://github.com/alexromantsov</a> <br>
        👔 LinkedIn: <a href="https://www.linkedin.com/in/alexromantsov" target="_blank">https://www.linkedin.com/in/alexromantsov</a> <br>
        📞 Телефон: +7 (908) 209-39-99
    </div>
</div>