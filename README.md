# :wrench: Home-Business
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/EvgVol)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
![Tests](https://raw.githubusercontent.com/EvgVol/rent_play/main/badges/tests.svg)
[![codecov](https://codecov.io/gh/EvgVol/rent_play/branch/main/graph/badge.svg?token=YB05m6VK4R)](https://codecov.io/gh/EvgVol/rent_play)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![CI](https://github.com/EvgVol/rent_play/actions/workflows/rentplay_worflow.yml/badge.svg)](https://github.com/EvgVol/rent_play/actions/workflows/rentplay_worflow.yml)
[![docker](https://img.shields.io/badge/-Docker-464646??style=flat-square&logo=docker)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646??style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

Arranging the rental of game consoles – a lucrative business idea...

Today, there are numerous gamers who enjoy playing a variety of computer games, including children. However, not everyone can afford to purchase a modern game console due to its high cost. This is where entrepreneurs who rent out consoles come to the rescue. It's a profitable venture for them.

## Structure
More information about the project can be found in the dynamic documentation generated using the module: [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/).
The documentation is available at: `http://127.0.0.1:8000/redoc/`.

Static documentation will be generated upon completion of the application development `backend`
____
1. [Basic project models](#Basic-project-models)
2. [User-permissions](#User-permissions)
    - [Unauthorized user](#Unauthorized-user)
    - [Authorized-user](#Authorized-user)
    - [Rentor](#Rentor)
    - [Administrator](#Administrator)
3. [Administrator page](#Administrator-page)
4. [Infrastructure](#Infrastructure)
5. [Project services and pages](#Project-services-and-pages)
6. [Project launch](#Project-launch)
7. [Code styling](#Code-styling)
8. [Test coverage](#Test-coverage)
9. [Status update](#Status-update)

____

##  Basic project models

### User
- :heavy_check_mark: Username
- :heavy_check_mark: First name
- :heavy_check_mark: Last name
- :heavy_check_mark: Email
- :heavy_check_mark: Phone number
- :heavy_check_mark: Image
- :heavy_check_mark: Role (rentor, user)
- :white_large_square: Rating

### Game console
- :heavy_check_mark: Author(rentor)
- :heavy_check_mark: Name
- :heavy_check_mark: Image
- :heavy_check_mark: Description
- :heavy_check_mark: Status (free, busy)
- :heavy_check_mark: Categories(slim, pro, xbox и пр.)
- :heavy_check_mark: Barcode
- :heavy_check_mark: Rating
- :heavy_check_mark: Rental price

### Game
- :heavy_check_mark: Name
- :heavy_check_mark: Image
- :heavy_check_mark: Description
- :heavy_check_mark: Tags(single, multi - user, etc.)

### Tag, Category
- :heavy_check_mark: Name
- :heavy_check_mark: HEX-color
- :heavy_check_mark: Slug

### Order
- :heavy_check_mark: User
- :heavy_check_mark: Game console
- :heavy_check_mark: Date start 
- :heavy_check_mark: Date end

[:arrow_up:Structure](#Structure)
____

## User-permissions

### Unauthorized user
- :eye: Allowed:
    - :heavy_check_mark: Create an account
    - :heavy_check_mark: View consoles
    - :heavy_check_mark: View games
    - :white_large_square: View rental pages
    - :white_large_square: Filter games by tags
    - :white_large_square: Filter consoles by categories
- :construction: Запрещено:


### Authorized-user
- :eye: Allowed:
    - :white_large_square: Has the rights of an unauthorized user
    - :heavy_check_mark: Logging into the system with their own login and password
    - :heavy_check_mark: Logging out of the system (logging out)
    - :heavy_check_mark: Changing password
    - :heavy_check_mark: Creating orders
    - :white_large_square: Tracking the status of orders
    - :heavy_check_mark: Adding / removing to favorites
    - :heavy_check_mark: Leaving reviews
    - :heavy_check_mark: Leaving comments on reviews
    - :ballot_box_with_check: Subscribing to lessors
    - :white_large_square: Evaluating lessors
- :construction: Запрещено:
    - :ballot_box_with_check: Подписываться на себя и других пользователей

### Rentor
- :eye: Allowed:
    - :white_large_square: Обладает правами авторизованного пользователя
    - :heavy_check_mark: Размещать игровые приставки
    - :white_large_square: Управлять заказами (отменять, редактировать дату, отмечать как завершенный)
    - :white_large_square: Оценивать арендателей
- :construction: Запрещено:
    - :ballot_box_with_check: Подписываться на кого-либо


[:arrow_up:Structure](#Structure)
____

## Administrator page

[:arrow_up:Structure](#Structure)
____

## Infrastructure

В репозитории есть папки backend, badges, tests:
* В папке `backend` — файлы, необходимые для сборки бэкенд приложения.
* В папке `tests` — файлы, необходимые для тестирования бэкенд приложения.
* В папке `badges` — бейджи, необхдимые для добавления в файл README

Continuous integration with GitHub Actions

Для работы с Workflow добавить в Secrets GitHub переменные окружения для работы:
```bash
CODECOV_TOKEN #Секретный токен сервиса: https://codecov.io
```
Workflow состоит из следующих этапов:
-   Проверка кода на соответствие PEP8
-   Тестирование приложения `backend` посредством pytest

[:arrow_up:Structure](#Structure)

____

## Project services and pages

[:arrow_up:Structure](#Structure)
____

## Project launch

1. Клонирование репозитория
```
git clone https://github.com/EvgVol/rent_play.git
```

Откройте в своем редакторе кода локальный проекта из репозитория GitHub, клонированного ранее

2. Развертывание в репозитории виртуального окружения
```
python3 -m venv venv
```
3. Запуск виртуального окружения
```
source venv/Scripts/activate
```
4. Установка зависимостей в виртуальном окружении
```
pip install -r requirements.txt
```

5. Выполнение миграций
```
python manage.py migrate
```

6. Выполните импорт данных (категории, теги, периоду) в базу данных
```
python manage.py importcsv
```

7. Запустите проект
```
python manage.py runserver
```

[:arrow_up:Structure](#Structure)
____

## Code styling
Код соответствует [PEP 8](https://pep8.org/)

[:arrow_up:Оглавление](#Оглавление)
____

## Test coverage
![codecov](https://codecov.io/gh/EvgVol/rent_play/branch/main/graphs/tree.svg?token=YB05m6VK4R)

[:arrow_up:Structure](#Structure)
____


## Team developers

- **BACKEND** - [EvgVol](https://github.com/EvgVol)

____

##  Status update

| Иконка | Статус | 
|----------------|:---------:|
| :ballot_box_with_check: | Реализовано и проверено |
| :white_check_mark: | Реализовано полностью |
| :heavy_check_mark: | Реализовано частично |
| :white_large_square: | Не реализовано |
| :interrobang: | Возникли трудности |
| :sos: | Нужна помощь |


[:arrow_up:Structure](#Structure)
____
