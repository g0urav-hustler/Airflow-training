from datetime import timedelta, datetime
from airflow import DAG


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 25),
    'email': ["myemail@gmail.com"],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG("weather_dag",
        default_args = default_args,
        schedule_interval = "@daily",
        catchup = False) as dag:
