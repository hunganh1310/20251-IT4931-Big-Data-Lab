# Docker Compose Optimization Analysis

## 📊 Image Version Analysis

### PostgreSQL Versions
| Lab | Version | Notes |
|-----|---------|-------|
| Airflow_lab | `postgres:15` | Full image |
| dbt_lab | `postgres:15-alpine` | ✅ Alpine (nhẹ hơn) |
| Great_Expectations_lab | `postgres:15-alpine` | ✅ Alpine |
| Data_Lakehouse_lab | `postgres:15-alpine` | ✅ Alpine |
| NoSQL_lab | `postgres:15` | Full image |
| Spark_lab | `postgres:15-alpine` | ✅ Alpine |

**Recommendation**: Standardize về `postgres:15-alpine` (tiết kiệm ~200MB/image)

### Redis Versions
| Lab | Version | Notes |
|-----|---------|-------|
| Kafka_lab | `redis:7.2-alpine` | ✅ Latest |
| Data_Lakehouse_lab | `redis:7-alpine` | Older version |
| NoSQL_lab | `redis:7.2-alpine` | ✅ Latest |
| Spark_lab | `redis:7-alpine` | Older version |

**Recommendation**: Standardize về `redis:7.2-alpine` (latest stable)

### Kafka Versions
| Lab | Version | Mode | Notes |
|-----|---------|------|-------|
| Kafka_lab | `confluentinc/cp-kafka:7.4.0` | KRaft | ✅ KRaft (no Zookeeper) |
| Data_Lakehouse_lab | `confluentinc/cp-kafka:7.5.0` | Zookeeper | Older pattern |
| Spark_lab | `confluentinc/cp-kafka:7.4.0` | KRaft | ✅ KRaft |

**Recommendation**: 
- Standardize về `confluentinc/cp-kafka:7.5.0` (latest)
- Prefer KRaft mode (no Zookeeper needed) cho labs mới

### Spark Versions
| Lab | Version | Notes |
|-----|---------|-------|
| Spark_lab | `bitnami/spark:3.5.0` | Specific version |
| Data_Lakehouse_lab | `bitnami/spark:3.5` | Tag without patch |

**Recommendation**: Standardize về `bitnami/spark:3.5.0` (specific version)

### Airflow Versions
| Lab | Version | Notes |
|-----|---------|-------|
| Airflow_lab | `apache/airflow:3.1.1` | ✅ Consistent |
| Data_Lakehouse_lab | `apache/airflow:3.1.1` | ✅ Consistent |

**Status**: ✅ Already consistent

## 🔧 Optimization Recommendations

### 1. Standardize Image Versions

#### PostgreSQL
- **Current**: Mix of `postgres:15` and `postgres:15-alpine`
- **Recommended**: `postgres:15-alpine` (all labs)
- **Savings**: ~200MB per container

#### Redis
- **Current**: Mix of `redis:7-alpine` and `redis:7.2-alpine`
- **Recommended**: `redis:7.2-alpine` (all labs)
- **Benefit**: Latest features và bug fixes

#### Kafka
- **Current**: Mix of `7.4.0` và `7.5.0`, KRaft và Zookeeper modes
- **Recommended**: `confluentinc/cp-kafka:7.5.0` với KRaft mode
- **Benefit**: No Zookeeper needed, simpler setup

#### Spark
- **Current**: `bitnami/spark:3.5.0` và `bitnami/spark:3.5`
- **Recommended**: `bitnami/spark:3.5.0` (specific version)
- **Benefit**: Reproducible builds

### 2. Remove Duplicate Services

#### PostgreSQL Instances
- **Issue**: Multiple PostgreSQL containers với different ports
- **Current**:
  - Airflow_lab: port 5432
  - dbt_lab: port 5432 (conflict!)
  - Great_Expectations_lab: port 5433 (avoid conflict)
  - Data_Lakehouse_lab: port 5432 (conflict!)
  - NoSQL_lab: port 5432 (conflict!)
  - Spark_lab: port 5432 (conflict!)

- **Recommendation**: 
  - Use different ports cho mỗi lab
  - Hoặc use external PostgreSQL service
  - Document port assignments

#### Redis Instances
- **Issue**: Multiple Redis containers
- **Current**: Kafka_lab, Data_Lakehouse_lab, NoSQL_lab, Spark_lab
- **Recommendation**: 
  - Labs có thể share Redis nếu không conflict
  - Hoặc use different ports

### 3. Resource Optimization

#### Health Checks
- **Status**: Most labs có health checks ✅
- **Missing**: Some services không có health checks
- **Recommendation**: Add health checks cho tất cả services

#### Restart Policies
- **Current**: Mix of `restart: always`, `restart: unless-stopped`
- **Recommendation**: `restart: unless-stopped` (cho labs)

#### Resource Limits
- **Missing**: No resource limits defined
- **Recommendation**: Add resource limits để tránh resource exhaustion

### 4. Network Optimization

- **Current**: Mỗi lab có network riêng
- **Status**: ✅ OK cho isolation
- **Note**: Labs không cần share networks (good practice)

## 📝 Action Items

### High Priority
1. ✅ Standardize PostgreSQL: `postgres:15-alpine`
2. ✅ Standardize Redis: `redis:7.2-alpine`
3. ✅ Standardize Kafka: `confluentinc/cp-kafka:7.5.0` với KRaft
4. ✅ Standardize Spark: `bitnami/spark:3.5.0`
5. ⚠️ Fix PostgreSQL port conflicts
6. ⚠️ Add health checks cho missing services

### Medium Priority
1. Add resource limits
2. Standardize restart policies
3. Document port assignments

### Low Priority
1. Consider shared services cho common dependencies
2. Add monitoring/logging

## 🎯 Expected Benefits

- **Disk Space**: ~500MB-1GB savings từ Alpine images
- **Consistency**: Easier maintenance và updates
- **Reliability**: Better health checks và restart policies
- **Developer Experience**: Clear port assignments, no conflicts

