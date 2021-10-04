FROM apache/airflow:2.1.3-python3.8

# This is what airflow sets as default in the above `apache/airflow` image
ENV AIRFLOW_HOME /home/airflow

# Set user back airflow
USER airflow

# Set working dir to airflow home
WORKDIR ${AIRFLOW_HOME}

COPY requirements.txt .

# Only install project requirements, Airflow requirements are already installed in base image
RUN pip install -r requirements.txt

COPY ./dags/ ${AIRFLOW_HOME}/dags/