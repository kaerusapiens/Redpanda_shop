from pathlib import Path
import yaml #追記



BASE_DIR = Path(__file__).resolve().parent.parent #追記
def read_yaml_config(file_path): #追記
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
#本番環境
# config = read_yaml_config(BASE_DIR / 'secrets/prod.yml')

#開発環境
config = read_yaml_config(BASE_DIR / 'secrets/dev.yml')

SECRET_KEY = config.get('SECRET_KEY')
DEBUG = config.get('DEBUG')
ALLOWED_HOSTS = config.get('ALLOWED_HOSTS')


#追記
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        }},
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django_debug.log',
            'formatter': 'verbose',
            'mode': 'w',  # 'w' to overwrite the file
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'project': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', #追記
    'debug_toolbar', #追記
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', #追記
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 "app.views.category_list" #追加。全てのページでこのデータベースが接続できるようになる
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'  #追記URL absolute / URL relative
STATICFILES_DIRS=[BASE_DIR/ 'static']  #追記add for image static file DIR
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = '/media/'  #追記add for image static file DIR
MEDIA_ROOT = BASE_DIR / 'media'  #追記add for image static file DIR



INTERNAL_IPS = ['127.0.0.1',] #追記


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#カスタマイズUser model
AUTH_USER_MODEL = 'app.User' #追記

LOGIN_URL = "/login/" #追記ログインページ   
LOGIN_REDIRECT_URL = "/"
LOGOUT_URL = "/logout/" #追記ログアウト
LOGOUT_REDIRECT_URL = "/"