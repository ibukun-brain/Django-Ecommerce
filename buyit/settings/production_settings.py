from base_settings import *
from settings.local.email_settings import *

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',
    'cloudinary',
]
MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

MIDDLEWARE += [
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
] 

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'dftimfbeb',
#     'API_KEY': '994671578336668',
#     'API_SECRET': 'cjYYIDvpvSz8Ny4UAun-22knfGI'
# }