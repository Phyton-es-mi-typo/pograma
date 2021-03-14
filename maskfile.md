# Tasks for tyempo

## run

> Run ASGI web server

~~~sh
poetry run uvicorn app.apirest.apirest:app --reload
>>>>>>> 9d3300ed35688ceb622f0ade1b37250b833b9de0
~~~

## check

> Check linters errors

This task is to check is everything ok for our linters.

~~~sh
flake8 ./app
~~~
