from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.docker.operators.docker import DockerOperator

from dags_config import DEFAULT_DAG_ARGS, LOCAL_DATA_PATH


with DAG(
        dag_id="data_generator",
        default_args=DEFAULT_DAG_ARGS,
        schedule_interval="@daily",
        start_date=days_ago(7)
) as dag:
    OUTPUT_DIR = "/data/raw/{{ ds }}"
    data_generator = DockerOperator(
        task_id="data_generator",
        image="airflow-download",
        command=f"{OUTPUT_DIR}",
        volumes=[f"{LOCAL_DATA_PATH}:/data"],
        auto_remove=True,
    )

    data_generator
