from pyspark.sql import SparkSession
import pyspark.sql.functions as fc

import schemas


spark = SparkSession.builder \
    .appName('MigsbyU') \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1') \
    .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

df = spark.readStream \
    .format('kafka') \
    .option('kafka.bootstrap.servers', 'kafka:9092') \
    .option('subscribe', 'migsbyu.public.students') \
    .option('startingOffsets', 'earliest') \
    .load()

json_df = df.selectExpr("cast(value as string) as value")

json_expanded_df = json_df.withColumn("value", fc.from_json(json_df["value"], schemas.schema)).select("value.*").select('payload.*').select('after.*')

# exploded_df = json_expanded_df.select(fc.explode('payload').alias('payload'))

query = json_expanded_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()