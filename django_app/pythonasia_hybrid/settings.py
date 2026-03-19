
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables explicitly from django_app/.env
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'django-insecure-change-me-for-production'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'recommendation', # Our app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pythonasia_hybrid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'pythonasia_hybrid.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_backend',
        'NAME': os.getenv("DB_NAME", 'pythonasia2026_workshop'),
        'COLLECTION_NAME': os.getenv("COLLECTION_NAME", 'recommendation_movies'),
        'HOST': os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27017/"),
    }
}

# MongoDB Config (kept for other usages if needed)
# MONGODB_URI is loaded from env above
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY", "your_api_key_here")

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django_mongodb_backend.fields.ObjectIdAutoField'
