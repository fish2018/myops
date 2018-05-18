"""
Django settings for opsweb project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
# -*- coding: utf-8 -*-

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l_72ta9^^tqg4u_9k_6g4^^&rr!8fd4p2ex98$eq^hi&+c)d-g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'work_order',
    'books',
    'djcelery',
    'cmdb',
    'projects',
    'tasks',
    'deploy',
]

AUTH_USER_MODEL = 'dashboard.UserProfile'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'opsweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'opsweb.context_processors.global_variable',

            ],
        },
    },
]

WSGI_APPLICATION = 'opsweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'opsweb',
        'HOST': '192.168.10.122',
        # 'HOST': '192.168.0.109',
        'USER': 'user',
        'PASSWORD': '123456',
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



LOGIN_URL = "/login/"

JUMP_PAGE = "jump.html"

EMAIL_HOST = "smtp.exmail.qq.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "sa-notice@yuanxin-inc.com"
EMAIL_HOST_PASSWORD = "Miao13456"
EMAIL_USE_SSL = True
EMAIL_FROM = "sa-notice@yuanxin-inc.com"


LOGGING = {
    "version": 1,
    'disable_existing_loggers': False,

    "loggers":{

        "opsweb": {
            "level": "DEBUG",
            "handlers": ["opsweb_file_handle"],
            'propagate': True,
        },

        "django":{
            "level": "DEBUG",
            "handlers": [ "django_handle"],
            'propagate': True,
        },

        "report":{
            "level": "ERROR",
            "handlers": [ "mail"],
            'propagate': True,
        }
    },


    "handlers": {

        "opsweb_file_handle": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "opsweb.log"),
            "formatter": "opsweb"
        },

        "django_handle": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "django.log"),
            "formatter": "opsweb"
        },

        'django_request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs", 'request.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'opsweb',
        },

        "mail":{
            "class": "logging.handlers.SMTPHandler",
            "level": "ERROR",
            "formatter": "simple",
            "mailhost":("smtp.139.com", 25),
            "fromaddr":"13260071987@139.com",
            "toaddrs":["787696331@qq.com"],
            "subject" : "devops mail",
            "credentials" :("13260071987@139.com","yi15093547036")
        }
    },

    'formatters': {
        'opsweb':{
            'format': '[%(asctime)s] [%(process)d] [%(thread)d] [%(filename)16s:%(lineno)4d] [%(levelname)-6s] %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        }
    },

}


import djcelery
djcelery.setup_loader()        

BROKER_URL = 'redis://127.0.0.1:6379/0'    
BROKER_TRANSPORT = 'redis'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'     

CELERYD_LOG_FILE = BASE_DIR + "/logs/celery/celery.log"         
CELERYBEAT_LOG_FILE = BASE_DIR + "/logs/celery/beat.log"     


GITLAB_HTTP_URI = "http://211.152.57.213/"
GITLAB_TOKEN = "xAhXAq4LGs7x61DSBjxx"


Jenkins_HTTP_URI = "http://192.168.25.12:8080/"
Jenkins_User = "xiazy"
Jenkins_User_API_Token = "18edb8794c4c0389b0b91e29bed08ba9"