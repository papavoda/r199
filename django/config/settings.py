import os
from pathlib import Path
from environs import Env

env = Env()
env.read_env()

SITE_ID = 1

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

#HSTS settings
#SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False)
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD', default=False)
#HTTPS settings
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # additional libs:
    # 'pytils',  # for custom slugify
    'rest_framework',
    'django.contrib.humanize',
    'autoslug',
    'mptt',
    # https://proghunter.ru/articles/django-base-2023-adding-ckeditor-5-to-django-41
    'django_ckeditor_5',
    'debug_toolbar',
    # 'snowpenguin.django.recaptcha3',
    'django_recaptcha',
    "phonenumber_field",
    'phonenumbers',
    'corsheaders',
    # my apps
    'blog.apps.BlogConfig',
    'contact',
    'price',
    'calc',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # add CorsMiddleware above CommonMiddleWare in MIDDLEWARE
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # for debug-toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',

    # "django.contrib.staticfiles",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': env.dj_db_url("DATABASE_URL")
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
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")  # need for collectstatic

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # work in localserver

if DEBUG:
    MEDIA_URL = 'media/'
else:
    MEDIA_URL = 'https://remont199.com/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# for debug-toolbar
# for debug toolbar in docker
# https://ranjanmp.medium.com/
# django-debug-toolbar-not-showing-up-when-using-docker-django-docker-e79585813bc6
if DEBUG:
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1']

LOGIN_REDIRECT_URL = '/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # for develop
        # "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        'LOCATION': os.path.join(BASE_DIR, 'cache'),

    }

}
# https://github.com/django-recaptcha/django-recaptcha?tab=readme-ov-file
# RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000', }
RECAPTCHA_PUBLIC_KEY = env.str('RECAPTCHA_PUBLIC_KEY', default='')
RECAPTCHA_PRIVATE_KEY = env.str('RECAPTCHA_PRIVATE_KEY', default='')
RECAPTCHA_DISABLE = env.bool('RECAPTCHA_DISABLE', default=False)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.str('DJANGO_EMAIL_HOST', default='smtp.gmail.com')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_HOST_USER = env.str('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_TO = env.str('DJANGO_EMAIL_TO')
PHONENUMBER_DEFAULT_REGION = env.str('DJANGO_PHONENUMBER_DEFAULT_REGION')


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ]
}
# CORS_ALLOW_ALL_ORIGINS = False

# # https://pypi.org/project/django-cors-headers/
# for vue.js
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")

#
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')


customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]

# CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
# CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage" # optional
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

IMAGE_PROCESSING = {
    'MAX_WIDTH': 1280,
    'WATERMARK_PATH': os.path.join(BASE_DIR, 'static/watermark_new.webp'),
    'WATERMARK_OPACITY': 0.2,  # 0.0-1.0
    'WATERMARK_POSITION': 'SouthEast',  # or 'Center'
    'WATERMARK_OFFSET': (130, 90),  # X,Y padding
}

