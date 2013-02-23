import warnings
warnings.simplefilter("ignore", DeprecationWarning)

# Django settings for simpleshop project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
    # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'wblog.db',  # Or path to database file if using sqlite3.
		'USER': '',  # Not used with sqlite3.
		'PASSWORD': '',  # Not used with sqlite3.
		'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',  # Set to empty string for default. Not used with sqlite3.
	}
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
	('en', 'English'),
)

LOCALE_PRICE_SEPARATOR = {
	'en': '.'
}

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

import os
import sys

PRJ_ROOT = os.path.dirname(__file__)

sys.path.append(PRJ_ROOT)
sys.path.append(PRJ_ROOT + '/apps/')
sys.path.append(PRJ_ROOT + '/external/')

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PRJ_ROOT + '/media/'
# DATA_ROOT = PRJ_ROOT + '/data/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

MEDIA_PREFIX = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '1t6lmv#%b00xnskdhfs^T*UGl!%ac5h7gkwfo1^)fs'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.transaction.TransactionMiddleware',
    'apps.blog.middleware.BlogMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

AUTH_PROFILE_MODULE = 'users.UserProfile'

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	'django.core.context_processors.request',
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.contrib.messages.context_processors.messages",
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


CURRENCY_EXCHANGE_XML = 'http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

TEMPLATE_DIRS = (
    PRJ_ROOT + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.sessions',
	'django.contrib.auth',
    'django.contrib.staticfiles',
	'blog',
	'south',
    'debug_toolbar',
)


SESSION_COOKIE_AGE = 31 * 24 * 60 * 60 * 60  # A month of cookie life

SESSION_COOKIE_WILDCARD_DOMAINS = []

TRANSLATION_REGISTRY = "translation"

STATIC_DOC_ROOT = PRJ_ROOT + '/media/'
TEMP_DIR = STATIC_DOC_ROOT + '/temp'

STATIC_URL = PRJ_ROOT + '/media/'


FILE_CHARSET = 'utf-8'

WEB_ROOT = ''

ADMIN_URL_PREFIX = '/admin/'

UPLOAD_DIR = 'uploaded/'
DEFAULT_MESSAGES_COUNT = 10

# AUTH_PROFILE_MODULE = 'users.UserProfile'

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

INTERNAL_IPS = ('127.0.0.1')


from settings_local import *
