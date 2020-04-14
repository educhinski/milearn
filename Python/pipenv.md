#

## A brief introduction to pipenv

* create a virtualenv with pipenv with the requests package to start with

``` bash
pipenv install requests
```

* activate our environment

``` bash
pipenv shell
```

* deactivate

``` bash
exit
```

* run python within our environment(without activating or our env)

``` bash
pipenv run python
```

* similarly run a script using our env python

``` bash
pipenv run python script.py
```

* install some more packages from a file

  * _will update the existing pacakges_

``` bash
pipenv install -r /path/to/requirements/file/requirements.txt
```

* add our dependencies to a requirements file

``` bash
pipenv lock -r
```

* install a package only in the dev environment (which is not needed in production)

``` bash
pipenv install pytest --dev
```

* remove an installed package

``` bash
pipenv uninstall requests
```

* recreate our environment with a different python version

``` bash
pipenv --python=3.6
```

* remove a virtualenv completely

``` bash
pipenv --rm
```

* install a virtualenv that matcehs our pipfile

``` bash
pipenv install
```

* find path to your virtual environment

``` bash
pipenv --venv
```

* check for non-security vulnerabilities for our package

``` bash
pipenv check
```

* display dependency graph

``` bash
pipenv graph
```

* when ready to push to production and all the tests passed

  * updates Pipfile.lock

  ``` bash
  pipenv lock
  ```

  * move pipfile to production environment

  -_when you're ready to install everything in pipfile.lock_

  ``` bash
  pipenv install --ignore-pipfile
  ```

  -_will ignore default pipfile and use current pipfile.lock_

* setting environment variables

  * create a `.env` file in the project's folder

  * add the environment variables we wanted to set
