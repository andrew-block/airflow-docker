# Initialize airflow
start-db:
	@docker-compose up airflow-init
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

