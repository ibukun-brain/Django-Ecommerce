import dj_database_url
from .base_settings import *
from buyit.settings.local.mailhog_settings import *

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

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES["default"] = dj_database_url.parse(
    f"sqlite:////{BASE_DIR.joinpath(BASE_DIR.name)}.db", conn_max_age=600,
)

PAYPAL_CLIENT_ID = 'Ad3uDKXmiTHvvcVUM6C-zHANQU-tbNV51E9-3cLAHP509H-Id3gwEAUzpQlZPFzu5Pw2S-5GsgTPSFtj'
PAYPAL_SECRET_KEY = 'ENpRwCZ19E7zOHR_S7vzFFruds4i0GEXHConGyO1qMJtC1L0wUHjBA-O21nC7RbXp2gOLzmeh82zyH6v'
