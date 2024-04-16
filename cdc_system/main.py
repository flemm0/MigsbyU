from pyspark.sql.streaming import StreamingQueryManager
from streams import *
from utils import create_spark_connection



if __name__ == '__main__':
    spark = create_spark_connection()
    students_streaming_query = students_streaming_query(spark)
    professsors_streaming_query = professsors_streaming_query(spark)
    courses_streaming_query = courses_streaming_query(spark)
    enrollments_streaming_query = enrollments_streaming_query(spark)
    assignments_streaming_query = assignments_streaming_query(spark)
    spark.streams.awaitAnyTermination()