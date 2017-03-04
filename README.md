# Licenser

Tool for adding open source licenses to your projects

---

[![PyPI](https://img.shields.io/pypi/v/licenser.svg?maxAge=3600)](http://pypi.python.org/pypi/licenser)
[![PyPI](https://img.shields.io/pypi/pyversions/licenser.svg?maxAge=3600)](http://pypi.python.org/pypi/licenser)
[![Travis](https://travis-ci.org/tylucaskelley/licenser.svg?branch=master)](https://travis-ci.org/tylucaskelley/licenser)

Finding and adding a license to your project is an annoying process,
and can be quite tedious depending on the license you choose.

Licenser allows you to quickly add a license to your project from
the command line. Supported licenses can be found in the
[assets folder](https://github.com/tylucaskelley/licenser/tree/master/licenser/assets).

Don't see what you need?
[Open an issue](https://github.com/tylucaskelley/licenser/issues/new)
to suggest the addition of other licenses!

### Prerequisites

* Python 2.7.x or Python 3.6.x

### Installation

```bash
$ pip install licenser
```

Alternatively, grab the
[zip](https://github.com/tylucaskelley/licenser/tarball/v2.0.4)!

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

Now any time you run `licenser`, you don't need to provide arguments unless you
want to override defaults.

### Development Setup

I recommend using `pyenv` with the `pyenv-virtualenv` plugin. [This][1]
document provides information on setting that up.

Regardless, make sure you have Python 2.7 or 3.6 installed in some form.

**With pyenv**

First, clone the repository:

```bash
$ git clone https://github.com/tylucaskelley/licenser && cd licenser
```

Next, create your virtual environment and activate it:

```bash
$ pyenv virtualenv venv && pyenv activate venv
```

Finally, install the dependencies:

```bash
$ pip install -r requirements.txt
```

Now you're good to go! Run tests with the `nosetests` command and test out the
script with `python licenser [args]`.

**Without pyenv**

Clone the repository:

```bash
$ git clone https://github.com/tylucaskelley/licenser && cd licenser
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Now you're good to go! Run tests with the `nosetests` command and test out the
script with `python licenser [args]`.

### Contributing

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details.

I accept [pull requests](https://github.com/tylucaskelley/licenser/compare);
there are some potential improvements I've been thinking about:

1. Prepending headers to source code files for licenses that recommend it
2. Pull licenses from an online API (maybe)
3. Support for more licenses

Additionally, make sure that all tests pass when you add features, and write
new unit tests if you add a function. Tests can be run using the `nosetests`
command from the root project directory.

[1]: https://github.com/yyuu/pyenv-virtualenv#installation
