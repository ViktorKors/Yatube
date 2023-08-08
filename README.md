# API для приложения YaTube
___
Приложение Yatube - социальная сеть для публикации постов с возможностью создания личного блога, функционалом осуществления подписки на интересующих авторов и комментирования их записей.

API для приложения Yatube осуществлен на DRF. Аутентификация осуществляется по JWT-токену.

### Документация доступна по ссылке:

`http://127.0.0.1:8000/redoc/`


### Стэк технологий:

+ Python 3.9
+ Django                        3.2.16
+ django-filter                 23.2
+ djangorestframework           3.12.4
+ djangorestframework-simplejwt 4.7.2
+ djoser                        2.1.0
+ drf-yasg                      1.21.7
+ Pillow                        9.3.0
+ PyJWT                         2.1.0
+ requests                      2.26.0


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
`git@github.com:ViktorKors/api_final_yatube.git`

`cd api_final_yatube`

Cоздать и активировать виртуальное окружение:
`python3 -m venv env`

Linux:

`source env/bin/activate`

Windows:

`source env/Scripts/activate`

Установить зависимости из файла requirements.txt:

`python3 -m pip install --upgrade pip`

`pip install -r requirements.txt`

Выполнить миграции:

`python3 manage.py migrate`

Запустить проект:

`python3 manage.py runserver`



