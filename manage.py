__author__ = 'luiscberrocal'

import argparse
import time
from settings.local import *
import pprint
from os import mkdir

def copy_templates(temporary_target):
    mkdir(temporary_target)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('django_project_folder')
    args = parser.parse_args()
    print('*' * 20 + ' ARGUMENTS ' + '*' * 20 )
    print('django_project_folder: %s' % args.django_project_folder)
    temporary_project_folder = '%s_%s' % (time.strftime("%Y%m%d_%H%M%S"), basename(args.django_project_folder))
    temporary_target = join(TEMPORARY_DIR, temporary_project_folder)
    print('temporary_target: %s' % temporary_target)
    print('*' * 20 + ' SETTINGS ' + '*' * 20 )
    print('DJANGO_ROOT: %s' % DJANGO_ROOT)
    print('SITE_ROOT: %s' % SITE_ROOT)
    print('SITE_NAME: %s' % SITE_NAME)
    print('ADD_DATE_TO_TEMPORARY_DIR: %s' % ADD_DATE_TO_TEMPORARY_DIR)
    print('TEMPORARY_DIR: %s' % TEMPORARY_DIR)
    pprint.pprint(TEMPLATES)

    copy_templates(temporary_target)

