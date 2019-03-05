{{cookiecutter.project_name}}
=============================

{{cookiecutter.project_description}}

Basic setup
-----------

Install the application:

::

   $ pip install -U --user .

Run the application:

::

   $ {{cookiecutter.cli_name}}

Run the tests:

::

   $ tox

Develop the application:

::

   $ python3 -m venv venv3
   $ source venv3/bin/activate
   $ pip install -r requirements-dev.txt -e .
