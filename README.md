# Refu backend application

## Installation

* Install Python 3.4
* Install PostgreSQL 9.4
* Install http://www.stickpeople.com/projects/python/win-psycopg/2.6.1/psycopg2-2.6.1.win32-py3.4-pg9.4.4-release.exe
* Run ``pip install -r requirements.txt``

## Running

* Write local.env containing your `DATABASE_URL`.
  e.g. ``DATABASE_URL=postgres://postgres@localhost/refu``
* ``heroku local -e local.env -f Procfile.windows``
