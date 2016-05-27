# Licenser

Tool for adding open source licenses to your projects

---

[![PyPI](https://img.shields.io/pypi/v/licenser.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/pyversions/licenser.svg?maxAge=2592000)]()
[![Travis](https://img.shields.io/travis/tylucaskelley/licenser.svg?maxAge=2592000)]()

Finding and adding a license to your project is an annoying process,
and can be quite tedious depending on the license you choose.

Licenser allows you to quickly add a license to your project from
the command line. Supported licenses can be found in the
[assets folder](https://github.com/tylucaskelley/licenser/tree/master/licenser/assets).

Don't see what you need?
[Open an issue](https://github.com/tylucaskelley/licenser/issues/new)
to suggest the addition of other licenses!

### Prerequisites

* Python 2.7 or Python 3.5

### Installation

```bash
    $ pip install licenser
```

Alternatively, grab the
[zip](https://github.com/tylucaskelley/licenser/tarball/v2.0.1)!

### Usage

From the command line:

```bash
$ licenser -n "Your Name" -e "you@example.com" -l "license name" -p "project name"
```

Name, email, and license are the three required parameters; project will default
to the current directory name if you don't include it.

`--txt` will add the `.txt` extension to the `LICENSE` file.

### Configuration

If you're like me and don't change your name very often, you can save time by
storing your defaults for name, email, and license in `~/.licenser`:

```bash
name="Your Name"
email="you@example.com"
license="MIT"
```

### Contributing

I accept [pull requests](https://github.com/tylucaskelley/licenser/compare)!
There are some potential improvements I've been thinking about:

1. Prepending headers to source code files for licenses that recommend it
2. Pull licenses from an online API (maybe)
3. Support for more licenses

**Tip**: While working on a feature or bug, you can test your script by running
`python licenser` from the root project directory.

Additionally, make sure that all tests pass when you add features, and write
new unit tests if you add a function. Tests can be run using the `nosetests`
command from the root project directory.
