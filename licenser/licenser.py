#!/usr/bin/env python

from argparse import ArgumentParser as parser
from datetime import date
import json
import os

config_file = os.path.expanduser('~/.licenser.json')
pwd = os.path.dirname(__file__)
licenses = ['GPL', 'Apache', 'Mozilla', 'MIT', 'BSD']


def __get_defaults():
    """Return the default options from the ~/.licenser.json file."""
    if os.path.isfile(config_file):
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

    if os.path.isfile(license_file):
        with open(license_file) as f:
            license = f.read()
    if os.path.isfile(license_header):
        with open(license_header) as f:
            header = f.read()

    return (license, header)


def __add_header(src_file, header, comment):
    """Prepends a license header to a file."""
    commented_header = [''.join([comment, ' ', s, '\n']) for s in header.split('\n')]
    commented_header[-1] = '\n'

    with open(src_file, 'r') as f:
        file_lines = commented_header + f.readlines()

    with open(src_file, 'w') as f:
        f.writelines(file_lines)


def add_license():
    """Add a license to a file."""
    defaults = __get_defaults()
    author, license_name, project, year, ext = __get_args(defaults)
    license, header = __get_license(license_name)

    license = license.format(author=author, year=year, project=project)

    with open('LICENSE' + ext, 'w') as f:
        f.write(license)

    if header:
        if 'filetypes' not in defaults:
            print("warning: filetypes object missing from ~/.licenser.json")
        else:
            header = header.format(author=author, year=year, project=project)
            filetypes = defaults.get('filetypes')
            exts = tuple(filetypes.keys())

            for root, dirs, files in os.walk(os.getcwd(), topdown=True):
                ignore = True if 'ignore' in defaults else False

                if ignore:
                    files = [f for f in files if f not in defaults['ignore']]
                    dirs[:] = [d for d in dirs if d not in defaults['ignore']]

                for f in files:
                    if f.endswith(exts):
                            src_file = os.path.join(root, f)
                            comment = filetypes.get(os.path.splitext(src_file)[1])

                            with open(src_file) as src:
                                first_line = src.readline()

                            if comment + ' ' + project not in first_line:
                                __add_header(src_file, header, comment)


if __name__ == '__main__':
    add_license()
