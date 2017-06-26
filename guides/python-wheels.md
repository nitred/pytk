# About
Guide to using python wheels.

# Commands
`python setup.py bdist_wheel`  

`pip install --no-index --find-links=dist/ PACKAGE==VERSION`  

`pip wheel -r requirements.txt`  
- creates all wheels in root folder
- `mv *.whl dist/`

# Experiments

## Experiment 1 (simple wheel creation and check if dependencies get installed)
* Create wheel dev_environment.yml with pandas etc
* In wheel environment install wheel and check if pandas is available
- **FAILED**

## Experiment 2
* dev env
  * `make create_dev_env`
  * `python setup.py bdist_wheel`
  * `pip wheel -r requirements.txt`
  * `mv *.whl dist/`
* wheel env
  * `make create_wheel_env`
  * `pip install --no-index --find-links=dist/ obix_fetch_service==0.1.0`
  * `pip install --no-index --find-links=dist/ --no-cache-dir -r requirements.txt`

## Experiment 3 (Dependency wheels from setup.py, --no-index & --find-links installation)
* Do: Create wheels for all dependencies as well
* Do: Use --wheels_dir and --find-links when creating wheels
* Do: Don't use --no-index when creating wheels
* Do: Use --no-index and --find-links when installing
* Issues: Package names have inconsistencies so we have to manually check what the package names internally are called.
* Issues: If multiple packages rely on the same dependency with different versions, then the dependency with the highest version is chosen. This may cause issues.
* Issues: Unofficial dependency packages with `dependency_links` is no longer supported, therefore other official PyPi packages are pulled when creating wheels. Eg. Pylogging.

## Experiment 4 (No dependency wheels, --find-links & PyPi installation)
* Do: Do not create wheels for dependencies by using --no-deps when creating wheels.
* Do: Use --wheels_dir and --find-links when creating wheels
* Do: Don't use --no-index when creating wheels
* Do: Use --no-index and --find-links when installing
* Issues: Unofficial dependency packages with `dependency_links` is no longer supported, therefore other official PyPi packages are pulled when creating wheels and installing. Eg. Pylogging.

## Experiment 5 (Dependency wheels from requirements, --no-index & --find-links installation)

## Experiment 6 (Custom PyPi server)


## TODO
- create wheel with dependencies
  - with a single command
  - add to install requires etc
- python package entire environment

# Makefiles for Experiements
PROJECT_NAME = ""
PROJECT_NAME_WHEEL = ""
ANACONDA_VERSION = "3"

ROOT_DIR = $(shell echo ~/anaconda$(ANACONDA_VERSION))
ROOT_PYTHON= "$(ROOT_DIR)/bin/python"
ROOT_CONDA = "$(ROOT_DIR)/bin/conda"

ENV_DIR = "$(ROOT_DIR)/envs/$(PROJECT_NAME)"
ENV_BIN = "$(ENV_DIR)/bin"
ENV_PIP = "$(ENV_BIN)/pip"
ENV_PYTHON = "$(ENV_BIN)/python"

ENV_DIR_WHEEL = "$(ROOT_DIR)/envs/$(PROJECT_NAME_WHEEL)"
ENV_BIN_WHEEL = "$(ENV_DIR_WHEEL)/bin"
ENV_PIP_WHEEL = "$(ENV_BIN_WHEEL)/pip"
ENV_PYTHON_WHEEL = "$(ENV_BIN_WHEEL)/python"


create_dev_env:
	$(ROOT_CONDA) env create --force -f dev_environment.yml

create_wheel_env:
	$(ROOT_CONDA) env create --force -f wheel_environment.yml

run_experiment_wheel_3:
	$(ROOT_CONDA) env create --force -f wheel_environment.yml && \
	cd ../pylogging && \
	$(ENV_PIP_WHEEL) wheel . --wheel-dir=../$(PROJECT_NAME)/wheels && \
	cd ../common-python && \
	$(ENV_PIP_WHEEL) wheel . --wheel-dir=../$(PROJECT_NAME)/wheels && \
	cd ../shazam && \
	$(ENV_PIP_WHEEL) wheel . --wheel-dir=../$(PROJECT_NAME)/wheels && \
	cd ../$(PROJECT_NAME)/ && \
	$(ENV_PIP_WHEEL) wheel . --wheel-dir=../$(PROJECT_NAME)/wheels --find-links=../$(PROJECT_NAME)/wheels

run_experiment_3:    run_experiment_wheel_3
	$(ROOT_CONDA) env create --force -f wheel_environment.yml && \
	$(ENV_PIP_WHEEL) install --no-cache-dir --no-index --find-links=wheels/ $(PROJECT_NAME)

run_experiment_wheel_4:
	$(ROOT_CONDA) env create --force -f wheel_environment.yml && \
	cd ../pylogging && \
	$(ENV_PIP_WHEEL) wheel . --no-deps --wheel-dir=../$(PROJECT_NAME)/wheels && \
	cd ../common-python && \
	$(ENV_PIP_WHEEL) wheel . --no-deps --wheel-dir=../$(PROJECT_NAME)/wheels && \
	cd ../shazam && \
	$(ENV_PIP_WHEEL) wheel . --no-deps --wheel-dir=../$(PROJECT_NAME)/wheels && \
	cd ../$(PROJECT_NAME)/ && \
	$(ENV_PIP_WHEEL) wheel . --no-deps --wheel-dir=../$(PROJECT_NAME)/wheels

run_experiment_4:    run_experiment_wheel_4
	$(ROOT_CONDA) env create --force -f wheel_environment.yml && \
	$(ENV_PIP_WHEEL) install --no-cache-dir --find-links=wheels/ $(PROJECT_NAME)
