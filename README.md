# Redpanda_shop

## Active virtual env & run server
```
source Scripts/activate
cd project
python manage.py runserver
```

## Migaration
```
python manage.py makemigrations
python manage.py migrate
```

## Direcotory structure

```tree
rendpanda_shop
├── config --> settings.py, urls.py, wsgi.py, asgi.py
├── static --> media
├── secrets --> yaml
├── cart --> app
└── store --> app
```


### APP - Store

* Install

`python manage.py startapp store`

```tree
store
├── admin.py - Add models in admin page
├── apps.py
├── models.py -make models from DB
├── tests.py
├── urls.py
└── views.py
```

* Image handling
  - install image handler `pip install pillow`
  - create directory
```tree
├──config -->main configs
├──store
└── static
    └──media :product images uploaded #127.0.0.1:8000/media/images/BulletGuard-iPhone.jpg
```


### APP - Cart

* Install

`python manage.py startapp cart`


```tree
cart
├── admin.py
├── apps.py
├── carts.py --> # manually create for cart session
├── contex_processors.py #manully create for cart session in settings.py
├── models.py -make models from DB
├── tests.py
├── urls.py
└── views.py
```


* Session creation

`python manage.py shell`

```
>>>from django.contrib.sessions.models import Session
>>>session_key = Session.objects.get(pk="")
>>>session_key.get_decoded() #blank
>>>exit()


```







* AJAX


### Notes
* カテゴリーボタン

