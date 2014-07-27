__author__ = 'luiscberrocal'

import argparse
from settings.local import *
import pprint
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('django_project_folder')
    args = parser.parse_args()
    print('*' * 20 + ' ARGUMENTS ' + '*' * 20 )
    print('django_project_folder: %s' % args.django_project_folder)
    temporary_target = join(TEMPORARY_DIR, basename(args.django_project_folder))
    print('temporary_target: %s' % temporary_target)
    print('*' * 20 + ' SETTINGS ' + '*' * 20 )
    print('DJANGO_ROOT: %s' % DJANGO_ROOT)
    print('SITE_ROOT: %s' % SITE_ROOT)
    print('SITE_NAME: %s' % SITE_NAME)
    print('TEMPORARY_DIR: %s' % TEMPORARY_DIR)
    pprint.pprint(TEMPLATES)

