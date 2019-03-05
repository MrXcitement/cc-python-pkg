#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The setup script.

{{ cookiecutter.project_description }}
"""

from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import setup
from setuptools import find_packages

DEPENDENCIES = []
with open('README.rst') as readme_file:
    README = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    CHANGELOG = changelog_file.read()

setup(
    name='{{ cookiecutter.pypi_name }}',
    version='{{ cookiecutter.version }}',
    license='MIT',
    description='{{ cookiecutter.project_description }}',
    long_description=README + '\n\n' + CHANGELOG,
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    url='{{ cookiecutter.repo_url }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=DEPENDENCIES,
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.cli_name }} = '
            '{{ cookiecutter.package_name }}.cli:main',
        ]
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
