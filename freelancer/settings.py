"""
Django settings for freelancer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&i*r*^o@v3cy9_k8h$59!mxzh8yk&zo&!&br*am!bsy6p_3@w0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
    os.path.join(BASE_DIR,'main','templates','main'),
    os.path.join(BASE_DIR,'home','templates','home'),
)

ALLOWED_HOSTS = ['jumushbar.kg','www.jumushbar.kg','jumushbar.tk','www.jumushbar.tk','91.213.233.202']
#DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'main',
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'freelancer.urls'

WSGI_APPLICATION = 'freelancer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3new'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static-root/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

STATIC_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR,'static-root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
