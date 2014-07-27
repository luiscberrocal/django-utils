__author__ = 'luiscberrocal'
from os.path import abspath, basename, dirname, join, normpath
from sys import path
########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)
ADD_DATE_TO_TEMPORARY_DIR = True
# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)

TEMPORARY_DIR = join(DJANGO_ROOT, 'temporary')

TEMPLATES = {
    'allauth': {
        'HTML_TEMPLATE_DIR': [
            normpath(join(DJANGO_ROOT, 'templates/allauth/html/account')),
            normpath(join(DJANGO_ROOT, 'templates/allauth/html/registration')),
            ]
    }
}
########## END PATH CONFIGURATION
