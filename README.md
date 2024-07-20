# Redpanda_shop Specification

## 実現したいこと
1. AdminでUSER, 商品, カテゴリーのCRUDができるようにデータモデルを作る
    * カテゴリー　→　カテゴリーVIEW
    * USER  →　Profile(USERに紐づく配送先住所、お名前)
    * 商品 →　在庫：当日出荷表示 / 直送：本日から七日後出荷表示
2. Cart In機能(SESSION)
3. 会員登録機能
4. ログイン・ログアウト(SESSION)
5. CHECK OUT(着払いでOK)


## WORK STEP
1. Admin作成 
2. Models作成 (USER, 商品, カテゴリー)とデータマイグレーション
3. TEMPLATE作成
4. URLS作成(route path)


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
1.  django_session
2.  store_category
3.  store_product


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


## ERROR LOG

* basic errors - URL route path error, models related, template error

* LogoutView class RETURN 405 Method Not Allowed -> POSTで解決
https://docs.djangoproject.com/en/5.0/releases/4.1/#log-out-via-get
https://qiita.com/guabanapple/items/c8062a138acbbb5896de

* Login Form passing error-> The default LoginView class in Django inherits from AuthenticationForm and accepts username and password as default fields.
This version makes it clear that LoginView inherits from AuthenticationForm and specifies that it accepts username and password fields by default.
```
class LoginView(RedirectURLMixin, FormView):

    form_class = AuthenticationForm
    authentication_form = None
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    extra_context = None
```
```
class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(label=_("Username"), max_length=30)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

```


## CSS
    <!--FONT-->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap">
    <!-- Bootstrap-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <!--ICON-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">