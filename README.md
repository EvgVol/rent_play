# :wrench: RENT&PLAY
Сервис по аренде игровых приставок. В проекте имеется возможность подобрать игры для себя или кампании. 

## Оглавление
Более подробно с проектом можно ознакомиться в спецификации API.
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

____

## Базовые модели проекта

[:arrow_up:Оглавление](#Оглавление)
____

## Права пользователей

### Неаторизованный пользователь
- :heavy_check_mark: Создать аккаунт
- :heavy_check_mark: Просматривать приставки
- :heavy_check_mark: Просматривать игры
- :white_large_square: Просматривать страницы арендодателей
- :white_large_square: Фильтровать игры по тегам
- :white_large_square: Фильтровать игровые приставки по категориям

### Авторизованный пользователь
- :white_large_square: Обладает правами неавторизованного пользователя 
- :white_large_square: Входить в систему под своим логином и паролем
- :white_large_square: Выходить из системы (разлогиниваться)
- :white_large_square: Менять свой пароль
- :heavy_check_mark: Создавать заказы
- :white_large_square: Отслеживать статус заказов
- :white_large_square: Добавлять/удалять в избранное 
- :heavy_check_mark: Оставлять отзывы
- :white_large_square: Оставлять комментария к отзывам
- :white_large_square: Подписываться на арендодателей
- :white_large_square: Оценивать арендодателей

### Арендодатель
- :white_large_square: Обладает правами авторизованного пользователя
- :white_large_square: Размещать игровые приставки
- :white_large_square: Управлять заказами (отменять, редактировать дату, отмечать как завершенный)
- :white_large_square: Оценивать арендателей

[:arrow_up:Оглавление](#Оглавление)
____

## Страница администратора

[:arrow_up:Оглавление](#Оглавление)
____

## Инфраструктура

[:arrow_up:Оглавление](#Оглавление)

____

## Сервисы и страницы проекта

[:arrow_up:Оглавление](#Оглавление)
____

## Запуск проекта

[:arrow_up:Оглавление](#Оглавление)
____

## Оформление кода
Код соответствует [PEP 8](https://pep8.org/)

[:arrow_up:Оглавление](#Оглавление)
____

## Команда разработки

- **BACKEND** - [EvgVol](https://github.com/EvgVol)

- **FRONTEND** - [Leliya](https://github.com/Leliya)
____