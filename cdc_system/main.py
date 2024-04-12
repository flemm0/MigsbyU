from pyspark.sql.streaming import StreamingQueryManager
from streams import *
from utils import create_spark_connection



if __name__ == '__main__':
    spark = create_spark_connection()
    students_streaming_query = students_streaming_query(spark, testing=True)
    professsors_streaming_query = professsors_streaming_query(spark, testing=True)
    courses_streaming_query = courses_streaming_query(spark, testing=True)
    spark.streams.awaitAnyTermination()