"""
XCom DAG - DAG mẫu về chia sẻ data giữa các tasks với XCom
"""
from __future__ import annotations

import pendulum

from airflow.sdk import DAG, task

@dag(
    dag_id="xcom_example",
    schedule=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["xcom", "data-sharing"],
)
def xcom_dag():
    """
    ### XCom DAG
    DAG mẫu về cách chia sẻ data giữa các tasks sử dụng XCom.
    """
    
    @task
    def extract_data():
        """### Extract Data
        Extract data và return để chia sẻ với task khác
        """
        data = {
            "users": [
                {"id": 1, "name": "Alice", "age": 30},
                {"id": 2, "name": "Bob", "age": 25},
                {"id": 3, "name": "Charlie", "age": 35},
            ],
            "total": 3,
        }
        print(f"Extracted {data['total']} users")
        return data
    
    @task
    def process_data(data: dict):
        """### Process Data
        Nhận data từ extract_data và xử lý
        """
        users = data["users"]
        total_age = sum(user["age"] for user in users)
        avg_age = total_age / len(users)
        
        result = {
            "total_users": len(users),
            "total_age": total_age,
            "average_age": avg_age,
        }
        print(f"Processed data: {result}")
        return result
    
    @task
    def save_summary(summary: dict):
        """### Save Summary
        Nhận summary từ process_data và lưu
        """
        print(f"Saving summary: {summary}")
        print(f"Average age: {summary['average_age']:.2f}")
        return f"Summary saved: {summary['total_users']} users processed"
    
    # Định nghĩa dependencies với data passing
    extracted = extract_data()
    processed = process_data(extracted)
    save_summary(processed)

# Tạo DAG instance
xcom_dag()

