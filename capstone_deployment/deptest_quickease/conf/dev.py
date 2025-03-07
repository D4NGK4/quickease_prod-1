from .common import *
import os

from dotenv import load_dotenv
load_dotenv()

DEBUG = int(os.environ.get("DEBUG"))
PRODUCTION = int(os.environ.get("PRODUCTION"))
SECRET_KEY = os.environ.get("SECRET_KEY")

INTERNAL_IPS = os.environ.get("DJANGO_INTERNAL_IPS").split(" ")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}