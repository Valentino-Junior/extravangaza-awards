import os

import django_heroku
from pathlib import Path
from decouple import config
import dj_database_url

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l-0zj$a@a7^q^&^yixzb96!+9k2s__i=w3sb*5yx%p2-s&i!fu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'awards',
    'cloudinary',
    'bootstrap4',
    'crispy_forms',
    'star_ratings',
    'rest_framework',

    'social_django'

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

ROOT_URLCONF = 'extravaganza.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'extravaganza.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD':config('DB_PASSWORD'),
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['*']


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',

   'social_core.backends.github.GithubOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',

    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

cloudinary.config(
    cloud_name = 'deltsoe6r',
    api_key = '631573746168511',
    api_secret = 'uA38YXC4GoywEV4_6imvPbuDmoU',
)



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '397724793102-v1flfpugn8i1u57sjeht32m2rekre5q0.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GITHUB_KEY = 'd60f056fca593fe5cc41'
SOCIAL_AUTH_GITHUB_SECRET = 'bb6616ee122c3c6dad2547b2504a78cb12739baf'


SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77opr6874i264b'    #Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '35tdEPWkjlHV8wKC'  #Client Secret

SOCIAL_AUTH_FACEBOOK_KEY='303618538391463'
SOCIAL_AUTH_FACEBOOK_SECRET ='f81ca43f6800642a258ffa9151703e84'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

STAR_RATINGS_RERATE = True
STAR_RATINGS_RANGE = 10
STAR_RATINGS_RERATE_SAME_DELETE = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())

SOCIAL_AUTH_JSONFIELD_ENABLED = True