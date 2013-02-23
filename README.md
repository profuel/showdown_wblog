showdown_wblog
==============

Python Web Frameworks Showdown, Dnipropetrovsk, Ukraine, February 23, Ukraine


Installing
----------

- Create and activate new virtual environment
$ virtualvenv .venv && . .venv/bin/activate
- Intall dependencies
$ pip install -r requirements/requirements-dev.txt
- Create database
$ python manage.py syncdb
- Run application
$ python manage.py runserver
- Enjoy!