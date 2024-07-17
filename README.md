# Redpanda_shop Specification

## Direcotory structure

```tree
rendpanda_shop
├── config --> settings.py, urls.py, wsgi.py, asgi.py
├── static --> media
├── secrets --> yaml
├── templates --> htmls
├── cart --> cart app
├── account --> user model
└── store --> product model, category model
```

## Database
Using sqlite3

### Tablelist
1.  django_admin_log
2.  django_content_type
3.  django_migrations
4.  django_session
5.  store_category
6.  store_product


### store_category schema

| Column Name | Data Type | Constraints |
|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| category_name | VARCHAR(100) | NOT NULL |
| slug | VARCHAR(100) | NOT NULL, UNIQUE |

### store_product schema

| Column Name | Data Type | Constraints |
|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| product_name | VARCHAR(100) | NOT NULL |
| slug | VARCHAR(100) | NOT NULL, UNIQUE |
| product_price | DECIMAL | NOT NULL |
| product_description | TEXT | NOT NULL |
| product_image | VARCHAR(100) | NOT NULL |
| can_return | BOOLEAN | NOT NULL |
| est_ship_date | VARCHAR(10) | NOT NULL |
| category_id | BIGINT | NOT NULL, FOREIGN KEY REFERENCES store_category(id) |

## django_session schema

| Column Name | Data Type | Constraints |
|---|---|---|
| session_key | VARCHAR(40) | PRIMARY KEY |
| session_data | TEXT | NOT NULL |
| expire_date | DATETIME | NOT NULL |

>session_data : serialized the cart item information





## Image handling for products

* install image handler
  
   `pip install pillow`
* create directory
```tree
├──config -->main configs
├──store
└── static
    └──media :product images uploaded #127.0.0.1:8000/media/images/BulletGuard-iPhone.jpg
```






## Active virtual env & run server
```
source Scripts/activate
cd project
python manage.py runserver
```

## DB Migaration
```
python manage.py makemigrations
python manage.py migrate
```

## create app

`python manage.py startapp cart`




### Notes
* AJAX, Jquery Session creation
`python manage.py shell`
```
>>>from django.contrib.sessions.models import Session
>>>session_key = Session.objects.get(pk="")
>>>session_key.get_decoded() #blank
>>>exit()
```