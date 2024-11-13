from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from generate_files import create_text_files
from count_incluedes import process_files
from summ import sum_results

def create_files():
    # Вызов функции для создания файлов
    create_text_files()

def count_a():
    # Вызов функции для подсчета 'a'
    process_files()

def sum_a():
    # Вызов функции для суммирования
    sum_results()

with DAG('text_processing', start_date=datetime(2024, 11, 13), schedule_interval=None) as dag:
    task1 = PythonOperator(
        task_id='create_files',
        python_callable=create_files
    )

    task2 = PythonOperator(
        task_id='count_a',
        python_callable=count_a
    )

    task3 = PythonOperator(
        task_id='sum_a',
        python_callable=sum_a
    )

    task1 >> task2 >> task3