# Contributing

## Getting Started

Fork the repository to your own account.

Clone the repository to a suitable location on your local machine.

```bash
git clone https://gitlab.com/<your-account>/frisky_sleuth.git
```

**Note:** This will clone the entire contents of the repository at the HEAD revision.

To update the project from within the project's folder you can run the following command:

```bash
git pull --rebase
```

### Building

Change into the root directory.

```bash
cd frisky_sleuth
```

Create a virtual environment.

```bash
virtualenv --python=python3 venv
```

---

**Note:** The value python3 passed to --python is the name of the
Python interpreter you want to install into your virtual
environment. Further calls to python while within your
virtual environment will use that Python interpreter.

---

Activate the virtual environment by sourcing the activate script created within the virtual environment directory.

- _Linux and MacOS:_

    ```bash
    source ./venv/bin/activate
    ```

- _Windows CMD or PowerShell:_

    ```shell
    venv\Scripts\activate
    ```

Install the project's dependencies.

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Testing

Install the project's dependencies.

```bash
pip install -r requirements-dev.text
```

Next, run the project's tests.

```bash
python3 setup.py test
```

Don't forget code coverage!

```bash
python3 setup.py coverage
# =>
running coverage
..................
----------------------------------------------------------------------
Ran 18 tests in 0.006s

OK
Name                                 Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------------------
frisky_sleuth/__init__.py                4      0      0      0   100%
frisky_sleuth/constants.py              17      0      0      0   100%
frisky_sleuth/evaluate/__init__.py       1      0      0      0   100%
frisky_sleuth/evaluate/file.py          13      9      4      0    24%   17-31
frisky_sleuth/evaluate/load.py          39     15      8      0    51%   23-24, 39-40, 78-91
frisky_sleuth/evaluate/match.py         31     13     12      1    49%   49-60, 72-79, 22->25
frisky_sleuth/evaluate/validate.py      21      9      4      0    48%   14-16, 63-70
frisky_sleuth/signature.py              29      8      4      0    64%   33, 61-69, 78
frisky_sleuth/violation.py               9      0      0      0   100%
--------------------------------------------------------------------------------
TOTAL                                  164     54     32      1    58%
```

Detailed reports are available as HTML:

```bash
open ./docs/reports/coverage/index.html
```

## Feature Requests

I'm always looking for suggestions to improve this project. If you have a suggestion for improving an existing feature, or would like to suggest a completely new feature, please file an issue with my [GitLab repository](https://gitlab.com/gregswindle/frisky_sleuth/issues).

## Defect Reports

My project isn't always perfect, but I strive to always improve on that work. You may file bug reports on the [GitLab repository](https://gitlab.com/gregswindle/frisky_sleuth/issues) site.

## Pull Requests

Along with my desire to hear your feedback and suggestions, I'm also interested in accepting direct assistance in the form of new code or documentation.

Please feel free to file merge requests against my [GitLab repository](https://gitlab.com/gregswindle/frisky_sleuth/pulls).
