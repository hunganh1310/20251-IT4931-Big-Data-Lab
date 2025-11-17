# Docker Ports Summary - After Revert

## ✅ Standard Ports (Reverted)

Tất cả các labs đã được revert về standard ports vì các labs độc lập với nhau.

### PostgreSQL
| Lab | Port | Status |
|-----|------|--------|
| Airflow_lab | 5432 | ✅ Standard |
| dbt_lab | 5432 | ✅ Standard |
| Great_Expectations_lab | 5432 | ✅ Standard (reverted) |
| NoSQL_lab | 5432 | ✅ Standard |
| Spark_lab | 5432 | ✅ Standard |
| Data_Lakehouse_lab | 5432 | ✅ Standard |

### Redis
| Lab | Port | Status |
|-----|------|--------|
| Kafka_lab | 6379 | ✅ Standard |
| NoSQL_lab | 6379 | ✅ Standard |
| Spark_lab | 6379 | ✅ Standard |
| Data_Lakehouse_lab | 6379 | ✅ Standard |

### Kafka
| Lab | Port | Status |
|-----|------|--------|
| Kafka_lab | 9092 | ✅ Standard |
| Spark_lab | 9092 | ✅ Standard |
| Data_Lakehouse_lab | 9092 | ✅ Standard |

### Web UIs (Port 8080)
| Lab | Service | Port | Status |
|-----|---------|------|--------|
| Spark_lab | Spark Master | 8080 | ✅ Standard |
| Airflow_lab | Airflow Web | 8080 | ✅ Standard |
| Kafka_lab | AKHQ | 8080 | ✅ Standard |
| NoSQL_lab | Trino | 8080 | ✅ Standard |
| Data_Lakehouse_lab | Airflow Web | 8080 | ✅ Standard |

### Special Cases (Trong cùng lab)
| Lab | Service | Port | Reason |
|-----|---------|------|--------|
| Data_Lakehouse_lab | Spark Master | 8081 | ⚠️ Conflict với Airflow (8080) trong cùng lab |

**Note**: Data_Lakehouse_lab có Spark Master và Airflow trong cùng lab nên cần port khác nhau.

## 📊 Other Ports

### Schema Registry
- Kafka_lab: 8081
- Spark_lab: 8081

### Kafka Connect
- Kafka_lab: 8083

### Jupyter
- Spark_lab: 8888

### pgAdmin
- dbt_lab: 5050

### Redis Commander
- NoSQL_lab: 8081

### Neo4j
- NoSQL_lab: 7474 (HTTP), 7687 (Bolt)

### MongoDB
- NoSQL_lab: 27017

## ✅ Summary

- ✅ Tất cả ports đã được revert về standard values
- ✅ Chỉ giữ Spark Master ở Data_Lakehouse_lab là 8081 (tránh conflict trong cùng lab)
- ✅ Labs độc lập nên có thể dùng cùng ports
- ✅ Image versions đã được standardize
- ✅ Health checks và restart policies đã được cải thiện

