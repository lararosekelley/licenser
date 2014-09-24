"""
licenser, v0.1.0
--------

licenser is a simple way to quickly add an open-source license to
your project. And it's MIT licensed!

Supported licenses:

* MIT
* BSD
* Mozilla

Installation:

    $ pip install licenser

Usage: 

    $ cd /path/to/project
    $ licener -l LICENSE -n NAME -e EMAIL -p PROJECT
    
Copyright (c) 2014 Ty-Lucas Kelley <tylucaskelley@gmail.com>
    
"""

from setuptools import setup

setup(
    name = "licenser",
    version = "0.1.0",
    description = "Quickly add an open-source license to your project.",
    entry_points = {
        'console_scripts': [
            'licenser = licenser.licenser:add_license'   
        ]
    },
    author = "Ty-Lucas Kelley",
    author_email = "tylucaskelley@gmail.com",
    license = "MIT",
    url = "http://github.com/tylucaskelley/licenser",
    download_url = "https://github.com/tylucaskelley/licenser/tarball/v0.1.0",
    long_description = __doc__,
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Utilities"
    ],
    py_modules=['licenser']
)