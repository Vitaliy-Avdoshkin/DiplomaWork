# Vitaliy_Avdoshkin_DiplomaWork

# SPA-Приложение для сайта типа "Доска объявлений"

## Описание

Backend-часть для сайта объявлений.
Бэкенд-часть проекта имеет следующий функционал:
- Регистрация пользователя с подтверждением почты.
- Авторизация и аутентификация пользователей.
- Изменение пароля через электронную почту.
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- CRUD для отзывов (админ может удалять или редактировать все отзывы, а пользователи только свои).
- В заголовке сайта можно осуществлять поиск объявлений по названию.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/Vitaliy-Avdoshkin/DiplomaWork.git
```
## Конфигурация
1. Создайте виртуальное окружение poetry.
```
poetry env
```
2. Примените зависимости с файла pyproject.toml
```
poetry install
```
3. Создайте файл .env и внесите все чувствительные параметры указанные в файле .env.sample
4. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

5. Создайте файл .flake8 для настройки библиотеки flak8

6. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 140
```

7. Установите требуемые библиотеки:
````commandline
poetry add requests
poetry add python-dotenv
poetry add psycopg2
poetry add django
poetry add redis
poetry add djangorestframework-simplejwt
poetry add Pillow
poetry add django-cors-headers
poetry add docker
````
8. Инициализируйте django-проект внутри текущей директории
````
django-admin startproject config .
````

## Тестирование

1. Для тестирования кода установите Pytest
```
poetry add --group dev pytest-django
```
2. Создайте файл pytest.ini и настройте библиотеку pytest, используя код ниже
```
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = tests.py tests_*.py *_tests.py
filterwarnings =
    ignore::django.utils.deprecation.RemovedInDjango60Warning
```    
3. Установите Code coverage для расчета процента протестированного кода
```
poetry add --group dev pytest-cov
```
Запуск Code coverage
```commandline
pytest --cov
```
Чтобы сгенерировать отчет о покрытии в HTML-формате, используйте следующую команду
```commandline
pytest --cov=src --cov-report=html
```
Отчет будет сгенерирован в папке
```
htmlcov
```
 и храниться в файле с названием 
```
index.html
```

4. Для тестирования вывода в консоль используйте специальную фикстуру
```
capsys
```

## Приложение Доска объявлений:

1. Создайте приложение announcements
````
python manage.py startapp announcements
python manage.py startapp users
````
2. Зарегистрируйте приложения в settings.py
3. Для приложения announcements создайте модели: Announcements, Review
4. Для приложения users создайте модели: User
5. Опишите CRUD для всех моделей на основе ViewSet и Generic-классов
6. Создайте сериализаторы
7. Настройте права доступа
8. Опишите требуемые валидаторы
9. Добавьте пагинацию
10. Для заполнения базы данных примените подготовленные фикстуры: fixture_announcements, fixture_review.json, fixture_users.json
````
python3 manage.py loaddata fixture_announcements fixture_review.json fixture_users.json
````
11. В случае необходимости базы данных с суперпользователем, то выполните команду csu
````
python3 manage.py csu
````
12. Для деплоя проекта на Docker

Запуск:
````
docker-compose up -d --build
````   
Остановка:
```` 
docker compose down
```` 

## Документация и безопасность

В файле urls.py создана схема документации. 
Просмотр документации доступен по ссылкам:
```` 
http://localhost:8000/swagger/ для Swagger UI 
http://localhost:8000/redoc/ для Redoc
```` 
Реализована настройка CORS.