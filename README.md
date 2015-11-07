# Refu backend application

## Installation

* Install Python 3.4
* Install PostgreSQL 9.4
* On Windows: Install http://www.stickpeople.com/projects/python/win-psycopg/2.6.1/psycopg2-2.6.1.win32-py3.4-pg9.4.4-release.exe
* Run ``pip install -r requirements.txt``

## Running

* Create local.env containing your these properties:
    * `DATABASE_URL`: Database connection string
    * `SECRET_KEY`: Session secret

    Example `local.env` file:
    ```
    SECRET_KEY=abcdefghij28731879
    DATABASE_URL=postgres://postgres@localhost/refu
    ```

* Run ``python manage.py collectstatic``
* Run ``python manage.py migrate``
* On Windows: Run ``heroku local -e local.env -f Procfile.windows``
* On Unix: Run ``heroku local -e local.env``

## Future improvements

* Rename `SimpleOffer` to distinguish between multiple types
* Add proper account+authentication system
