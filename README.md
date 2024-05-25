# Shift-rest
REST-сервис просмотра текущей зарплаты и даты следующего повышения.

# Документация проекта

## Описание
 - alembic - папка с миграциями
 - src - папка с исходным кодом
 - .env.fastapi.dev - файл с переменными окружения для разработки
 - src/auth - приложение с роутами для аутентификации
 - src/salary - приложение с роутами для просмотра зарплаты и даты следующего повышения

## Требования
 - Docker
 - Git
 - Созданный и заполненный .env.fastapi.dev файл

## Клонирование репозитория 

1. Клонируйте репозиторий:

```bash
git clone <url репозитория>
```

2. Перейдите в директорию проекта:

```bash
cd shift-rest
```

## Добавление .env файлов

1. Создайте и заполните файл `.env.fastapi.dev` следующим образом:

```dev
DB_PORT=5432
DB_HOST=db
DB_NAME=postgres
DB_USER=postgres
DB_PASS=12345

SECRET_KEY = "60a66d11eea3a05709692535550f27e4a8ad8469598ab4df46e4057ebc6f5226"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

POSTGRES_USER=postgres
POSTGRES_PASSWORD=12345
POSTGRES_DB=postgres
```

## Запуск

1. Запустите Docker Compose:

```bash
docker-compose build
docker-compose up -d
```

После этого приложение будет доступно по адресу `http://0.0.0.0:8000`.

## Что происходит при запуске
При запуске Docker Compose выполняются следующие действия:
1. Создается контейнер с PostgreSQL.
2. Создается контейнер с FastAPI.
3. Применяются миграции к базе данных.
4. Создаются 10 пользователей связанных с 10-ю записями о зарплате в базе данных:
   - Пользователи: `user0`, `user1`, ..., `user9`
   - Пароли: `password0`, `password1`, ..., `password9`
5. Запускается FastAPI.

## Документация API

Документация API доступна по адресу `http://0.0.0.0:8000/docs`.
Доступно два эндпоинта:
-  `/auth/login` - аутентификация пользователя. Response: 
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```
- `/salary` - просмотр зарплаты и даты следующего повышения пользователя. Response:
```json
{
  "salary_amount": "int",
  "next_increase": "Y:M:D"
}
```

### Отправка запросов с помощью Postman
Для обращения к `/token` POST через Postman, вам нужно следовать следующим шагам:

1. Откройте Postman.
2. Введите URL `http://localhost:8000/auth/token`.
3. Убедитесь, что выбран метод `POST`.
4. Перейдите на вкладку `Body`, затем выберите `x-www-form-urlencoded`.
5. Добавьте два ключа: `username` и `password`, и установите их значения в соответствии с вашими учетными данными.
6. Нажмите кнопку `Send` для отправки запроса.
7. Скопируйте токен из ответа и используйте его для доступа к другим эндпоинтам.

Для обращения к `/salary` GET через Postman, вам нужно следовать следующим шагам:

1. Откройте Postman.
2. Введите URL `http://localhost:8000/salary`.
3. Убедитесь, что выбран метод `GET`.
4. Вам также может потребоваться добавить токен авторизации в заголовки запроса. Для этого перейдите на вкладку `Headers` и добавьте новый заголовок с именем `Authorization` и значением `Bearer {ваш токен}`.
5. Нажмите кнопку `Send` для отправки запроса.

Пожалуйста, учтите, что `{ваш токен}` нужно заменить на реальный токен, который вы получили при аутентификации.

## Завершение работы

**Не забудьте остановить контейнеры** после завершения работы, так как они должны быть удалены, потому что при каждом запуске docker-compose создаются новые пользователи и записи о зарплате, что может привести к конфликтам.
```bash
docker-compose down
```
