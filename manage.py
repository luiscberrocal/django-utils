__author__ = 'luiscberrocal'

import argparse
import time
from settings.local import *
import pprint
from os import mkdir
from shutil import copytree

def copy_templates(temporary_target, app_name):
    mkdir(temporary_target)
    for template_dir in TEMPLATES[app_name]['HTML_TEMPLATE_DIR']:
        tdir = join(temporary_target, basename(template_dir))
        #mkdir(tdir)
        copytree(template_dir, tdir)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('django_project_folder')
    parser.add_argument('app_name')
    args = parser.parse_args()
    print('*' * 20 + ' ARGUMENTS ' + '*' * 20 )
    print('django_project_folder: %s' % args.django_project_folder)
    print('app_name: %s' % args.app_name)
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

    copy_templates(temporary_target, args.app_name)

