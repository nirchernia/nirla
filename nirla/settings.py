"""
Django settings for nirla project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's8*kn18711*h&42$o81h3evvj2f#yhegrpm)u8scor#oj3%52)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['nirla.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nirla.apps.blog',
    'nirla.apps.suggest',
    'dj_database_url',
    'south',
    'nirla.userprofile',
    'django_extensions',
    #'django.contrib.sites',
    #'inviter',
    'nirla.apps.invites',
)





MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	#install the middleware for invites
	#'nirla.apps.invites.middleware.InviteMiddleware',
)

ROOT_URLCONF = 'nirla.urls'

WSGI_APPLICATION = 'nirla.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "dddsam8hd2005h",
#         "USER": "xjtvgzeeccqmzs",
#         "PASSWORD": "X84fwIkffPm8aG7VV4OeR8R6bg",
#         "HOST": "ec2-23-23-81-171.compute-1.amazonaws.com",
#         "PORT": "5432",
#     }
# }



import dj_database_url
#type heroku config to get the link that default should be
DATABASES = {'default': dj_database_url.config(default='postgres://xjtvgzeeccqmzs:X84fwIkffPm8aG7VV4OeR8R6bg@ec2-23-23-81-171.compute-1.amazonaws.com:5432/dddsam8hd2005h')}







# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



STATIC_URL = '/static/'

# only refers to the location where your static files should end up after running manage.py collectstatic. you shouldn't really need collectstatic) when developing locally
STATIC_ROOT = 'staticfiles'


STATICFILES_DIRS = (	
    os.path.join(BASE_DIR, '../static'),
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, '../templates'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

#this path tells @login_required decorator where to redirect if condition isn't met
#it accepts reverse URLS
LOGIN_URL = 'login_page'
