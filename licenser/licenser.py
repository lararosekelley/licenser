# -*- coding: utf-8 -*-

'''
licenser
========

Tool for adding open source licenses to your projects
'''

from argparse import ArgumentParser as parser
from datetime import date
import os

cfg = os.path.expanduser('~/.licenser')
cwd = os.getcwd()

matches = [
    'apache-2.0',
    'bsd-2-clause',
    'bsd-3-clause',
    'epl-1.0',
    'gpl-2.0',
    'gpl-3.0',
    'mit',
    'mpl-2.0'
]


def get_license(name='mit'):
    '''
    returns the requested license
    '''

    return name


def get_defaults():
    '''
    reads cfg for default values
    '''

    defaults = {}

    if os.path.isfile(cfg):
        with open(cfg) as f:

            for line in f:
                line = line.strip()
                if '=' not in line or line.startswith('#'):
                    continue

                k, v = line.split('=', 1)
                v = v.strip('"').strip("'")

                defaults[k] = v
        return defaults
    else:
        return {}


def get_args():
    '''
    parse command line args & override defaults

    returns
    '''

    defaults = get_defaults()
    p = parser(description='tool for adding open source licenses to your projects')

    _name = False if defaults.get('name') else True
    _email = False if defaults.get('email') else True

    p.add_argument('-n', dest='name', required=_name, help='name')
    p.add_argument('-e', dest='email', required=_email, help='email')
    p.add_argument('-l', dest='license', required=False, help='license')
    p.add_argument('-p', dest='project', required=False, help='project')
    p.add_argument('--txt', action='store_true', required=False, help='add .txt')

    args = p.parse_args()

    name = args.name if args.name else defaults.get('name')
    email = args.email if args.email else defaults.get('email')
    license = get_license(args.license) if args.license else defaults.get('license')
    project = args.project if args.project else os.getcwd().split('/')[-1]
    ext = '.txt' if args.txt else ''
    args.year = str(date.today().year)

    return (name, email, license, project, ext, year)


def main():
    print get_args()

if __name__ == '__main__':
    main()
