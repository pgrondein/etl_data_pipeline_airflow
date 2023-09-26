# import the libraries
from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator

# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
		'owner': ' P Grondein',
		'start_date': days_ago(0),
		'email': ['pg@gmail.com'],
}

# define the DAG
dag = DAG(
    dag_id = 'process_web_log',
    default_args = default_args,
    description = 'Apache Airflow Capstone project',
    schedule_interval = timedelta(days = 1),
)

# Create a task to extract data
extract_data = BashOperator(
    task_id = 'extract_data',
    bash_command = 'cut -d " " -f1 --output-delimiter=" " /home/project/airflow/dags/capstone/accesslog.txt > extracted_data.txt',
    dag = dag,
)

# define the transform task
transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = 'grep "198.46.149.143" /home/project/airflow/dags/capstone/accesslog.txt > transformed_data.txt',
    dag = dag,
)

# define the load task
load_data = BashOperator(
    task_id = 'load_data',
    bash_command ='tar -czvf weblog.tar /home/project/airflow/dags/capstone/transformed_data.txt',
    dag = dag,
)

# task pipeline
extract_data >> transform_data >> load_data
