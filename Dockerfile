# Use the official Airflow image as the base
FROM apache/airflow:2.8.2-python3.9

# Switch to airflow user
USER airflow

# Install Spark Airflow provider and any other required packages
COPY airflow-requirements.txt .
RUN pip install --no-cache-dir -r airflow-requirements.txt

# Switch back to airflow user
USER airflow
