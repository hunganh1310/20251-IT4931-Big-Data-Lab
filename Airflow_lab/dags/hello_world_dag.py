"""
Hello World DAG - DAG đơn giản nhất để làm quen với Airflow
"""
from __future__ import annotations

import pendulum

from airflow.sdk import DAG, task

# Định nghĩa DAG với @dag decorator
@dag(
    dag_id="hello_world",
    schedule=None,  # Manual trigger only
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial", "hello-world"],
)
def hello_world_dag():
    """
    ### Hello World DAG
    DAG đơn giản nhất với một task duy nhất.
    """
    
    @task
    def hello_task():
        """### Hello Task
        Task đơn giản in ra "Hello World!"
        """
        print("Hello World!")
        print("Chào mừng đến với Apache Airflow!")
        return "Hello World completed successfully!"
    
    # Gọi task để thêm vào DAG
    hello_task()

# Tạo DAG instance
hello_world_dag()

