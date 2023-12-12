import os
from datetime import timedelta

import environ


root = environ.Path(__file__) - 2
env = environ.Env()
environ.Env.read_env(env.str(root(), '.env'))

BASE_DIR = root()

SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', False)
ALLOWED_HOSTS = env.str('ALLOWED_HOSTS', '').split(' ')

# Base packages
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Additional packages
INSTALLED_APPS += [
    'rest_framework',
    'django_filters',
    'corsheaders',
    'djoser',
    'phonenumber_field',
    'mptt',
    'django_mptt_admin',
    'debug_toolbar',
]

# Apps
INSTALLED_APPS += [
    'api',
    'common',
    'users',
    'storage',
]

# After apps
INSTALLED_APPS += [
    'drf_spectacular',
]

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = ('users.backends.AuthBackend', )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'crum.CurrentRequestUserMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('PG_DATABASE', 'postgres'),
        'USER': env.str('PG_USER', 'postgres'),
        'PASSWORD': env.str('PG_PASSWORD', 'postgres'),
        'HOST': env.str('PG_HOST', 'localhost'),
        'PORT': env.int('PG_PORT', 5432),
    },
    'extra': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

################################
# DJANGO REST FRAMEWORK
################################
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],

    'DEFAULT_PARSES_CLASSES': [
        'rest_framework.parses.JSONParses',
        'rest_framework.parses.FormParser',
        'rest_framework.parses.MultiPartParser',
        'rest_framework.parses.FileUploadParser',
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.BasePagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

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

################################
# LOCALIZATION
################################
LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

################################
# CORS-HEADERS
################################
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CSRF_COOKIE_SECURE = False

################################
# STATIC & MEDIA
################################
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

################################
# DRF SPECTACULAR SETTINGS
################################
SPECTACULAR_SETTINGS = {
    'TITLE': 'API-сервис файлового хранилища данных',
    'DESCRIPTION': 'Полное описание REST API доступа к сервису',
    'VERSION': '1.0.0',

    'SERVE_PERMISSIONS': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'SERVE_AUTHENTICATION': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],

    'SWAGGER_UI_SETTINGS': {
        'DeepLinking': True,
        'DisplayOperationId': True,
        'filter': True,
    },

    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,

    'TITLES_TAGS': {
        'STORAGE': 'Хранилище',
        'AUTH': 'Аутентификация и авторизация',
        'PROFILE': 'Пользователь'
    },
}

#######################
# DJOSER
#######################
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {},
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
}
