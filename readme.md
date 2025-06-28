# snap-stream

Youtube video summarizer


## Setup Instructions

### Installing python
assuming we'll need different python versions for various projects we'll install our required version of the python i.e. `v3.11.5` in isolation.

1. Install system dependencies - [for more os not listed below](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
    1. macos + brew - `brew install openssl readline sqlite3 xz zlib tcl-tk@8 libb2`
1. install `asdf` - Follow the core installation steps from [official guide](https://asdf-vm.com/guide/getting-started.html).
1. install `asdf-python` plugin - https://github.com/asdf-community/asdf-python
    1. `asdf plugin-add python https://github.com/asdf-community/asdf-python.git` (pre-0.16.0)
    1. `asdf plugin add python https://github.com/asdf-community/asdf-python.git` (0.16.0+)
1. install python
    1. `asdf install python 3.11.5`

validate python is installed correctly 
```bash
➜  ~ python --version
Python 3.11.5

# for macos/unix
➜  ~ which python
/Users/myuser/.asdf/shims/python
```

### Setup virtual env
[Detailed instructions](https://fastapi.tiangolo.com/virtual-environments/)
1. go to the project dir
1. create `python3 -m venv --prompt . .venv`
1. activate `source .venv/bin/activate`
1. upgrade pip - `python -m pip install --upgrade pip`

### Install dependencies

`python -m pip install -r requirements/base.txt`

To install dev deps - `python -m pip install -r requirements/dev.txt`

### Setup Postgres
1. Install docker
    - https://docs.docker.com/get-started/get-docker/
    - https://www.docker.com/blog/how-to-check-docker-version/
1. start postgres server
    - from the project root dir - `docker-compose up -d postgres`
    - check it's up using `docker ps` or gui of Docker Desktop

### Setup .env file
1. make a copy of the [example.env](./example.env) and save as `.env` in the project root dir
1. update `.env` with the required values

### Start the server
1. `fastapi dev main.py` 
1. visit http://localhost:8000/ in the web-browser