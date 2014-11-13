# Licenser

**Current Release: v1.0.2**

*Quickly add an open source license to your project!*

---

Finding and adding a license to your project is an annoying process,
and can be quite tedious depending on the license you choose.

Licenser allows you to quickly add a license to your project from
the command line. Supported licenses as of now include:

* MIT
* New BSD
* GNU GPL v3.0
* Apache 2.0
* Mozilla 2.0

### Installation

First, make sure you have the dependencies:

* Python
* pip

Then, install Licenser:

    $ pip install licenser

### Basic Usage

It couldn't be simpler:

    $ cd path/to/project
    $ licenser -l MIT -n "Your name" -e you@example.com -p "Project name"

Boom! You'll now have a copy of the MIT License with your name and year in the root project folder.
The year will automatically be filled in using the current year. Make sure you enclose your name
with quotes so the program treats it as one argument.

If you don't want the file extension on your license, just add the "--no" flag at runtime.

### .licenser.json

If you're like me and don't change your name very often, you can save time by creating
a config file in your home directory.

It needs to look something like this:

```json
{
    "name": "Ty-Lucas Kelley",
    "email": "tylucaskelley@gmail.com",
    "license": "MIT",
    "filetypes": {
        ".java": "//",
        ".py": "#",
        ".js": "//"
    }
}
```

You can leave out any of the fields (except `filetypes`); anything that isn't found in the JSON file will have
to be passed in when you run the `licenser` script. Of course, you can also override this file
with the command line arguments.

### filetypes

The `filetypes` object is important if you're using a license like the GPL, because they
involve adding a header to the top of every source code file. You need to fill it in with
the type of file and the character(s) it use(s) for one-line comments.

Note that this is the ONLY WAY you can properly use licenses like the GPL or Apache.
If you leave it out, the license will be added in the normal "LICENSE.txt" file,
but the source code will not have headers prepended to it.

And fear not; if you attempt to prepend a license twice to the same file, you won't end up with two
license headers; the old one will remain in place.
