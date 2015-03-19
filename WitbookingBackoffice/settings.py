"""
Django settings for WitbookingBackoffice project.

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
SECRET_KEY = 's4ejhf!g$ttt2u(l5-_fdov*+@6*=3_=$@fs+p*u#1yn3fsfsl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'bootstrap3',
    'accounting',
    'establishmentDataManagement',
    'witbooking_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'djrill'
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'establishmentDataManagement.router.MultipleDbMiddleware',
)

AUTHENTICATION_BACKENDS = (
    #'django.contrib.auth.backends.ModelBackend',
    'establishmentDataManagement.authorization.MultipleDBAuthorization',
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_USER_MODEL = "witbooking_auth.WitbookingUser"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
SOCIALACCOUNT_EMAIL_REQUIRED = False

ROOT_URLCONF = 'WitbookingBackoffice.urls'

WSGI_APPLICATION = 'WitbookingBackoffice.wsgi.application'

MANDRILL_API_KEY = "-pzMDIrAVBi4J-tHcEud_A"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = 'info@witbooking.com'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'witbooking_auth',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    },
    'hoteldemo.com.v6': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bk_demowitbcn6',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    },
    'hotelpraktikmetropol.com': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bkpraktikmetropol',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    }
}

DATABASE_ROUTERS = ['establishmentDataManagement.router.MultiDBRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOGIN_REDIRECT_URL = '/admin'
LOGIN_URL = "/accounts/login/"

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount"
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'templates', 'allauth'),
    os.path.join(BASE_DIR, 'templates', 'admin')
)

GRAPPELLI_ADMIN_TITLE = 'Admin Witbooking'
GRAPPELLI_INDEX_DASHBOARD = {
      'django.contrib.admin.site': 'establishmentDataManagement.dashboard.CustomIndexDashboard',
      'establishmentDataManagement.admin.admin_site': 'establishmentDataManagement.dashboard.CustomIndexDashboard'
}
