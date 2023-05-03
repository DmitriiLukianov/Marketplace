# Проект агрегатора товаров для различных продавцов (мультибрендовый интернет-магазин).

## Как запустить проект:

- Установить зависимости: `pip install -r requirements.txt`

- Выполнить миграции: `python manage.py migrate`

- Загрузить фикстуры:
`python manage.py loaddata users.json profiles.json categories.json products.json reviews.json deliveries.json orders.json`

- Запустить сервер: `python manage.py runserver`

- Перейти в браузере по ссылке: `localhost:8000`