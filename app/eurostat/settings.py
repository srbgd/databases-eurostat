"""
Django settings for minimal_django project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mysecretkey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'eurostat',
]

ROOT_URLCONF = 'eurostat.urls'

DATABASES = {}

TIME_ZONE = 'UTC'

USE_TZ = True

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        'rest_framework.renderers.JSONRenderer',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "UNAUTHENTICATED_USER": None,
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': \
        'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter'
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
    ],
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
    },
]