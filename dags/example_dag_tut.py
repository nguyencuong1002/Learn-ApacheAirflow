from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG(
   dag_id = 'example_dag',
   default_args={"start_date": "2019-10-01"}
)

part1 = BashOperator(
   task_id='generate_random_number',
   bash_command='echo $RANDOM',
   dag=dag
)