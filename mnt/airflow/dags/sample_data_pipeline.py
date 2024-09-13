from airflow import DAG
from airflow.operators.email import EmailOperator

from datetime import datetime, timedelta

import csv
import requests
import json

default_args = {
    'owner' : 'airflow',
    'email_on_failure' : False,
    'email_on_try' : False,
    'email' : 'admin@localhost.com',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5)
}

def _get_message() -> str:
    return 'Hi from sample_data_pipeline'

with DAG('sample_data_pipeline', start_date=datetime(2021, 1, 1), 
         schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    send_email_notification = EmailOperator(
        task_id='send_email_notification',
        to='airflow_test@yopmail.com',
        subject='This is a sample_data_pipeline',
        html_content='<h3>sample_data_pipeline 2</h3>'
    )

    send_email_notification
