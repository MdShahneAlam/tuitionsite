import os
from pathlib import Path
import pymysql
import dj_database_url

pymysql.install_as_MySQLdb()
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Load environment variables

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key (from .env file)
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')

# Debug Mode
DEBUG = True


# Allowed Hosts
ALLOWED_HOSTS = [
    "excelhometuitionsite.com",
    "www.excelhometuitionsite.com",
    "localhost",
    "127.0.0.1",
    ".railway.app",  # Allow Railway deployment
]


# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this early
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bussiness',
        'USER': 'root',
        'PASSWORD': 'root@123',  # Change '@' to '%40'
        'HOST': 'localhost',
        'PORT': '3306',  # Default MySQL port
    }
}



# Static Files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# URL Configuration
ROOT_URLCONF = 'mypro.urls'

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = True
