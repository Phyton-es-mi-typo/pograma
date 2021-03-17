# Tasks for tyempo

## run

> Run ASGI web server

~~~sh
poetry run uvicorn app.apirest.apirest:app --reload
~~~

## check

> Check linters errors

This task is to check is everything ok for our linters.

~~~sh
poetry run flake8 ./app
~~~

## test

> Run tests

~~~sh
poetry run pytest
~~~

## clean

> Clean the project of cached files, compiled pyc files, etc.

~~~sh
find . -type d -name '__pycache__' -exec rm -rf {} +
find . -type d -name '.pytest_cache' -exec rm -rf {} +
find . -type f -name '*.py[co]' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
~~~
