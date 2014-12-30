# Licenser

*Quickly add an open source license to your project!*

---

![version](https://pypip.in/version/licenser/badge.svg)
![downloads](https://pypip.in/download/licenser/badge.svg)

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

* A Mac or Linux computer (not tested on Windows)
* Python (2 or 3)
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
    },
    "ignore": [
        "node_modules",
        "lib",
        "bin",
        "dist",
        "Gruntfile.js",
        ".git"
    ]
}
```

These defaults can be overridden by using the normal command-line arguments. They're optional,
but if you want to use a license that recommends prepending your source code files with a header,
you'll need the `filetypes` object, which contains key-value pairs of file extensions and their
respective syntax for one-line comments.

Leaving out the `filetypes` object will simply mean skipping the step of prepending your code,
and will result in a warning message upon program exit:

    warning: filetypes object missing from ~/.licenser.json

To avoid prepending the same source code files more than once (if you call `licenser` multiple times),
the script will skip any files that contain the commented out project name on the first line. If you
want to switch licenses, you'll have to manually remove the headers from your source code.

The `ignore` array is pretty important too; you don't want to be prepending license headers to
third-party files, or minified JavaScript code.

### Contributing

I accept pull requests! There are some potential improvements I've been thinking about:

* Override global `ignore` and `filetypes` settings with a project-specific `.licenserconfig` file
* Switch to multi-line comments (which will help with supporting CSS and HTML)
