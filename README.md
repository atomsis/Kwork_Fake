# Проект Kwork Fake

Проект Kwork Fake представляет собой веб-приложение, созданное для имитации платформы фриланс-услуг. В этом проекте пользователи могут регистрироваться, создавать профили как заказчиков, так и исполнителей.

## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/your_username/kwork_fake.git

```
2. Создайте виртуальное окружение и активируйте его:
```
python3 -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```
pip install -r requirements.txt

```
4. Выполните миграции:
```
python manage.py migrate

```
5. Создайте суперпользователя:
```
python manage.py createsuperuser
```
6. Запустите сервер:
```
python manage.py runserver
```
После этого проект будет доступен по адресу http://127.0.0.1:8000/.

## С чего начать?:
- Перейдите по ссылке:
  - http://127.0.0.1:8000/account/login/

## Структура проекта

- **accounts**: Приложение для регистрации и аутентификации пользователей.
- **profiles**: Приложение для создания профилей пользователей (заказчиков и исполнителей).


## Как использовать

1. Регистрация и аутентификация
    - Пользователи могут зарегистрироваться через форму регистрации, указав имя пользователя, электронную почту и пароль.
    - После регистрации пользователи могут войти в систему, используя свои учетные данные.

2. Создание профилей
    - После регистрации пользователи могут создать профили заказчика или исполнителя, заполнив соответствующие формы.
    - Профили могут содержать информацию о пользователе, его контактных данных и опыте работы.


## Разработка

- Используйте `python manage.py startapp <app_name>` для создания новых приложений Django.
- Добавляйте новые URL-адреса и представления в соответствующие файлы `urls.py` и `views.py`.
- Создавайте новые модели в файле `models.py` и выполняйте миграции при их изменении.
- Разрабатывайте фронтенд, создавая или изменяя HTML-шаблоны и файлы CSS/JavaScript в папках `templates` и `static`.

## Тестирование

- Используйте `python manage.py test` для запуска всех тестов в проекте.
