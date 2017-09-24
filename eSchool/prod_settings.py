import dj_database_url
from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['cemmah.herokuapp.com']


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = 'utlplp@sc2yh36c&9t!!4d4ody&b2@b(3qf&8y692*4va79dz4'

DATABASES['default'] = dj_database_url.config()
