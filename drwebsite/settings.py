

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-asc=zfl)y0xveh57ocuh0-=^xot#dx)a2rg5ri-rmd$_$=8rur'



ALLOWED_HOSTS = ['web-production-c7bea.up.railway.app',
    '127.0.0.1',
    'localhost','sabrconsult.com', 'www.sabrconsult.com']
CSRF_TRUSTED_ORIGINS = ['https://sabrconsult.com', 'https://www.sabrconsult.com',"https://web-production-c7bea.up.railway.app"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drapp',
    'jobs',
    'accounts',


]
AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'drapp.middleware.VisitorMiddleware',
    
]
USER_AGENTS_CACHE = 'default'

# مسار ملف GeoIP2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')
GEOIP_CITY = 'GeoLite2-City.mmdb'

ROOT_URLCONF = 'drwebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drwebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:hEzsUvAdaopyMpizgBrBPTzodTZWknCx@gondola.proxy.rlwy.net:21914/railway',
        conn_max_age=600,
        engine='django.db.backends.postgresql_psycopg2' 

    )
}
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB




# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'  # URL لخدمة الملفات
MEDIA_ROOT = '/data/media'  # المسار المحلي لتخزين الملفات

# إذا كنت تستخدم Railway للرفع
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # لـ AWS S3

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#ارسال الاستمارة للايميل
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or whatever your SMTP server is
EMAIL_PORT = 587  # Usually 587 for TLS
EMAIL_USE_TLS = True  # Make sure TLS is enabled
EMAIL_HOST_USER = 'M.abuzaifah@gmail.com'  # Your email
EMAIL_HOST_PASSWORD = 'zuoc zlqs nyqm awhe'
  # Use an app password if you have 2FA enabled
DEFAULT_FROM_EMAIL =  'M.abuzaifah@gmail.com' 

# إعدادات التخزين المؤقت
CACHE_TTL = 60 * 15  # 15 دقيقة
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_folder'),

    }
}


DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# إعدادات الأمان عند تفعيل HTTPS
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# مهم جداً مع Railway ونطاق مخصص
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


