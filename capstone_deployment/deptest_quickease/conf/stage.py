from .common import *
import os

from dotenv import load_dotenv
load_dotenv()

DEBUG = int(os.environ.get("DEBUG"))
PRODUCTION = int(os.environ.get("PRODUCTION"))
SECRET_KEY = os.environ.get("SECRET_KEY")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}