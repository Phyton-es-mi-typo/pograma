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
flake8 ./app
~~~


## test

> Run tests

~~~sh
poetry run pytest
~~~
