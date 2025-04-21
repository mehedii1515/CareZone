
import os
import dj_database_url
import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')
DEBUG = True  # Set to False in production
# ALLOWED_HOSTS = ['carzone-x3f8.onrender.com']

LOGIN_REDIRECT_URL = 'dashboard'

UTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# SOCIALACCOUNT_PROVIDERS = {
    # 'facebook': {
        # 'SCOPE': ['email'],
        # 'METHOD': 'js_sdk',
        # 'FIELDS': ['id', 'email', 'name', 'first_name', 'last_name', 'verified', 'locale', 'timezone', 'link', 'gender', 'updated_time'],
        # 'VERSION': 'v12.0',
    # }
# }


SOCIALACCOUNT_LOGIN_ON_GET = True


# Application definition

INSTALLED_APPS = [
    'contacts.apps.ContactsConfig',
    'cars.apps.CarsConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'multiselectfield',
    'django.contrib.humanize',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    
]

ROOT_URLCONF = 'carzone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'carzone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'cardealer_db',
#         'USER': 'postgres',
#         'PASSWORD': 'mehedi',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }



DATABASES = {
    'default': dj_database_url.config(default=env("DATABASE_URL"))
}


# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
        # 'USER': '',                      # Not used with sqlite3.
        # 'PASSWORD': '',                  # Not used with sqlite3.
        # 'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        # 'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    # }
# }

# DATABASES = {'default': dj_database_url.config(default='postgres://postgres:postgres@localhost/carzone_db')}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'carzone/static'),
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'

# # Directory where 'collectstatic' will store static files in production
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Additional locations of static files (used during development)
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'carzone/static'),
# ]

# CSRF_TRUSTED_ORIGINS = ['https://carzone-x3f8.onrender.com']
# # Whitenoise for serving static files in production
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # Media files (uploaded by users)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


from django.contrib.messages import constants as message

MESSAGE_TAGS = {
    message.ERROR: 'danger',
}

SITE_ID = 1


# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")


# Whitenoise settings

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
