from .common import *
import os

from dotenv import load_dotenv
load_dotenv()

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEBUG = int(os.environ.get("PRODUCTION"))
SECRET_KEY = os.environ.get("SECRET_KEY")

CORS_ALLOW_ALL_ORIGINS = True

#CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS").split(" ")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

REST_AUTH_TOKEN_MODEL = None


#CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': os.environ.get("DB_NAME"),
#        'USER': os.environ.get("DB_USER"),
#        'PASSWORD': os.environ.get("DB_PASSWORD"),
#        'HOST': os.environ.get("DB_HOST"),
#        'PORT': os.environ.get("DB_PORT"),
#        'OPTIONS':{
#            'passfile': os.environ.get("DB_PASSFILE"),
#            },
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': ''
    }
}
