# -*- coding: utf-8 -*-

'''
licenser
========

Tool for adding open source licenses to your projects.
'''

from argparse import ArgumentParser as parser
from datetime import date
import os

cfg = os.path.expanduser('~/.licenser')
cwd = os.path.dirname(__file__)
licenses_loc = '/assets/'


def compute_distance(a, b):
    '''
    Computes the Levenshtein distance between two strings.

    Arguments:
        - a (str) String to compare to 'b'
        - b (str) String to compare to 'a'

    Returns:
        - (int) Number representing closeness of 'a' and 'b' (lower is better)
    '''

    # check simple cases first
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    # create empty vectors to store costs
    vector_1 = [-1] * (len(b) + 1)
    vector_2 = [-1] * (len(b) + 1)

    # set default values
    for i in range(len(vector_1)):
        vector_1[i] = i

    # compute distance
    for i in range(len(a)):
        vector_2[0] = i + 1

        for j in range(len(b)):
            penalty = 0 if a[i] == b[j] else 1
            vector_2[j + 1] = min(vector_2[j] + 1, vector_1[j + 1] + 1, vector_1[j] + penalty)

        for j in range(len(vector_1)):
            vector_1[j] = vector_2[j]

    return vector_2[len(b)]


def get_defaults(path):
    '''
    Reads file for configuration defaults.

    Arguments:
        - path (str) Absolute filepath (usually ~/.licenser)

    Returns:
        - (dict) Defaults for name, email, license, .txt extension
    '''

    defaults = {}

    if os.path.isfile(path):
        with open(path) as f:

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


def get_license(name):
    '''
    Returns the closest match to the requested license.

    Arguments:
        - name (str) License to use

    Returns:
        - (str) License that most closely matches the 'name' parameter
    '''

    filenames = os.listdir(cwd + licenses_loc)
    licenses = dict(zip(filenames, [-1] * len(filenames)))

    for l in licenses:
        licenses[l] = compute_distance(name, l)

    return min(licenses, key=(lambda k: licenses[k]))


def get_args(path):
    '''
    Parse command line args & override defaults.

    Arguments:
        - path (str) Absolute filepath

    Returns:
        - (tuple) Name, email, license, project, ext, year
    '''

    defaults = get_defaults(path)
    licenses = ', '.join(os.listdir(cwd + licenses_loc))
    p = parser(description='tool for adding open source licenses to your projects. available licenses: %s' % licenses)

    _name = False if defaults.get('name') else True
    _email = False if defaults.get('email') else True
    _license = False if defaults.get('license') else True

    p.add_argument('-n', dest='name', required=_name, help='name')
    p.add_argument('-e', dest='email', required=_email, help='email')
    p.add_argument('-l', dest='license', required=_license, help='license')
    p.add_argument('-p', dest='project', required=False, help='project')
    p.add_argument('--txt', action='store_true', required=False, help='add .txt to filename')

    args = p.parse_args()

    name = args.name if args.name else defaults.get('name')
    email = args.email if args.email else defaults.get('email')
    license = get_license(args.license, licenses_loc=licenses_loc) if args.license else defaults.get('license')
    project = args.project if args.project else os.getcwd().split('/')[-1]
    ext = '.txt' if args.txt else ''
    year = str(date.today().year)

    return (name, email, license, project, ext, year)


def generate_license(args):
    '''
    Creates a LICENSE or LICENSE.txt file in the current directory. Reads from
    the 'assets' folder and looks for placeholders enclosed in curly braces.

    Arguments:
        - (tuple) Name, email, license, project, ext, year
    '''

    with open(cwd + licenses_loc + args[2]) as f:
        license = f.read()

    license = license.format(name=args[0],
                             email=args[1],
                             license=args[2],
                             project=args[3],
                             year=args[5])

    with open('LICENSE' + args[4], 'w') as f:
        f.write(license)
        print('licenser: license file added to current directory')


def main():
    '''
    Gets arguments and generates a LICENSE file.
    '''

    args = get_args(cfg)
    generate_license(args)


if __name__ == '__main__':
    main()
