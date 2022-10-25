"""
Django settings for Hindustan_blogs project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

import django_heroku

from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#the TEMPLATE_DIRS is necessary so that django knows where your templates are stored for this PROJECT_ROOT
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--!zvql3tb)gyhsoj7c#n9t*luv0kq8n$n9e9$=(n62-_b8#ip('

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
    'froala_editor',
    'blogapplication.apps.BlogapplicationConfig',
    'authentication.apps.AuthenticationConfig',

    #django website api section
    #django cleanup will delete any static files images when the model is deleted
    'django_cleanup.apps.CleanupConfig',
    #add 'rest_framework', for our django rest api
    'rest_framework',
    #add boto3 and django-storages here so that we can use amazon s3 bucket
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #whitenoise for serving our static files in production environment
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Hindustan_blogs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'Hindustan_blogs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

#configure MEDIA_URL so that we can connect and display the uploaded image that is present in the static/images folder to our front end from the static folder via models.py file since our images url are gonna be dynamic
MEDIA_URL = '/images/'

#now add the static urls here for this website
#static is like graphics icons and all that stuff for your website including your flex boxes
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

#STATIC_ROOT defines where our static files in production are gonna be when I say production that means we will be setting debugging= False
#collect static is a command that we will use to run STATIC_ROOT
#collect static is a command that will tell django to take all the files in the static folder and its gonna bundle them up in one file and django can take care of that from there
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#configuring the path where the images should be stored when a user uploads his/her images into the website
#by default the images uploaded by the user will be stored in the root directory of the project
#but we want django to store our images uploaded by the users into this path (static/images/)
#MEDIA_ROOT simply tells django where to store user uploaded content
MEDIA_ROOT = os.path.join(BASE_DIR,'static/images') #-> current path of all the images that are being sent inyto this directory

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#this line of code will host our website on heroku
django_heroku.settings(locals())

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'email'
# EMAIL_HOST_PASSWORD = 'password'

# #------AMAZON S3 BUCKET RELATED SETTINGS--------------------
# #this will handle our amazon s3 bucket that will host our static files and user uploaded files on our website
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# #setup your access key of your AWS (Amazon web services)
# AWS_ACCESS_KEY_ID = 'AKIAXJD4CDE464QQSZ6L'
# AWS_SECRET_ACCESS_KEY = 'eWvePxmLSkLj84oUqx/os7Zx6hKvep0wRdJjIzaM'
#
# #now assign your s3 bucket to this django project
# AWS_STORAGE_BUCKET_NAME = "blog-application-aryan68125"
#
# #add this so that you can access your uploaded images from amazon s3 bucket
# AWS_S3_REGION_NAME = "ap-south-1"
#
# AWS_S3_SIGNATURE_VERSION = "s3v4"
#
# #this will make sure that the images having same name when uploaded to the s3 bucket have a unique name and do not overwrite each other
# #so basically if there are two users uploading an image having same names then it will not cause any conflict and prevent one user from overwriting othe user's uploaded image in the S3 bucket
# AWS_S3_FILE_OVERWRITE = False
