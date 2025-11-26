# Airflow Lab - Data Pipeline Orchestration với Apache Airflow

## 🎯 Overview

Lab này cung cấp kiến thức thực hành về **Apache Airflow 3.1.1** - công cụ orchestration hàng đầu cho data pipelines. Sinh viên sẽ học cách thiết kế, lập lịch và giám sát các workflow phức tạp trong thực tế.

## 📚 Lab Structure

### **Lab 1: Airflow Basics**
- **Focus**: Giới thiệu Airflow, cài đặt và cấu hình
- **Skills**: Hiểu kiến trúc Airflow, Web UI, CLI commands
- **Use Case**: Setup môi trường và chạy DAG đầu tiên

### **Lab 2: DAGs và Tasks**
- **Focus**: Tạo DAGs với Task SDK (@dag, @task decorators)
- **Skills**: Định nghĩa workflows, tasks, dependencies
- **Use Case**: ETL pipeline đơn giản với Python tasks

### **Lab 3: Operators và Hooks**
- **Focus**: Sử dụng các operators phổ biến (Bash, Python, SQL)
- **Skills**: BashOperator, PythonOperator, SQLExecuteQueryOperator
- **Use Case**: Data extraction và transformation với nhiều loại operators

### **Lab 4: Task Dependencies và Branching**
- **Focus**: Quản lý dependencies, branching logic, trigger rules
- **Skills**: Bitshift operators (>>, <<), BranchPythonOperator
- **Use Case**: Conditional workflows và error handling

### **Lab 5: XCom và Data Sharing**
- **Focus**: Chia sẻ dữ liệu giữa các tasks với XCom
- **Skills**: Task return values, XCom push/pull, custom XCom backends
- **Use Case**: Data pipeline với data passing giữa tasks

### **Lab 6: Scheduling và Timetables**
- **Focus**: Lập lịch DAGs với cron, timedelta, custom timetables
- **Skills**: Schedule intervals, catchup, data intervals
- **Use Case**: Daily, hourly, và custom scheduling patterns

### **Lab 7: End-to-End Pipeline Integration**
- **Focus**: Tích hợp Airflow với Kafka, Spark, Databases
- **Skills**: Multi-service orchestration, monitoring, error recovery
- **Use Case**: Complete data pipeline từ source → processing → destination

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Install dependencies
./setup_airflow_lab.sh

# Set AIRFLOW_UID (Linux/Mac)
export AIRFLOW_UID=$(id -u)
echo "AIRFLOW_UID=$AIRFLOW_UID" > .env

# Or set manually (Windows)
echo "AIRFLOW_UID=50000" > .env
```

### 2. Initialize Airflow Database
```bash
# Initialize database and create admin user
docker compose up airflow-init

# Wait for initialization to complete
```

### 3. Start Airflow Services
```bash
# Start all services
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f airflow-webserver
```

### 4. Access Airflow UI
- **URL**: http://localhost:8080
- **Username**: `airflow`
- **Password**: `airflow`

### 5. Start Jupyter Lab
```bash
# Activate conda environment
conda activate datalab

# Start Jupyter Lab
jupyter lab
```

### 6. Run Labs
Mở notebooks theo thứ tự:
1. `notebooks/01_airflow_basics.ipynb`
2. `notebooks/02_dags_and_tasks.ipynb`
3. `notebooks/03_operators_and_hooks.ipynb`
4. `notebooks/04_task_dependencies.ipynb`
5. `notebooks/05_xcom_data_sharing.ipynb`
6. `notebooks/06_scheduling_timetables.ipynb`
7. `notebooks/07_end_to_end_pipeline.ipynb`

## 🏗️ Architecture

### **Services Included:**
- **Airflow Webserver (API Server)**: Port 8080 (Web UI và REST API)
- **Airflow Scheduler**: Lập lịch và trigger DAGs
- **Airflow DAG Processor**: Parse và load DAGs
- **Airflow Triggerer**: Xử lý deferrable operators
- **PostgreSQL**: Port 5432 (Metadata database)

### **Components:**
- **DAGs**: Workflow definitions trong `dags/`
- **Plugins**: Custom operators/hooks trong `plugins/`
- **Logs**: Task execution logs trong `logs/`
- **Config**: Airflow configuration trong `config/`

### **Data Flow:**
```
Source Data → Airflow DAG → Task 1 → Task 2 → ... → Destination
                ↓
            Scheduler monitors
                ↓
            Web UI displays
```

## 📊 Sample DAGs

### **Basic DAGs:**
- `hello_world_dag.py`: DAG đơn giản nhất
- `tutorial_dag.py`: DAG tutorial với nhiều tasks
- `etl_pipeline_dag.py`: ETL pipeline mẫu

### **Advanced DAGs:**
- `branching_dag.py`: Conditional branching
- `dynamic_dag.py`: Dynamic task generation
- `xcom_dag.py`: Data sharing với XCom
- `scheduled_dag.py`: Custom scheduling

### **Integration DAGs:**
- `kafka_spark_dag.py`: Kafka → Spark → Database
- `data_quality_dag.py`: Data validation pipeline
- `ml_pipeline_dag.py`: Machine learning pipeline

## 🔧 Configuration

### **Environment Variables:**
```bash
# Airflow UID (set in .env)
AIRFLOW_UID=50000

# Admin user (optional)
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow
```

### **Airflow Configuration:**
- Executor: `LocalExecutor` (single machine)
- Database: PostgreSQL
- Load Examples: `false` (clean environment)
- DAGs Paused at Creation: `true`

## 🐛 Troubleshooting

### **Common Issues:**

1. **Airflow won't start:**
   ```bash
   # Check logs
   docker compose logs airflow-webserver
   docker compose logs airflow-scheduler
   
   # Restart services
   docker compose restart
   ```

2. **Permission errors:**
   ```bash
   # Set correct AIRFLOW_UID
   export AIRFLOW_UID=$(id -u)
   echo "AIRFLOW_UID=$AIRFLOW_UID" > .env
   
   # Fix permissions
   sudo chown -R $AIRFLOW_UID:0 dags logs plugins config
   ```

3. **DAGs not appearing:**
   ```bash
   # Check DAG processor logs
   docker compose logs airflow-dag-processor
   
   # Test DAG parsing
   docker compose run airflow-cli airflow dags list
   ```

4. **Database connection errors:**
   ```bash
   # Check PostgreSQL health
   docker compose ps postgres
   
   # Restart database
   docker compose restart postgres
   ```

### **Performance Tuning:**
- Increase Docker memory allocation (minimum 4GB)
- Adjust scheduler settings in `config/airflow.cfg`
- Use appropriate executor for your use case

## 📚 Learning Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/3.1.1/)
- [Airflow Task SDK](https://airflow.apache.org/docs/apache-airflow/3.1.1/task-sdk/index.html)
- [Airflow Concepts](https://airflow.apache.org/docs/apache-airflow/3.1.1/core-concepts/index.html)
- [Airflow Best Practices](https://airflow.apache.org/docs/apache-airflow/3.1.1/best-practices/index.html)

## 🎯 Learning Outcomes

Sau khi hoàn thành lab series này, sinh viên sẽ có thể:

1. **Airflow Fundamentals**:
   - Hiểu kiến trúc và components của Airflow
   - Sử dụng Web UI và CLI để quản lý DAGs
   - Cài đặt và cấu hình Airflow environment

2. **DAG Development**:
   - Tạo DAGs với Task SDK (@dag, @task decorators)
   - Định nghĩa task dependencies và workflows
   - Implement branching và conditional logic

3. **Operators & Hooks**:
   - Sử dụng các operators phổ biến
   - Tạo custom operators và hooks
   - Integrate với external systems

4. **Data Management**:
   - Chia sẻ data giữa tasks với XCom
   - Handle data passing trong pipelines
   - Implement data validation

5. **Scheduling**:
   - Cấu hình scheduling với cron và timetables
   - Hiểu catchup và data intervals
   - Implement custom scheduling logic

6. **Pipeline Integration**:
   - Tích hợp Airflow với Kafka, Spark, Databases
   - Build end-to-end data pipelines
   - Monitor và troubleshoot pipelines

## 📋 Assessment Criteria

### **Beginner Level**:
- Hoàn thành Lab 1 và 2
- Hiểu basic concepts của Airflow
- Tạo được DAG đơn giản

### **Intermediate Level**:
- Hoàn thành Labs 1-5
- Hiểu operators, dependencies, XCom
- Implement được branching logic

### **Advanced Level**:
- Hoàn thành tất cả labs
- Build được end-to-end pipeline
- Tích hợp với multiple systems
- Optimize performance và reliability

## 🔗 Integration với Labs Khác

Lab này tích hợp với:
- **Kafka Lab**: Stream data ingestion
- **Spark Lab**: Data processing
- **NoSQL Lab**: Database operations
- **PyIceberg Lab**: Data lake operations

## 🎉 Next Steps

Sau khi hoàn thành Airflow Lab, bạn có thể:
1. Tích hợp với dbt Lab (transformation)
2. Thêm Data Quality Lab (Great Expectations)
3. Implement CI/CD cho data pipelines
4. Deploy lên production environment

---

**Happy Orchestrating! 🚀**

