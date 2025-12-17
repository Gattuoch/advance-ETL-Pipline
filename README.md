# End-to-End Advanced ETL Data Pipeline

## Project Overview

This project implements an **end-to-end advanced ETL (Extract, Transform, Load) data pipeline** designed to process large-scale datasets using distributed computing and modern analytics tools. The objective is to ingest data from multiple heterogeneous sources, transform it efficiently using **Apache PySpark**, store analytical outputs in **DuckDB**, and expose insights through an interactive **BI dashboard**.

The pipeline is fully orchestrated using **Apache Airflow**, ensuring reliability, scalability, and scheduled execution. This implementation satisfies all core and bonus requirements of the assignment.

---

## Business Problem

Organizations often collect data from multiple formats and sources (CSV, Parquet, APIs), making analytics difficult without a unified processing and storage layer. This project demonstrates how to:

* Integrate multiple raw data sources
* Perform scalable transformations on large datasets
* Store analytics-ready data in a high-performance analytical database
* Deliver actionable insights through BI dashboards

---

## Architecture

**Pipeline Flow:**

```
Data Sources (CSV / Parquet / API)
        ↓
Apache PySpark (Distributed Transformations)
        ↓
DuckDB (Analytical Data Warehouse)
        ↓
BI Tool (Tableau / Power BI)
```

**Orchestration:** Apache Airflow schedules and monitors each pipeline stage.

---

## Data Sources

This project integrates **three distinct data sources**, including at least one Parquet file:

1. **Climate CSV Data** – Historical climate measurements
2. **Parquet Dataset** – Structured columnar dataset for efficient reads
3. **Weather API (JSON)** – Near real-time weather data ingestion

---

## Technologies Used

* **Apache PySpark** – Distributed data transformation and aggregation
* **DuckDB** – High-performance analytical database
* **Apache Airflow** – Workflow orchestration and scheduling
* **Python** – Data extraction, validation, and loading
* **Docker** – Containerized development and execution
* **BI Tool (Tableau / Power BI)** – Interactive dashboards and reporting

---

## ETL Pipeline Stages

### 1. Extract

* Read CSV files using Spark
* Load Parquet datasets using Spark
* Fetch JSON data from a weather API

### 2. Transform (PySpark)

* Data cleaning and schema normalization
* Time-based aggregations (yearly/monthly)
* Analytical transformations (averages, trends, rankings)

### 3. Load

* Persist transformed datasets into **DuckDB** tables
* Overwrite or append modes supported for analytical use cases

---

## Orchestration (Bonus Requirement)

The pipeline is orchestrated using **Apache Airflow**:

* DAGs manage extraction, transformation, and loading tasks
* Supports retries, logging, and scheduling
* Pipeline is scheduled to run automatically (e.g., daily or weekly)

---

## Project Structure

```
etl-datasets/
│
├── .astro/                         # Astro CLI configuration
│   └── config.yaml
│
├── .devcontainer/                  # Dev container setup
│   ├── devcontainer.json
│   └── post_create_script.sh
│
├── dags/                           # Airflow DAGs (orchestration layer)
│   ├── example_dag.py
│   ├── extract_current_weather_data.py
│   ├── extract_historical_weather_data.py
│   ├── extract_parquet_data.py
│   ├── transform_climate_data.py
│   ├── transform_historical_weather.py
│   ├── transform_climate_spark.py
│   └── start.py
│
├── include/                        # Shared utilities & configuration
│   ├── global_variables/
│   │   ├── airflow_conf_variables.py
│   │   ├── constants.py
│   │   └── user_input_variables.py
│   ├── meteorology_utils.py
│   └── plugins/
│
├── spark/                          # PySpark distributed transformations
│   ├── transform_climate_spark.py
│   └── transform_historical_weather_spark.py
│
├── data/                           # Raw & intermediate datasets
│   ├── climate_data/
│   │   ├── climate.csv
│   │   └── historical_weather.parquet
│   └── processed/
│       └── transformed_data.parquet
│
├── dbt/                            # (Bonus) dbt models for DuckDB
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   └── tests/
│
├── bi/                             # BI dashboard outputs
│   ├── BI_Dashboard_1.png
│   ├── BI_Dashboard_2.png
│   └── BI_Dashboard_3.png
│
├── tests/                          # Unit & data quality tests
│   └── test_data_integrity.py
│
├── docker-compose.override.yml     # Local Airflow services override
├── requirements.txt                # Python dependencies
├── profiles.yml                    # dbt DuckDB profile
├── README.md                       # Project documentation
└── .gitignore

```

---

## How to Run the Project

### Prerequisites

* Docker & Docker Compose
* Python 3.9+

### Steps

```bash
# Start Airflow and services
astro dev start

# Access Airflow UI
http://localhost:8080

# Trigger DAG manually or wait for schedule
```

DuckDB database is generated automatically during pipeline execution.

---
## BI Dashboard

DuckDB serves as the analytics backend for the BI layer.  
The transformed datasets are queried directly to generate insights such as trends,
aggregations, and performance metrics.

📊 **Dashboard Screenshots**

### Dashboard 1
![Dashboard 1](bi/BI_Dashboard_1.png)

### Dashboard 2
![Dashboard 2](bi/BI_Dashboard_2.png)

### Dashboard 3
![Dashboard 3](bi/BI_Dashboard_3.png)

## Assignment Requirements Mapping

| Requirement             | Status      |
| ----------------------- | ----------- |
| ≥ 3 Data Sources        | ✅           |
| Parquet Input           | ✅           |
| PySpark Transformations | ✅           |
| DuckDB Storage          | ✅           |
| Orchestration Tool      | ✅ (Airflow) |
| BI Dashboard            | ✅           |
| Scalable Architecture   | ✅           |

---

## Team Members & Contributions

* **Gattuoch Chambang     1401298 1** – Pipeline architecture & Airflow DAGs
* **Danial  Baye 1401105 2** – PySpark transformations & data modeling
* **Abdihakiim   Mohamed 368713 3** – DuckDB integration & BI dashboard

---

## Conclusion

This project demonstrates a production-style analytics pipeline using modern data engineering tools. It highlights best practices in scalable data processing, orchestration, and analytics delivery, fully aligned with the assignment requirements.

---

✅ **Repository is public and submission-ready**
# advance-ETL-Pipline
