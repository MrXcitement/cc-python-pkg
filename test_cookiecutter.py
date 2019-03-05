"""Test the ability to create a cookiecutter project."""

from __future__ import absolute_import, division, print_function


def test_bake(cookies):
    """Create a default cookie cutter project and verify it was created."""

    result = cookies.bake()

    assert result.exit_code == 0
    assert result.project.basename == 'python-hello'
    assert result.project.isdir()
