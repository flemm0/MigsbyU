from pyspark.sql import SparkSession
import logging


def create_spark_connection():
    spark = None
    try:
        spark = SparkSession.builder \
            .appName('MigsbyU') \
            .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1') \
            .getOrCreate()

        spark.sparkContext.setLogLevel('ERROR')
        logging.info('Spark connection create successfully')
    except Exception as e:
        logging.error(f'Could not create spark session due to exception: {e}')

    return spark


def read_kafka_topic(spark_conn: SparkSession, topic: str):
    df = None
    try:
        df = spark_conn.readStream \
            .format('kafka') \
            .option('kafka.bootstrap.servers', 'kafka:9092') \
            .option('subscribe', topic) \
            .option('startingOffsets', 'earliest') \
            .load()
        logging.info('Kafka topic read successfully')
    except Exception as e:
        logging.warning(f'Kafka topic could not be created: {e}')
    
    return df