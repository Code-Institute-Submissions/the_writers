from base import *
import dj_database_url

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


# Stripe environment test variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_mNb1dKaAFoLSHyj2BAcDMl99')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_blRbu4P14RH0LjZMT2jDpwxy')


SITE_URL = 'https://thewriters.herokuapp.com'
ALLOWED_HOSTS.append('thewriters.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}