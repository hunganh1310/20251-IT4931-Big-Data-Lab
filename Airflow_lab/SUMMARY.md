# Airflow Lab - Summary

## 🎉 Airflow Lab đã được tạo thành công!

### 📁 Cấu trúc thư mục:
```
Airflow_lab/
├── docker-compose.yml          # Airflow 3.1.1 với PostgreSQL
├── requirements.txt            # Python dependencies
├── setup_airflow_lab.sh       # Setup script
├── README.md                  # Hướng dẫn chi tiết
├── SUMMARY.md                 # File này
├── dags/                      # DAGs mẫu
│   ├── hello_world_dag.py
│   ├── tutorial_dag.py
│   ├── branching_dag.py
│   └── xcom_dag.py
├── notebooks/                 # Jupyter notebooks
│   └── 01_airflow_basics.ipynb
├── logs/                      # Airflow logs
├── plugins/                   # Custom plugins
├── config/                    # Airflow config
└── data/                      # Sample data
```

### 🚀 Cách sử dụng:

#### 1. Setup Environment:
```bash
cd Airflow_lab
./setup_airflow_lab.sh
```

#### 2. Initialize Airflow:
```bash
# Set AIRFLOW_UID
export AIRFLOW_UID=$(id -u)
echo "AIRFLOW_UID=$AIRFLOW_UID" > .env

# Initialize database
docker compose up airflow-init
```

#### 3. Start Airflow Services:
```bash
docker compose up -d
```

#### 4. Access Airflow UI:
- **URL**: http://localhost:8080
- **Username**: airflow
- **Password**: airflow

#### 5. Start Jupyter Lab:
```bash
conda activate datalab
jupyter lab
```

#### 6. Run Labs:
- Mở `notebooks/01_airflow_basics.ipynb`
- Chạy từng cell để học Airflow fundamentals

### 🌐 Web UIs:
- **Airflow UI**: http://localhost:8080
- **PostgreSQL**: localhost:5432 (airflow/airflow)

### 📊 Lab Content:

#### **Lab 1: Airflow Basics** ✅
- Kiến trúc Airflow
- Web UI và CLI
- REST API
- Trigger và monitor DAGs

#### **Lab 2: DAGs và Tasks** (Coming soon)
- Task SDK (@dag, @task decorators)
- Task dependencies
- Error handling

#### **Lab 3: Operators và Hooks** (Coming soon)
- BashOperator, PythonOperator
- SQLExecuteQueryOperator
- Custom operators

#### **Lab 4: Task Dependencies và Branching** (Coming soon)
- Bitshift operators
- BranchPythonOperator
- Trigger rules

#### **Lab 5: XCom và Data Sharing** (Coming soon)
- XCom push/pull
- Task return values
- Data passing

#### **Lab 6: Scheduling và Timetables** (Coming soon)
- Cron expressions
- Custom timetables
- Catchup và data intervals

#### **Lab 7: End-to-End Pipeline** (Coming soon)
- Kafka integration
- Spark integration
- Database operations

### 🎯 Learning Outcomes:
Sau khi hoàn thành lab series này, sinh viên sẽ có thể:

1. **Airflow Fundamentals**: Hiểu kiến trúc và components
2. **DAG Development**: Tạo DAGs với Task SDK
3. **Operators & Hooks**: Sử dụng và tạo custom operators
4. **Data Management**: Chia sẻ data với XCom
5. **Scheduling**: Cấu hình scheduling phức tạp
6. **Pipeline Integration**: Tích hợp với các hệ thống khác

### 🔧 Tech Stack:
- **Apache Airflow**: 3.1.1 (latest stable)
- **PostgreSQL**: Metadata database
- **Docker Compose**: Containerized environment
- **Python**: Task SDK, operators, hooks
- **Jupyter**: Interactive learning

### 📈 Use Case: E-commerce Data Pipeline
- **Data Sources**: Kafka streams, databases
- **Processing**: Spark transformations
- **Destination**: Data warehouse, analytics
- **Orchestration**: Airflow workflows

### 🔗 Integration với Labs Khác:
- **Kafka Lab**: Stream data ingestion
- **Spark Lab**: Data processing
- **NoSQL Lab**: Database operations
- **PyIceberg Lab**: Data lake operations

---

**Airflow Lab đã sẵn sàng để sử dụng! 🚀**

