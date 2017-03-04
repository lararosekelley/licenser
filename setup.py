#!/usr/bin/env python

import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('licenser/__init__.py', 'r') as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            f.read(), re.MULTILINE).group(1)
if not version:
    raise RuntimeError('Cannot find version information')

config = {
    'name': 'licenser',
    'version': version,
    'description': 'Tool for adding open source licenses to your projects',
    'author': 'Ty-Lucas Kelley',
    'author_email': 'tylucaskelley@gmail.com',
    'license': 'MIT',
    'url': 'http://github.com/tylucaskelley/licenser',
    'long_description': open('README.md').read(),
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    'entry_points': {
        'console_scripts': [
            'licenser = licenser.licenser:main'
        ]
    },
    'keywords': [
        'cli',
        'license',
        'tools',
        'script'
    ],
    'packages': [
        'licenser'
    ],
    'package_dir': {
        'licenser': 'licenser'
    },
    'package_data': {
        'licenser': [
            'assets/*'
        ]
    },
    'test_requires': [
        'nose==1.3.7'
    ]
}

setup(**config)
