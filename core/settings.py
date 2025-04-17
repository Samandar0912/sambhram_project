from django.utils.translation import gettext_lazy as _
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-2*)vfpz0bkomk$co@%ysvr6#f0@#r74di)n_0r&_t0rwi3ge4m'  # Move to env variable in production
DEBUG = True
ALLOWED_HOSTS = []  # Add specific hosts in production, e.g., ['example.com']

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'api',  # Remove if not used
    'rosetta',  # For translation management
]

# Jazzmin admin customization
JAZZMIN_SETTINGS = {
    'site_title': 'Mening Admin Panelim',
    'site_header': 'Mening Saytim',
    'welcome_sign': 'Xush kelibsiz, admin!',
    'copyright': 'Mening Kompaniyam',
    'search_model': ['auth.User', 'myapp.NewsArticle'],
    'show_sidebar': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Keep for static file serving in production
]

# URL configuration
ROOT_URLCONF = 'core.urls'

# Template configuration
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

# WSGI application
WSGI_APPLICATION = 'core.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'uz'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('uz', _('Uzbek')),
    ('en', _('English')),
    ('ru', _('Russian')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'