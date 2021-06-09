LOCAL_DATA_PATH = '/Users/stepdan23/made/airflow_data'
DEFAULT_DAG_ARGS = {
    "owner": "airflow",
    "retries": 0,
    "email": ["admin@example.com"],
    "email_on_failure": True,
    "email_on_retry": True,
}
