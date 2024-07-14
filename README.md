# Redpanda_shop

## Active virtual env & run server
```
source Scripts/activate
cd project
python manage.py runserver
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


`python manage.py startapp cart`


# Notes
* web socket -wsgi asgi
* url name space - urls.py
* oop, instanciation
* Django의 ORM
* def __init__, __init__= name, 
* @admin.register(Category)
* super()
* gitignore
* image upload
* why migration folder not eixst