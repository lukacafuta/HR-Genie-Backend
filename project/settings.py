"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import ast
import os
from datetime import timedelta
from pathlib import Path

import dj_database_url



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DJANGO_DEBUG = ast.literal_eval(os.environ.get("DJANGO_DEBUG", True))

ALLOWED_HOSTS = ['hr-genie-backend-24b07ef76680.herokuapp.com', 'localhost']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # frameworks
    "rest_framework",
    "drf_yasg",

    # apps
    "companiesProfile",
    "customUser",       # need to specify also AUTH_USER_MODEL
    "userProfile",
    "department",
    "absenceRequests",
    "trainingRequests",
    "publicHoliday",
    "timeDependentVar"
]

# needed for custom user model
AUTH_USER_MODEL = "customUser.CustomUser"   # name of the App. name of the model

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # added whitenoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
SERVER_TYPE = os.environ.get('SERVER_TYPE', 'development')

if SERVER_TYPE == 'development':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get('POSTGRES_DB'),
            "PORT": os.environ.get('POSTGRES_PORT'),
            "HOST": os.environ.get('POSTGRES_HOST'),
            "USER": os.environ.get('POSTGRES_USER'),
            "PASSWORD": os.environ.get('POSTGRES_PASSWORD'),
        }
    }

if SERVER_TYPE == 'production':
    DATABASES = {
        'default': dj_database_url.config()
    }

# print(os.environ.get('POSTGRES_DB'))
# print(os.environ.get('POSTGRES_PORT'))
# print(os.environ.get('POSTGRES_HOST'))
# print(os.environ.get('POSTGRES_USER'))
# print(os.environ.get('POSTGRES_PASSWORD'))


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files
SPACES = os.getenv('SERVER_TYPE') == 'production'

if SPACES:
    # production settings here
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # AWS SDK
    AWS_ACCESS_KEY_ID = os.environ.get('DO_SPACES_ACCESS_KEY')  # Spaces access key
    AWS_SECRET_ACCESS_KEY = os.environ.get('DO_SPACES_SECRET')  # Spaces access secret
    AWS_STORAGE_BUCKET_NAME = os.environ.get('DO_SPACES_SPACE_NAME')  # Name of the space
    AWS_S3_ENDPOINT_URL = os.environ.get('DO_SPACES_ENDPOINT')  # Endpoint found under Spaces/<your-space>/Settings
    MEDIA_URL = 'https://hr-genie-spaces.fra1.digitaloceanspaces.com/media/'  # Full url displayed in Spaces
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# +++ START JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),    # a bit lower lifetime operative
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10)
}
# .... END JWT


# +++ SWAGGER
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,  # Change settings to True to enable Django Login option
    'LOGIN_URL': 'admin/',  # URL For Django Login
    'LOGOUT_URL': 'admin/logout/',  # URL For Django Logout
    'SECURITY_DEFINITIONS': { # Allows usage of Access token to make requests on the docs.
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
# ... SWAGGER


# +++ EMAIL
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.environ.get('EMAIL_PORT')
# ... EMAIL

