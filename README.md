# :wrench: Home-Business
[![CI](https://github.com/EvgVol/rent_play/actions/workflows/rentplay_worflow.yml/badge.svg)](https://github.com/EvgVol/rent_play/actions/workflows/rentplay_worflow.yml)
![Tests](https://raw.githubusercontent.com/EvgVol/rent_play/main/badges/tests.svg)
[![codecov](https://codecov.io/gh/EvgVol/rent_play/branch/main/graph/badge.svg?token=YB05m6VK4R)](https://codecov.io/gh/EvgVol/rent_play)

Arranging the rental of game consoles – the idea of a business... 

Today there are a lot of people – gamers who love to play a variety of computer games, not to mention children. Although not everyone can afford to purchase a modern game console due to its price. Entrepreneurs who rent out consoles come to the rescue. It's project for them.

## Оглавление
Более подробно с проектом можно ознакомиться в диначеской документацией, сформиронной при помощи модуля [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/).
Документация доступна по адресу `http://127.0.0.1:8000/redoc/`.

Статическая документация, будет сформирована после завершение разработки приложения `backend`
____
1. [Базовые модели проекта](#Базовые-модели-проекта)
2. [Права пользователей](#Права-пользователей)
    - [Неаторизованный пользователь](#Неаторизованный-пользователь)
    - [Авторизованный пользователь](#Авторизованный-пользователь)
    - [Арендодатель](#Арендодатель)
    - [Администратор](#Администратор)
3. [Страница администратора](#Страница-администратора)
4. [Инфраструктура](#Инфраструктура)
5. [Сервисы и страницы проекта](#Сервисы-и-страницы-проекта)
6. [Запуск проекта](#Запуск-проекта)
7. [Оформление кода](#Оформление-кода)
8. [Покрытие тестами](#Покрытие-тестами)
9. [Статус работы](#Статус-работы)

____

##  Базовые модели проекта

### Пользователь
- :heavy_check_mark: Логин
- :heavy_check_mark: Имя пользователя
- :heavy_check_mark: Фамилия
- :heavy_check_mark: Email
- :heavy_check_mark: Номер телефона
- :heavy_check_mark: Изображение
- :heavy_check_mark: Роль (арендатель, арендодатель)
- :white_large_square: Рейтинг

### Игровая консоль
- :heavy_check_mark: Владелец консоли(арендодатель)
- :heavy_check_mark: Наименовение
- :heavy_check_mark: Изображение
- :heavy_check_mark: Описание
- :heavy_check_mark: Статус (свободна, занята)
- :heavy_check_mark: Категория(slim, pro, xbox и пр.)
- :heavy_check_mark: Штрих-код
- :heavy_check_mark: Рейтинг
- :heavy_check_mark: Стоимость аренды

### Игра
- :heavy_check_mark: Название
- :heavy_check_mark: Изображение
- :heavy_check_mark: Описание
- :heavy_check_mark: Тег(одиночная, многопользователькая и др.)

### Тег, категория
- :heavy_check_mark: Название
- :heavy_check_mark: Цветовой HEX-код
- :heavy_check_mark: Slug

### Заказ
- :heavy_check_mark: Арендатель
- :heavy_check_mark: Игровая приставка
- :heavy_check_mark: Дата начала аренды
- :heavy_check_mark: Дата окончание аренды

[:arrow_up:Оглавление](#Оглавление)
____

## Права пользователей

### Неаторизованный пользователь
- :eye: Разрешено:
    - :heavy_check_mark: Создать аккаунт
    - :heavy_check_mark: Просматривать приставки
    - :heavy_check_mark: Просматривать игры
    - :white_large_square: Просматривать страницы арендодателей
    - :white_large_square: Фильтровать игры по тегам
    - :white_large_square: Фильтровать игровые приставки по категориям
- :construction: Запрещено:


### Авторизованный пользователь
- :eye: Разрешено:
    - :white_large_square: Обладает правами неавторизованного пользователя
    - :heavy_check_mark: Входить в систему под своим логином и паролем
    - :heavy_check_mark: Выходить из системы (разлогиниваться)
    - :heavy_check_mark: Менять свой пароль
    - :heavy_check_mark: Создавать заказы
    - :white_large_square: Отслеживать статус заказов
    - :heavy_check_mark: Добавлять/удалять в избранное 
    - :heavy_check_mark: Оставлять отзывы
    - :heavy_check_mark: Оставлять комментария к отзывам
    - :ballot_box_with_check: Подписываться на арендодателей
    - :white_large_square: Оценивать арендодателей
- :construction: Запрещено:
    - :ballot_box_with_check: Подписываться на себя и других пользователей

### Арендодатель
- :eye: Разрешено:
    - :white_large_square: Обладает правами авторизованного пользователя
    - :heavy_check_mark: Размещать игровые приставки
    - :white_large_square: Управлять заказами (отменять, редактировать дату, отмечать как завершенный)
    - :white_large_square: Оценивать арендателей
- :construction: Запрещено:
    - :ballot_box_with_check: Подписываться на кого-либо


[:arrow_up:Оглавление](#Оглавление)
____

## Страница администратора

[:arrow_up:Оглавление](#Оглавление)
____

## Инфраструктура

В репозитории есть папки backend, badges, tests:
* В папке `backend` — файлы, необходимые для сборки бэкенд приложения.
* В папке `tests` — файлы, необходимые для тестирования бэкенд приложения.
* В папке `badges` — бейджи, необхдимые для добавления в файл README

Для работы с Workflow добавить в Secrets GitHub переменные окружения для работы:
```bash
CODECOV_TOKEN #Секретный токен сервиса: https://codecov.io
```
Workflow состоит из следующих этапов:
-   Проверка кода на соответствие PEP8
-   Тестирование приложения `backend` посредством pytest

[:arrow_up:Оглавление](#Оглавление)

____

## Сервисы и страницы проекта

[:arrow_up:Оглавление](#Оглавление)
____

## Запуск проекта

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

[:arrow_up:Оглавление](#Оглавление)
____

## Оформление кода
Код соответствует [PEP 8](https://pep8.org/)

[:arrow_up:Оглавление](#Оглавление)
____

## Покрытие тестами
![codecov](https://codecov.io/gh/EvgVol/rent_play/branch/main/graphs/tree.svg?token=YB05m6VK4R)

[:arrow_up:Оглавление](#Оглавление)
____


## Команда разработки

- **BACKEND** - [EvgVol](https://github.com/EvgVol)

____

##  Статус работы

| Иконка | Статус | 
|----------------|:---------:|
| :ballot_box_with_check: | Реализовано и проверено |
| :white_check_mark: | Реализовано полностью |
| :heavy_check_mark: | Реализовано частично |
| :white_large_square: | Не реализовано |
| :interrobang: | Возникли трудности |
| :sos: | Нужна помощь |


[:arrow_up:Оглавление](#Оглавление)
____
