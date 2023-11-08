import os
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", True)
REAL_DB = os.environ.get("REAL_DB", False)
PRODUCTION = os.environ.get("PRODUCTION", False)


ALLOWED_HOSTS = ["blackkaiwhite.herokuapp.com", ] if PRODUCTION else ['*']


if PRODUCTION:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'frontend',
    'catalogue',
    'site_settings',
    'accounts',
    'cart',
    'dashboard',
    'point_of_sale',
    'voucher',
    'newsletter',
    'contact',
    'subscribe',
    'blog',

    'django_tables2',
    # 'social_django',
    'tinymce',

    'import_export',
    'mptt',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'black_and_white.urls'

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
                'frontend.context_processors.frontend_site_data',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'black_and_white.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if REAL_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('HOST'),
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db_.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


if REAL_DB:
    AWS_REGION = 'eu-central-1'
    S3_USE_SIGV4 = True
    AWS_S3_HOST = "s3.eu-central-1.amazonaws"
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://s3.%s.amazonaws.com/%s/media/' % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    # from storages.backends.s3boto import S3BotoStorage
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


CURRENCY = '€'
WAREHOUSE_ORDERS_TRANSCATIONS = False
RETAIL_TRANSCATIONS = False
MANUAL_RETAIL_TRANSCATIONS = False
PRODUCT_ATTRIBUTE_TRANSCATIONS = True
USE_QTY_LIMIT = False
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

AUTHENTICATION_BACKENDS = [
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    # 'social_core.backends.instagram.InstagramOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'user_profile'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'


#SOCIAL_AUTH_URL_NAMESPACE = 'social'
#SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')    # App ID
#SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')  # App Secret
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', ]  # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {  # add this
    'fields': 'email'
}


# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
#SENDGRID_API_KEY = config('SENDGRID_API_KEY')
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_ECHO_TO_STDOUT = True
SITE_EMAIL = 'lirageika@hotmail.gr'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"