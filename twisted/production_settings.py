from .settings import *

# Overide dev variables
DEBUG=False

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '.amazonaws.com']
# Chaneg this setting to allow your host only!!! This is after you've registered a domain name

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default=None)
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default=None)
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default=None)

AWS_S3_FILE_OVERWRITE = True
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'%AWS_STORAGE_BUCKET_NAME

AWS_QUERYSTRING_AUTH = False

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

# Overide normal django static files settings

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = "https://%s/%s/"%(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://%s/%s/"%(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
