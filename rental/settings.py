import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-54!j4d(ujrf@be=2sy!6)p&s!^17yl)8f9#qdj7vx&#n!cd3d)'
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.app.github.dev',
    'rental-1-yhkm.onrender.com',
    'rental-production-321f.up.railway.app',
    'rental-production-2aa8.up.railway.app',
    'rental-2-sjrr.onrender.com',
    '.onrender.com',
    '.railway.app',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',

    # Social auth
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'rental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'rental.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',  # Google OAuth2
    'django.contrib.auth.backends.ModelBackend',  # Default
)

# social-auth-app-django Google OAuth2 config
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '458183466107-3als8l6an9m20lgfbh39rtv714nns571.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False  # For local development

# Login/Logout URLs
LOGIN_URL = 'signin'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'signin'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nanaware406@gmail.com'
EMAIL_HOST_PASSWORD = 'cctr xdkx aqtn iknh'  # Keep secret
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Razorpay API
RAZORPAY_API_KEY = 'rzp_test_wH0ggQnd7iT3bB'
RAZORPAY_API_SECRET = 'eZseshY3oSsz2fcHZkTiSlCm'

# CSRF & Session
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_SECURE = False
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
