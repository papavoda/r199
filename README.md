For production run:
git clone https://github.com/papavoda/r199.git
Copy .env-compose .env.prod .db.env to directories
docker compose --env-file .env-compose  -f docker-compose-PROD.yml up -d
docker exec -ti <YOUR_CONTAINER> python manage.py migrate
cat BACKUP.sql | docker exec -i  <DB_CONTAINER> psql -U <USER> -d <DB_NAME>
( last command run twice )

## Файлы окружения

`django/.env` — настройки Django для разработки; `django/.env.prod` — для production.
`db/.db.env` — параметры инициализации нового тома PostgreSQL.
Корневой `.env-compose` задаёт MEDIA_NGINX для production Compose.
Для нового окружения скопируйте соответствующие `.example`, заполните секреты и пути.
Production запускается с `--env-file .env-compose`: env_file сервиса web не используется
Compose для подстановки `${MEDIA_NGINX}`.

Используйте разные SECRET_KEY для dev и production. Создание нового ключа:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Изменение POSTGRES_PASSWORD в `.db.env` не меняет пароль существующей БД.
Сначала измените пароль средствами PostgreSQL, затем согласуйте DATABASE_URL.
Пароль внутри DATABASE_URL должен быть URL-кодирован.
Реальные env, медиа, локальные окружения и результаты аудита исключены из Git.
Секреты исключены из Docker build context и передаются при запуске.

## Обновление окружения — 30 октября 2026

Dockerfile для разработки и production используют Python 3.14.10 Alpine.
В requirements.txt закреплены Django 6.1.2 и обновлённые зависимости.
Python 3.15 пока не выбран: официальная поддержка в Django начинается с 6.1.3.
Удалена устаревшая подмена файла snowpenguin/recaptcha3: проект использует django_recaptcha.

Пересобрать и перезапустить только dev-сервис, сохранив контейнер БД:

```powershell
docker compose -f docker-compose.yml build web
docker compose -f docker-compose.yml up -d --no-deps web
docker compose -f docker-compose.yml exec web python --version
docker compose -f docker-compose.yml exec web python -m django --version
docker compose -f docker-compose.yml exec web python manage.py check
```

Локально зависимости установлены без конфликтов; 10 тестов прошли на Django 6.1.2
и Python 3.14.3 с SQLite в памяти при DEBUG=False и DEBUG=True.
Страницы админки и API также проверены на искусственных данных.
Сборка dev-образа дважды остановилась при обращении к Docker Hub
с ошибкой TLS handshake timeout, до загрузки базового образа.
Проверка на Python 3.14.10 Alpine и PostgreSQL остаётся необходимой.
Production-образ не собирался, работающие сервисы не перезапускались.

Известное расхождение миграций Price.updated (default=datetime.datetime.now())
существовало до обновления и остаётся отдельной задачей; новых миграций не создавалось.
