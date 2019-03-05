Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

### Report Bugs

Report bugs at https://github/mrxcitement/cc-python-pkg

If you are reporting a bug, please include:

-  Your operating system name and version.
-  Any details about your local setup that might be helpful in
   troubleshooting.
-  Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with \"bug\"
and \"help wanted\" is open to whoever wants to fix it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
\"enhancement\" and \"help wanted\" is open to whoever wants to
implement it.

### Write Documentation

cc-python-pkg could always use more documentation,
whether as part of the official cc-python-pkg docs,
in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/mrxcitement/cc-python-pkg.

If you are proposing a feature:

-  Explain in detail how it would work.
-  Keep the scope as narrow as possible, to make it easier to
   implement.
-  Remember that this is a volunteer-driven project, and that
   contributions are welcome :)

Get Started!
------------

Ready to contribute? Here\'s how to set up
[cc-python-pkg](https://github.com/mrxcitement/cc-python-pkg) for local
development.

1.  Fork the [cc-python-pkg](https://github.com/mrxcitement/cc-python-pkg) repo.

1.  Clone your fork locally:

        $ git clone https://github.com/<your username>/cc-python-pkg

1.  Install your local copy into a python 3 virtualenv. Assuming you
    have python 3 installed, this is how you set up your fork for local
    development:

        $ cd cc-python-pkg
        $ python3 -m venv .venv
        $ source .venv/bin/activate
        $ pip install -U pip
        $ pip install -r requirements-dev.txt -e .

1.  Create a branch for local development:

        $ git checkout -b <name-of-your-bugfix-or-feature>

    Now you can make your changes locally.

1.  When you\'re done making changes, check that your changes pass the
    tests:

        $ pytest

1.  Run static analysis of the python source, fix any errors.

        $ flake8

1.  Commit your changes and push your branch:

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

1.  Submit a pull request through the
    https://github.com/mrxcitement/cc-python-pkg website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
1.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.md.
1.  The pull request should work with cookiecutter >= 1.6.

Deploying
---------

A reminder for the maintainers on how to deploy. Make sure all your
changes are committed, including an entry in CHANGELOG.rst.

### Requires:
-  bumpversion

### Steps:

    $ bumpversion patch # possible: major / minor / patch
    $ git push
    $ git push --tags
