LiteWarden
==========

LiteWarden Security And Safety Management

.. image:: https://img.shields.io/sonar/quality_gate/PopinjayJohn_LiteWarden?server=https%3A%2F%2Fsonarcloud.io
     :target: https://sonarcloud.io/dashboard?id=PopinjayJohn_LiteWarden
     :alt: Sonar Quality Gate
.. image:: https://img.shields.io/github/package-json/v/PopinjayJohn/LiteWarden
     :target: https://github.com/PopinjayJohn/LiteWarden
     :alt: GitHub package.json version
.. image:: https://img.shields.io/github/workflow/status/PopinjayJohn/LiteWarden/CI
     :target: https://github.com/PopinjayJohn/LiteWarden/actions/workflows/ci.yml
     :alt: GitHub Workflow Status
.. image:: https://img.shields.io/requires/github/PopinjayJohn/LiteWarden
     :target: https://requires.io/github/PopinjayJohn/LiteWarden/requirements/?branch=main
     :alt: Requires.io
.. image:: https://img.shields.io/github/milestones/progress-percent/PopinjayJohn/LiteWarden/1?label=Next%20Milestone
     :target: https://github.com/PopinjayJohn/LiteWarden/milestone/1
     :alt: GitHub milestone

:License: PolyForm Shield License 1.0.0

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Shortcuts
----------

.. image:: https://img.shields.io/github/issues/PopinjayJohn/LiteWarden/help%20wanted?label=Help%20Wanted
      :target: https://github.com/PopinjayJohn/LiteWarden/labels/help%20wanted
      :alt: GitHub help wanted issues
.. image:: https://img.shields.io/github/issues/PopinjayJohn/LiteWarden/Priority:%20Blocker?label=Blockers
     :target: https://github.com/PopinjayJohn/LiteWarden/labels/Priority%3A%20Blocker
     :alt: GitHub blocker issues
.. image:: https://img.shields.io/github/issues/PopinjayJohn/LiteWarden/Priority%3A%20Upcoming?label=Upcoming
     :target: https://github.com/PopinjayJohn/LiteWarden/labels/Priority%3A%20Upcoming
     :alt: GitHub upcoming release issues

.. contents::
   Table of Contents

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy litewarden

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog



Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



Custom Bootstrap Compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v4 is installed using npm and customised by tweaking your variables in ``static/sass/custom_bootstrap_vars``.

You can find a list of available variables `in the bootstrap source`_, or get explanations on them in the `Bootstrap docs`_.


Bootstrap's javascript as well as its dependencies is concatenated into a single file: ``static/js/vendors.js``.


.. _in the bootstrap source: https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss
.. _Bootstrap docs: https://getbootstrap.com/docs/4.1/getting-started/theming/
