"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1!gbckk=*wngr+uzvcq@mi*w67r#aekwzf4ypeu_2h%861cmyk"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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
# AUTH_USER_MODEL = "customUser.CustomUser"   # name of the App. name of the model

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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

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

