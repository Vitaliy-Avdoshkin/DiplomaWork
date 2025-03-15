# Vitaliy_Avdoshkin_DiplomaWork

# Приложение для сайта типа "Доска объявлений"

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

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки flak8


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
```

5. Установите требуемые библиотеки:
````commandline
poetry add requests
poetry add python-dotenv
poetry add psycopg2
poetry add django
poetry add redis
````

6. Инициализируйте django-проект внутри текущей директории
````
django-admin startproject config .
````

## Приложение Доска объявлений:

1. Создайте приложение bulletinboard
````
python manage.py startapp bulletinboard
python manage.py startapp users
````
2. Зарегистрируйте приложения в settings.py
3. Для приложения lms создайте модели: Course, Lesson, Subscription
4. Для приложения users создайте модели: User, Payment
5. Опишите CRUD для всех моделей на основе ViewSet и Generic-классов
6. Создайте сериализаторы
7. Настройте права доступа
8. Опишите требуемые валидаторы
9. Добавьте пагинацию
10. Протестируйте полученный код
11. Поключите и настройте вывод документации для проекта
12. Настройте celery. Запуск селери и воркер : celery -A config worker --beat --scheduler django --loglevel=info
13. Запуск селери и воркер : celery -A config worker --beat --scheduler django --loglevel=info
14. Как запускать с докер из консоли: Ввести команду для сборки образов и запуска контейнеров: docker-compose up -d —build