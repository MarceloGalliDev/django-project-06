"""file of config the base configuration"""

from pathlib import Path
import environ  # type: ignore
from datetime import timedelta

env = environ.Env()


ROOT_DIR = Path(__file__).resolve().parent.parent.parent


ROOT_APP = ROOT_DIR / "core_apps"


DEBUG = env.bool("DJANGO_DEBUG", False)


ALLOWED_HOSTS: list[str] = []


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]


THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'corsheaders',
    'taggit',
    'phonenumber_field',
    'drf_yasg',
    'django_countries',
    'djcelery_email',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
]


LOCAL_APPS: list[str] = [
    'core_apps.profiles',
    'core_apps.common',
    'core_apps.users',
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


ROOT_URLCONF = 'authors_api.urls'


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


WSGI_APPLICATION = 'authors_api.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }


# para usar no docker
DATABASES = {"default": env.db("DATABASE_URL")}


PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# opção devido a inclusáo do contrib.site
SITE_ID = 1


ADMIN_URL = "supersecret/"


STATIC_URL = '/staticfiles/'
STATIC_ROOT = str(ROOT_DIR / "staticfiles")


MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = str(ROOT_DIR / "mediafiles")


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_URLS_REGEX = r"ˆapi/.*$"

AUTH_USER_MODEL = "users.User"

CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BROKER")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_TASK_SEND_SENT_EVENT = True

if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ]
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": env("SIGNING_KEY"),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "authors_access_token",
    "JWT_AUTH_REFRESH_COOKIE": "authors_refresh_token",
    "REGISTER_SERIALIZER": "core_apps.users.serializers.CustomRegisterSerializer",
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  # pylint: disable=C0301
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    },
}
