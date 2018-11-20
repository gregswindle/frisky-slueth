# frisky_sleuth

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)


[![codecov](https://codecov.io/gh/gregswindle/frisky_sleuth/branch/master/graph/badge.svg?style=flat-square)](https://codecov.io/gh/gregswindle/frisky_sleuth)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fgregswindle%2Ffrisky_sleuth.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fgregswindle%2Ffrisky_sleuth?ref=badge_shield)

> Inspect repository resources against a list of patterns to detect sensitive or dangerous information by file contents, extension, name, and path.

## Table of Contents

<!-- toc -->

- [Security](#security)
- [Background](#background)
- [Install](#install)
  * [From Git](#from-git)
- [Usage](#usage)
  * [Terminal](#terminal)
  * [REPL](#repl)
- [API](#api)
  * [Terminal (command-line)](#terminal-command-line)
  * [Package/library](#packagelibrary)
- [Maintainers](#maintainers)
- [Contribute](#contribute)
- [License](#license)

<!-- tocstop -->

## Security

> `frisky` is a simpler port of
> [gitrob](https://github.com/michenriksen/gitrob) and is a command line
> utility to scan codebases for sensitive files/contents.  It is
> imagined this will happen as part of code review prior to open source
> release.
>
> `frisky` has some useful differences to gitrob:
>
>  - Single distribution file, making distribution trivial
>  - JSON output for integration with other utilities
>  - Ability to generate and consume and overrides file to suppress errors for specific matches
>  - Signature part 'contents' to analyze file contents
>
> _VerizonDigital/frisky_. (2018). _GitHub_. Retrieved 16 November 2018, from <https://github.com/VerizonDigital/frisky/blob/master/README.md>

## Background

This version of `frisky_sleuth` packages features into modules for unit testing, extensibility, and reusability. `frisky_sleuth` is now a Python3 library that can be invoked within:

- A command-line client (included);
- A Gitlab (or GitHub) webhook

## Install

### From Git

```bash
# Locally from Git:
git clone https://github.com/gregswindle/frisky_sleuth.git

# Change into the root directory.
cd frisky_sleuth

# Create a virtual environment.
# The value python3 passed to --python is the name of the
# Python interpreter you want to install into your virtual
# environment. Further calls to python while within your
# virtual environment will use that Python interpreter.
virtualenv --python=python3 venv

# Activate the virtual environment by sourcing the
# activate script created within the virtual environment
# directory.

# Linux and MacOS:
source ./venv/bin/activate

# Windows CMD or PowerShell:
# venv\Scripts\activate

# With the virtual environment activated you can install
# your library's required development tools by running:
pip install -r requirements-dev.txt
```

## Usage

### Terminal

Quick and dirty:

```bash
# Evaluate a directory (e.g., a local Git repo) for secrets:
frisky_sleuth "./you/might/be/surprised/repo"
# =>
#    ./subversion.py:129 has static passwords contents
#    ./certifi/cacert.pem has Potential cryptographic private key extension
#    ...
```

Halt evaluation on the first match found:

```bash
frisky_sleuth --first "./teh/31337/h4x0r/Warez"
# =>
#    ./venv/lib/python3.7/hashlib.py:187 has static passwords contents password = bytes(memoryview(password)) matches pattern (password|passwd|pass|pwd)['"]? ?[=:] ?['"]?(?!(['"]))
```

Show matching values:

```bash
frisky_sleuth --match "/p/a/t/h/t/o/directory-name"
# =>
#    /subversion.py:40 has static passwords contents data = 'password="OMG!LOL-puppies11"' matches pattern (password|passwd|pass|pwd)['"]? ?[=:] ?['"]?(?!(['"]))
#    ...
```

Replace the default <samp>./frisky_sleuth/frisky_sleuth/signatures.json</samp> with your own signature definitions:

```bash
frisky_sleuth --override-filename /usr/local/pwnage/all-your-base-are-belong-to-us.json ./Я0XX0ЯZ
```

Warm the cockles of your ever-`JSON`-lovin' 💔:

```bash
# Output JSON to the Terminal
frisky_sleuth --json /4chan/src/R/U/kidding/me

# Pipe JSON to file:
frisky_sleuth --json /omg/4realz/4chan/suxorz-c0de > ./suxorz-c0de-scan-violations.json
```

### REPL

```python
import frisky_sleuth

# Inspect a local git repository's resources
# for secrets:
violations = frisky_sleuth.evaluate('.', 'top-level-directory-name')

# Save violations to a JSON file:
frisky_sleuth.file.save(violations, '/path/to/violations.json')
```

## API

### Terminal (command-line)

```bash
# Output command-line help:
frisky_sleuth --help
Usage: frisky_sleuth [-h] [--first] [--match] [--no-color]
              [--override-filename OVERRIDE_FILENAME] [--warnings] [--verbose]
              [--json]
              PATH

Pre-receive oopsy checker

Positional arguments:
  PATH                  The directory to analyze

Optional arguments:
  -h, --help            Show this message and exit.
  --first               Exit on the first file that violates our rules.
  --match               Print the matching value.
  --no-color            No color output.
  --override-filename   OVERRIDE_FILENAME
                        Filename holding JSON overrides for violations in the form:
                        [{
                          "caption":"summary",
                          "description": "Optional details|null",
                          "path": "/p/a/t/h/t/o/file.pem",
                          "part": "contents|extension|filename|path",
                          "pattern": "pem",
                          "type": "match|regex"
                        }]
                        See ./frisky_sleuth/signatures.json for details.
  --warnings            Print violations that have been overriden.
  --verbose             Be noisy. Implies --match and --warnings.
  --json                Produce JSON output. Implies --no-color and --warnings; overrides --verbose.
```

### Package/library

```python
import frisky_sleuth

# Inspect a local git repository's resources
# for secrets:
violations = frisky_sleuth.evaluate('.', 'top-level-directory-name')

# Save violations to a JSON file:
frisky_sleuth.file.save(violations, '/path/to/violations.json')
```

## Maintainers

[@gregswindle](https://github.com/gregswindle)

## Contribute

See [the contribute file](CONTRIBUTING.md)!

PRs happily accepted.

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fgregswindle%2Ffrisky_sleuth.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fgregswindle%2Ffrisky_sleuth?ref=badge_large)

[Apache-2.0](LICENSE) © [Greg Swindle](https://github.com/gregswindle).
