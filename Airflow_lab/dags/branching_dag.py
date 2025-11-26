"""
Branching DAG - DAG với conditional branching logic
"""
from __future__ import annotations

import pendulum

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.empty import EmptyOperator

@dag(
    dag_id="branching_example",
    schedule="@daily",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["branching", "example"],
)
def branching_dag():
    """
    ### Branching DAG
    DAG mẫu với conditional branching để học cách xử lý logic điều kiện.
    """
    
    start = EmptyOperator(task_id="start")
    
    @task.branch
    def check_condition(**context):
        """### Check Condition
        Branch dựa trên điều kiện (ví dụ: ngày trong tuần)
        """
        # Lấy execution date từ context
        execution_date = context["data_interval_start"]
        day_of_week = execution_date.weekday()
        
        # Nếu là thứ 2 (0) hoặc thứ 6 (4), chạy cả 2 branches
        if day_of_week == 0 or day_of_week == 4:
            return ["branch_a", "branch_b"]
        # Nếu là cuối tuần, chỉ chạy branch_a
        elif day_of_week >= 5:
            return "branch_a"
        # Ngày thường chỉ chạy branch_b
        else:
            return "branch_b"
    
    branching = check_condition()
    
    branch_a = EmptyOperator(task_id="branch_a")
    branch_b = EmptyOperator(task_id="branch_b")
    
    # Join task - chạy sau khi cả 2 branches hoàn thành
    join = EmptyOperator(
        task_id="join",
        trigger_rule="none_failed_min_one_success",  # Chạy nếu ít nhất 1 branch thành công
    )
    
    end = EmptyOperator(task_id="end")
    
    # Định nghĩa dependencies
    start >> branching
    branching >> branch_a >> join
    branching >> branch_b >> join
    join >> end

# Tạo DAG instance
branching_dag()

