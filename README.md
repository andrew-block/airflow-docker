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

This repository uses `Airflow 2.1.3` and `Python 3.8` but you can modify these to whatever versions you want my modifying the Dockerfile 🐳.

### Start Airflow

To run Airflow locally use the execute the following command:

        make start-airflow
        
After the `webserver` service starts, you can login to the Airflow UI by going to http://localhost:8080/

You can also look at the `flower` worker/s UI by going to http://localhost:5555/

### Stop Airflow

To stop Airflow at anytime you can execute the following command:

        make stop-airflow
        
### Rebuild Airflow 

If you make any changes to the Dockerfile you can rebuild the Airflow image by executing the following command:

        make rebuild-airflow

### Reset Airflow

If you want to reset your local Airflow you can execute the following command:

        make reset-airflow
        
## Airflow UI

To run the `DAG` you toggle the button to the right which will turn blue to indicate your `mario` DAG has started. A successfull DAG run will show up as a green circle in the `Runs` section and the number inside that circle indicates how many runs you have processed. 

<p align="center">
<img src="https://github.com/andrew-block/airflow-docker/blob/0974a551a58c42cd593cb8f61a6a1f68b392643b/resources/airflow_ui.png" />
</p>

If the DAG run was succesfull ✅ you should see `pixel_mario` image created in your mario folder such as:

<p align="center">
<img src="https://github.com/andrew-block/airflow-docker/blob/0da2e7b327bf65463f07ad444049d428b5426e24/mario/pixel_mario_%23579841.png" width="400" height=400" />
</p>

