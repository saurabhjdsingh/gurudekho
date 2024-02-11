import os
from pathlib import Path
from decouple import config
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = DEBUG = config('DEBUG', default=True, cast=bool)

if DEBUG:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASS'),
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
    ]

    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config("EMAIL_HOST")
    DEFAULT_FROM_EMAIL = config("EMAIL_USER")
    EMAIL_HOST_USER = config("EMAIL_USERNAME")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
