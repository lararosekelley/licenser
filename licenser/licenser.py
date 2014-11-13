#!/usr/bin/env python

from argparse import ArgumentParser as parser
from datetime import date
from os.path import expanduser
from os.path import isfile
from os.path import dirname
import json

config_file = expanduser('~/.licenser.json')
pwd = dirname(__file__)
licenses = ['GPL', 'Apache', 'Mozilla', 'MIT', 'BSD']


def __get_defaults():
    """Return the default options from the ~/.licenser.json file."""
    if isfile(config_file):
        with open(config_file) as f:
            defaults = json.load(f)
        return defaults
    else:
        return {}


def __get_args(defaults):
    """Parse command line arguments and merge them with the defaults."""
    need_name = False if 'name' in defaults else True
    need_email = False if 'email' in defaults else True
    need_license = False if 'license' in defaults else True

    p = parser(description='quickly add an open-source license to your project')

    p.add_argument('-l', dest='license', required=need_license, help='license to add')
    p.add_argument('-e', dest='email', required=need_email, help='your email address')
    p.add_argument('-n', dest='name', required=need_name, help='your name')
    p.add_argument('-p', dest='project', required=True, help='project name')
    p.add_argument('--no', action='store_true', required=False, help='remove .txt')

    args = p.parse_args()

    name = args.name if args.name else defaults.get('name')
    email = args.email if args.email else defaults.get('email')
    author = name + ' <' + email + '>'
    license = args.license if args.license else defaults.get('license')
    project = args.project
    year = str(date.today().year)
    ext = '' if args.no else '.txt'

    if license not in licenses:
        p.exit(1, 'fatal: license %s does not exist\n' % license)

    return (author, license, project, year, ext)


def __get_license(l):
    """Grabs the text from the specified license and header files and formats them."""
    license_file = pwd + '/licenses/' + l
    license_header = pwd + '/licenses/' + l + '_header'
    license = None
    header = None

    if isfile(license_file):
        with open(license_file) as f:
            license = f.read()
    if isfile(license_header):
        with open(license_header) as f:
            header = f.read()

    return (license, header)


def add_license():
    """Add a license to a file."""
    defaults = __get_defaults()
    author, license_name, project, year, ext = __get_args(defaults)
    license, header = __get_license(license_name)

    license = license.format(author=author, year=year, project=project)
    if header:
        header = header.format(author=author, year=year, project=project)

    with open('LICENSE' + ext, 'w') as f:
        f.write(license)


if __name__ == '__main__':
    add_license()
