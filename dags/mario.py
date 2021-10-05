from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from Tools.pixel_mario import PixelMario


def get_mario():
    pm = PixelMario()
    pm.create_pixel_mario()


default_args = {
    "owner": "Airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 5, 11, 12, 0, 0),
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
    "backfill": False,
    "Catchup": False
}

dag = DAG(
    'mario',
    default_args=default_args,
    start_date=datetime(2020, 5, 11),
    catchup=False,
    schedule_interval='30 6 * * *'
)

task = PythonOperator(
    task_id='create_mario',
    python_callable=get_mario,
    provide_context=True,
    dag=dag)