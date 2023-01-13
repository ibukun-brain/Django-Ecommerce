import dj_database_url
from .base_settings import *

from .base_settings import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3mw+y#8j8e4*9z2g!itddgt1$5ykqi^p@+i3-+p)mwhih3zuyv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware"
] 

DATABASES

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_URL = 'assets/'
STATICFILES_DIRS = [
    BASE_DIR / 'assets'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static_root'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES["default"] = dj_database_url.parse(
    f"sqlite:////{BASE_DIR.joinpath(BASE_DIR.name)}.db", conn_max_age=600,
)