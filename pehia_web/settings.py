from dotenv import load_dotenv, find_dotenv
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'a%+4e8nq=pd%id254#drkv8=!_vy@*qovpc(3l(1pqk4x*e02q'


DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'oppurtunities',
    'events',
    'campus',
    'blog',
    'pehia_web',
    'loginauth',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pehia_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'pehia_web.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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
SOCIAL_AUTH_TRAILING_SLASH = False                   
SOCIAL_AUTH_AUTH0_DOMAIN = 'YOUR_AUTH_DOMAIN'
SOCIAL_AUTH_AUTH0_KEY = 'YOUR_CLIENT_ID'
SOCIAL_AUTH_AUTH0_SECRET = 'YOUR_CLIENT_SECRET'

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile'
]
AUTHENTICATION_BACKENDS = {
    'loginauth.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
}
LOGIN_URL = "/login/login/auth0"
LOGIN_REDIRECT_URL = "/login/dashboard"
LOGOUT_REDIRECT_URL = "/login"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "project_static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "pehia_web/static_cdn", "static_root")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "pehia_web/static_cdn", "media_root")
