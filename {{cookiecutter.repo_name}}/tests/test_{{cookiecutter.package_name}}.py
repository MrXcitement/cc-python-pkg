"""Test {{ cookiecutter.package_name }}"""
from __future__ import absolute_import, division, print_function
import subprocess
import sys


def check_output(process):
    """Return processes output as a string"""
    result = subprocess.check_output(process)
    if sys.version_info.major >= 3:
        return result.decode()
    return result


def test_cli_greet():
    """Test the cli greet function."""
    import {{ cookiecutter.package_name }}.cli

    result = {{ cookiecutter.package_name }}.cli.greet().lower()
    assert 'hello' in result


def test_cli():
    """Test the cli process."""
    result = check_output(['{{ cookiecutter.cli_name }}']).lower()
    assert 'hello' in result

    result = check_output(['python', '-m', '{{ cookiecutter.cli_name }}']).lower()
    assert 'hello' in result
