import dj_database_url
from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['cemmah.herokuapp.com']


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = 'utlplp@sc2yh36c&9t!!4d4ody&b2@b(3qf&8y692*4va79dz4'

DATABASES['default'] = dj_database_url.config()
## EMAIL_HOST = 'cemmah.herokuapp.com'
## EMAIL_PORT = 1025


AWS_ACCESS_KEY_ID = 'AKIAIWVTFL4ITDRCUWSA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'cemmah-assets'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'eSchool.storage_backends.MediaStorage'