# airflow-spark-postgres-redis-playground

A Docker Compose environment to run Airflow, Spark, Postgres, and Redis to play with.

## Project Overview

This project sets up a development environment using Docker Compose to run the following services:

### Airflow

Apache Airflow is a workflow orchestration platform that allows you to programmatically schedule, monitor, and manage
complex sequences of data pipelines and tasks through code-based DAGs (Directed Acyclic Graphs). It helps coordinate
dependencies between different data processes and services.

### Spark

Apache Spark is a distributed data processing engine designed for large-scale data analytics and machine learning,
enabling fast parallel computation across clusters through in-memory processing and optimized query execution. It
excels at both batch and stream processing workloads.

### Postgres

A powerful, open-source object-relational database system.

### Redis

An in-memory data structure store, used as a database, cache, and message broker.

## Prerequisites

Ensure you have the following installed on your machine:

- Docker
- Docker Compose

## Setup Instructions

### Clone the repository

```sh
  git clone https://github.com/yourusername/airflow-spark-postgres-redis-playground.git
  cd airflow-spark-postgres-redis-playground
```

### Generate a FERNET key

Copy the output of this

```sh
  openssl rand -base64 32
```

### Create a `.env` file

Copy the `.env.example` file to `.env` and adjust any passwords accordingly. The one you need to change forsure will be
to add a FERNET key from the previous step.

Edit the `.env` and change the following line:

```dotenv
  AIRFLOW__CORE__FERNET_KEY='VALUE FROM THE PREVIOUS STEP GOES IN HERE'
```

### Build and start the services

Run the following command to build and start all the services defined in the `docker-compose.yml` file:

```sh
  docker-compose up --build
```

## Access the services

* Airflow Web UI [http://localhost:8081](http://localhost:8081)
* Spark Master UI [http://localhost:8080](http://localhost:8080)
* Postgres: Accessible on port `5432`
* Redis: Accessible on port `6379`

## Usage

- Airflow: Use the Airflow web UI to create and manage your workflows.
- Spark: Submit Spark jobs to the Spark master.
- Postgres: Connect to the Postgres database using the credentials provided in the `.env` file.
- Redis: Use Redis as a message broker and result backend for Airflow.

## Stopping the Services

To stop the services, run:

```sh
docker-compose down
```

## Cleaning Up

To remove all containers, networks, and volumes created by `docker-compose up`, run:

```sh
docker-compose down --volumes
```