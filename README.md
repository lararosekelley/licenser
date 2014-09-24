# Licenser

*Quickly add an open source license to your project!*

---

Finding and adding a license to your project is an annoying process, 
and can be quite tedious depending on the license you choose.

Licesnser allows you to quickly add a license to your project from
the command line. Supported licenses as of now include:

* MIT
* New BSD

### Installation

First, make sure you have the dependencies:

* Python
* pip

Then, install Licenser:

    $ pip install licenser
    
### Example Usage

It couldn't be simpler:

    $ cd path/to/project
    $ licenser -l MIT -n "Your name" -e you@example.com -p "Project name"
    
Boom! You'll now have a copy of the MIT License with your name and year in the root project folder.
The year will automatically be filled in using the current year. Make sure you enclose your name
with quotes so the program treats it as one argument.
