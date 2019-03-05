#!/usr/bin/env python
"""{{cookiecutter.project_name}}

{{cookiecutter.project_description}}
"""
from __future__ import absolute_import, division, print_function


def greet():
    """Return a greeting."""
    return "Hello, {{cookiecutter.project_name}}!"


def main():
    """Print a greeting to the console."""
    print(greet())


if __name__ == "__main__":
    main()
