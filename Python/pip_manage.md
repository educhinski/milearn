#

## command to update pip packages

``` bash
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

## virtualenvs - and managing multiple projects

create a conda virtual environment

``` bash
conda create -n "envname" python=python_version
```

activate the virtual environment

``` bash
conda activate envname
```

export your environment to a file

``` bash
conda env export > env_file.yaml
```

recreate the virtual environment from the file

``` bash
conda env create -f env_file.yaml
```
