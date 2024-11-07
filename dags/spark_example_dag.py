from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta
import os

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'spark_job_dag',
    default_args=default_args,
    description='A simple DAG to run a Spark job',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    spark_submit = SparkSubmitOperator(
        task_id='spark_submit_task',
        application='/opt/airflow/spark/spark_job.py',
        conn_id='spark_default',
        executor_memory='2g',
        total_executor_cores=2,
        name='airflow-spark-job',
        verbose=True,
        conf={
            "spark.master": "spark://spark-master:7077"
        },
        # Set additional Spark configurations if needed
    )

    spark_submit
