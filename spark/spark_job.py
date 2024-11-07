from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("AirflowSparkDemo").getOrCreate()

    # Sample data
    data = [
        "Hello world",
        "Apache Airflow and Spark",
        "Docker Compose integration",
        "Hello from Spark",
        "Airflow orchestrates workflows"
    ]

    # Create RDD
    rdd = spark.sparkContext.parallelize(data)

    # Perform word count
    word_counts = (
        rdd.flatMap(lambda line: line.split(" "))
        .map(lambda word: (word.lower(), 1))
        .reduceByKey(lambda a, b: a + b)
        .collect()
    )

    # Print the results
    print("Word Counts:")
    for word, count in word_counts:
        print(f"{word}: {count}")

    spark.stop()

if __name__ == "__main__":
    main()
