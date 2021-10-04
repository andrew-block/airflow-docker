# Deploy Airflow 2+ with Docker 

<p align="center">
<img src="https://github.com/andrew-block/airflow-docker/blob/39b95511b57b2f857a153b479e3d884bd239f5c8/resources/airflow_docker.png" width="500" height="500" />
</p>

## Airflow Overview
[Apache Airflow](https://airflow.apache.org/) is a platform for programmatically authoring, scheduling, and monitoring workflows. It is completely open source and is especially useful in architecting and orchestrating complex data pipelines. Airflow was originally created to solve the issues that come with long-running cron tasks and hefty scripts, but it's since grown to become one of the most powerful open source data pipeline platforms out there.

Airflow has a couple of key benefits, namely:

* It's dynamic: Anything you can do in Python, you can do in Airflow.
* It's extensible: Airflow has readily available plugins for interacting with most common external systems. You can also create your own plugins as needed.
* It's scalable: Teams use Airflow to run thousands of different tasks per day.

With Airflow, workflows are architected and expressed as Directed Acyclic Graphs (DAGs), with each node of the DAG representing a specific task. Airflow is designed with the belief that all data pipelines are best expressed as code, and as such is a code-first platform where you can quickly iterate on workflows. This code-first design philosophy provides a degree of extensibility that other pipeline tools can't match.

<p align="center">
<img src="https://github.com/andrew-block/airflow-docker/blob/39b95511b57b2f857a153b479e3d884bd239f5c8/resources/airflow_principles.png" />
</p>

## Getting Started

This repository uses `Airflow 2.1.3` and `Python 3.8` but you can modify these to whatever versions you want my modifying the Dockerfile.
To run Airflow locally use the execute the following command:

        make start-airflow
