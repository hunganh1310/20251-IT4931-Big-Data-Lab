# Docker Compose Issues Found

## 🔴 Critical Issues

### 1. Port Conflicts

#### PostgreSQL Port Conflicts
| Lab | Port | Status |
|-----|------|--------|
| Airflow_lab | 5432 | ⚠️ CONFLICT |
| dbt_lab | 5432 | ⚠️ CONFLICT |
| NoSQL_lab | 5432 | ⚠️ CONFLICT |
| Spark_lab | 5432 | ⚠️ CONFLICT |
| Great_Expectations_lab | 5433 | ✅ OK |
| Data_Lakehouse_lab | 5434 | ✅ OK |

**Fix Required**: Change ports for dbt_lab, NoSQL_lab, Spark_lab

#### Redis Port Conflicts
| Lab | Port | Status |
|-----|------|--------|
| Kafka_lab | 6379 | ⚠️ CONFLICT |
| NoSQL_lab | 6379 | ⚠️ CONFLICT |
| Spark_lab | 6379 | ⚠️ CONFLICT |
| Data_Lakehouse_lab | 6380 | ✅ OK |

**Fix Required**: Change ports for NoSQL_lab, Spark_lab

#### Kafka Port Conflicts
| Lab | Port | Status |
|-----|------|--------|
| Kafka_lab | 9092 | ⚠️ CONFLICT |
| Spark_lab | 9092 | ⚠️ CONFLICT |
| Data_Lakehouse_lab | 9092 | ⚠️ CONFLICT |

**Fix Required**: Change ports for Spark_lab, Data_Lakehouse_lab

#### Port 8080 Conflicts (Web UIs)
| Lab | Service | Port | Status |
|-----|---------|------|--------|
| Spark_lab | Spark Master | 8080 | ⚠️ CONFLICT |
| Airflow_lab | Airflow Web | 8080 | ⚠️ CONFLICT |
| Kafka_lab | AKHQ | 8080 | ⚠️ CONFLICT |
| NoSQL_lab | Trino | 8080 | ⚠️ CONFLICT |
| Data_Lakehouse_lab | Airflow Web | 8080 | ⚠️ CONFLICT |

**Fix Required**: Assign unique ports

### 2. Kafka Version Inconsistency
- Kafka_lab: `confluentinc/cp-kafka:7.4.0`
- Spark_lab: `confluentinc/cp-kafka:7.4.0`
- Data_Lakehouse_lab: `confluentinc/cp-kafka:7.5.0`

**Fix Required**: Standardize to 7.5.0

## 🟡 Medium Priority Issues

### 3. Missing Health Checks
- dbt_lab: pgadmin không có healthcheck
- Spark_lab: Một số services thiếu healthcheck
- Kafka_lab: schema-registry, kafka-connect thiếu healthcheck

### 4. Restart Policy Inconsistency
- Airflow_lab: Dùng `restart: always` (khác với các labs khác)
- Một số services thiếu restart policy

### 5. Missing Restart Policies
- dbt_lab: pgadmin thiếu restart policy
- Spark_lab: Một số services thiếu restart policy

## 🟢 Low Priority Issues

### 6. Schema Registry Version
- Kafka_lab: `confluentinc/cp-schema-registry:7.4.0`
- Spark_lab: `confluentinc/cp-schema-registry:7.4.0`
- Should match Kafka version (7.5.0)

### 7. Missing Depends_on Conditions
- Một số services dùng `depends_on` đơn giản thay vì `condition: service_healthy`

