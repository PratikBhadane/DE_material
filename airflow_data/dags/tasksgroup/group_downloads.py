from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def download_tasks():

    with TaskGroup("downloads", tooltip="Download tasks") as group:

        downaload_a = BashOperator(
            task_id='downaload_a',
            bash_command='sleep 10'
        )

        downaload_b = BashOperator(
            task_id='downaload_b',
            bash_command='sleep 10'
        )

        downaload_c = BashOperator(
            task_id='downaload_c',
            bash_command='sleep 10'
        )
        return group