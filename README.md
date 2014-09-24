# Licenser

*Quickly add an open source license to your project!*

---

Finding and adding a license to your project is an annoying process, 
and can be quite tedious depending on the license you choose. 

Licenser lets you apply the MIT License to your code, and is intended
for smaller projects where something as large as the GNU or Apache license
isn't necessary.

### Installation

First, make sure you have the dependencies:

* Python 2 or 3
* pip

Then, install Licenser:

    $ pip install licenser
    
### Usage

It couldn't be simpler:

    $ cd path/to/project
    $ licenser -n Your Name -e you@example.com
    
Boom! You'll now have a copy of the MIT License with your name and year in the root project folder.
The year will automatically be filled in using the current year.