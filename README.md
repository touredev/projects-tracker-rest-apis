# projects-tracker-rest-apis
REST APIs for Projects Tracker App Frontend.
Built using Django REST Framework (DRF) and PostgreSQL.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone touredev/projects-tracker-rest-apis.git
$ cd projects-tracker-rest-apis
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv -p python3 venv 
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd projects_api
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/`.
