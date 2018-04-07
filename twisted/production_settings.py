from .settings import *

# Overide dev variables
DEBUG=False

ALLOWED_HOSTS = ['*']
# Chaneg this setting to allow your host only!!! This is after you've registered a domain name

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
