AIRFLOW_VERSION=2.1.3
AIRFLOW_EXTRAS := postgres,redis,mysql

# Recreates your virtualenv from scratch, assuming you have python3 installed
.PHONY: venv
venv:
ifneq ($(wildcard ./venv/.*),)
	@echo "venv already exists"
else
	python3 -m pip install --user virtualenv
	python3 -m virtualenv venv
	venv/bin/python3 -m pip install --upgrade pip
	venv/bin/python3 -m pip install --trusted-host pypi.python.org "apache-airflow[${AIRFLOW_EXTRAS}]==${AIRFLOW_VERSION}" --use-deprecated legacy-resolver
	venv/bin/python3 -m pip install -r local.requirements.txt --use-deprecated legacy-resolver
endif

# Lint all python files
.PHONY: lint
lint: venv
	venv/bin/python3 -m black dags plugins tests --check
	venv/bin/python3 -m pylint dags --load-plugins=pylint_airflow
	venv/bin/python3 -m pylint dags/modules --load-plugins=pylint_airflow
	venv/bin/python3 -m pylint plugins
	venv/bin/python3 -m pylint tests

lint-docker:
	@docker-compose up lint

# Run all tests
.PHONY: test
test: venv
	@( \
		export AIRFLOW_HOME=${PWD}; \
		source venv/bin/activate; \
		pytest tests --log-cli-level=info --disable-warnings; \
	)

test-docker:
	@docker-compose up test

# Get rid of junk from running pytest locally
clean-pytest:
	rm -rf *.cfg airflow.db logs .pytest_cache

# Clean virtualenv, run make venv to recreate it
clean-venv:
	rm -rf venv plugins.egg-info

# Initialize airflow
start-db:
	@docker-compose up  airflow-init
	@docker-compose up

# Start airflow worker
start-airflow: start-db
	@docker-compose run airflow-worker

# Stops Airflow
stop-airflow:
	@docker-compose down

# Rebuild the local Airflow image for docker-compose (useful if you make changes to the Dockerfile)
rebuild-airflow:
	@docker-compose build

# Resets local Airflow, removes all docker volumes and stopped containers
reset-airflow:
	@docker-compose down -v || true
	@docker-compose rm -f
	rm -f webserver_config.py

# Cleans everything
clean-all: clean-pytest clean-venv reset-airflow

### DO NOT RUN THESE STEPS BY HAND
### The below steps are used inside the Dockerfile and/or docker-compose, they are not meant to be run locally
internal-install-deps:
	pip install -r requirements.txt --use-deprecated legacy-resolver

internal-install-local-deps:
	pip install -r local.requirements.txt --use-deprecated legacy-resolver

internal-test: internal-install-local-deps
	pytest tests --log-cli-level=info --disable-warnings

internal-lint: internal-install-local-deps
	black dags plugins tests --check
	pylint dags --load-plugins=pylint_airflow
	pylint dags/modules --load-plugins=pylint_airflow
	pylint plugins
	pylint tests