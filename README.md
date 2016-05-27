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
[zip](https://github.com/tylucaskelley/licenser/tarball/v2.0.0)!

### Usage

From the command line:

```bash
$ licenser -n "Ty-Lucas Kelley" -e "tylucaskelley@gmail.com" [-l BSD] [-p project] [--txt]
```

Name and email are the only needed parameters. License defaults to `MIT` and
project defaults to the current directory name.

`--txt` will add the `.txt` extension to the `LICENSE` file.

### Configuration

If you're like me and don't change your name very often, you can save time by
storing your defaults in `~/.licenser`:

```json
{
    "name": "Ty-Lucas Kelley",
    "email": "tylucaskelley@gmail.com",
    "license": "MIT",
    ".txt": true
}
```

### Contributing

I accept [pull requests](https://github.com/tylucaskelley/licenser/compare)!
There are some potential improvements I've been thinking about:

1. Prepending headers to source code files for licenses that recommend it
2. Pull licenses from an online API
3. Support for more licenses

**Tip**: While working on a feature or bug, you can test your script by running
`python -m licenser` from the root project directory.
