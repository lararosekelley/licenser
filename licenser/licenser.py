# -*- coding: utf-8 -*-

'''
licenser
========

Tool for adding open source licenses to your projects.
'''

from argparse import ArgumentParser as parser
from datetime import date
import os
import re

# get version info
with open('licenser/__init__.py', 'r') as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

# global variables
cfg = os.path.expanduser('~/.licenser')
cwd = os.path.dirname(__file__)
licenses_loc = '/assets/'


def find_in_matrix_2d(val, matrix):
    '''
    Returns a tuple representing the index of an item in a 2D matrix.

    Arguments:
        - val (str) Value to look for
        - matrix (list) 2D matrix to search for val in

    Returns:
        - (tuple) Ordered pair representing location of val
    '''

    dim = len(matrix[0])
    item_index = 0

    for row in matrix:
        for i in row:
            if i == val:
                break
            item_index += 1
        if i == val:
            break

    loc = (int(item_index / dim), item_index % dim)

    return loc


def compute_qwerty_distance(c1, c2):
    '''
    Provides a score representing the distance between two characters on a
    QWERTY keyboard, utilizing a simple matrix to represent the keyboard:

        | 0   1   2   3   4   5   6   7   8   9   10  11  12  13
      --+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
      0 | ` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | - | = |   |
      1 |   | q | w | e | r | t | y | u | i | o | p | [ | ] | \ |
      2 |   | a | s | d | f | g | h | j | k | l | ; | ' |   |   |
      3 |   |   | z | x | c | v | b | n | m | , | . | / |   |   |
      --+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

    For example, a score of 0 means the characters are the same, while a score
    of 5 means that it takes 5 position changes to get from c1 to c2. However,
    for characters that are 1 diagonal move away (such as q to s), the score is
    reduced from 2 to 1 to prevent any horizontal / vertical bias.

    Arguments:
        - c1 (str) Character to compare to 'c2'
        - c2 (str) Character to compare to 'c1'

    Returns:
        - (int) Number representing distance between two characters

    Raises:
        - ValueError: If the length of c1 or c2 is greater than 1
    '''

    # build table
    keyboard = [
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', ''],
        ['', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
        ['', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', '', ''],
        ['', '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '', '']
    ]

    loc_c1 = find_in_matrix_2d(c1, keyboard)
    loc_c2 = find_in_matrix_2d(c2, keyboard)

    # euclidean distance
    distance = ((loc_c2[0] - loc_c1[0])**2 + (loc_c2[1] - loc_c1[1])**2)**0.5

    return distance


def compute_distance(a, b):
    '''
    Computes a modified Levenshtein distance between two strings, comparing the
    lowercase versions of each string and accounting for QWERTY distance.

    Arguments:
        - a (str) String to compare to 'b'
        - b (str) String to compare to 'a'

    Returns:
        - (int) Number representing closeness of 'a' and 'b' (lower is better)
    '''

    # check simple cases first
    if not a:
        return len(b)
    if not b:
        return len(a)
    if a == b or str.lower(a) == str.lower(b):
        return 0

    # lowercase each string
    a = str.lower(a)
    b = str.lower(b)

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
            penalty = 0 if a[i] == b[j] else compute_qwerty_distance(a[i], b[j])
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
    p.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version=version))
    p.add_argument('--txt', action='store_true', required=False, help='add .txt to filename')

    args = p.parse_args()

    name = args.name if args.name else defaults.get('name')
    email = args.email if args.email else defaults.get('email')
    license = get_license(args.license) if args.license else defaults.get('license')
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
