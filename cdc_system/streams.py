import pyspark.sql.functions as fc

from utils import read_kafka_topic
import schemas



def students_streaming_query(spark, testing=False):
    df = read_kafka_topic(spark_conn=spark, topic='migsbyu.public.students')
    
    json_df = df.selectExpr("cast(value as string) as value")

    students_df = json_df \
        .withColumn('value', fc.from_json(json_df['value'], schemas.students_schema)) \
        .select('value.payload.after.*', fc.from_unixtime(fc.col('value.payload.source.ts_ms') / 1000).alias('source_datetime')) \
        .withColumn('gpa', fc.when(fc.col('gpa.scale') == 2, fc.conv(fc.hex('gpa.value'), 16, 10) / 100).otherwise(fc.conv(fc.hex('gpa.value'), 16, 10) / 10))

    if testing:
        query = (students_df.writeStream \
            .outputMode('append') \
            .format('console') \
            .option('truncate', 'false') \
            .start())
    else:
        query = (students_df.writeStream \
            .format('parquet') \
            .option('path', '/data_lake/students/data') \
            .option('checkpointLocation', '/data_lake/students/checkpoint') \
            .outputMode('append') \
            .start())
    
    return query


def professsors_streaming_query(spark, testing=False):
    df = read_kafka_topic(spark_conn=spark, topic='migsbyu.public.professors')

    json_df = df.selectExpr('cast(value as string) as value')

    professors_df = json_df \
        .withColumn('value', fc.from_json(json_df['value'], schemas.professors_schema)) \
        .select('value.payload.after.*', fc.from_unixtime(fc.col('value.payload.source.ts_ms') / 1000).alias('source_datetime')) \
        .withColumn('date_of_birth', fc.from_unixtime(fc.col('date_of_birth')).cast('date'))
    
    if testing:
        query = (professors_df.writeStream \
                .outputMode('append') \
                .format('console') \
                .option('truncate', 'false') \
                .start())
    else:    
        query = (professors_df.writeStream \
            .format('parquet') \
            .option('path', '/data_lake/professors/data') \
            .option('checkpointLocation', '/data_lake/professors/checkpoint') \
            .outputMode('append') \
            .start())

    return query


def courses_streaming_query(spark, testing=False):
    df = read_kafka_topic(spark_conn=spark, topic='migsbyu.public.courses')

    json_df = df.selectExpr('cast(value as string) as value')

    courses_df = json_df \
        .withColumn('value', fc.from_json(json_df['value'], schemas.courses_schema)) \
        .select('value.payload.after.*', fc.from_unixtime(fc.col('value.payload.source.ts_ms') / 1000).alias('source_datetime')) \
    
    if testing:
        query = (courses_df.writeStream \
                .outputMode('append') \
                .format('console') \
                .option('truncate', 'false') \
                .start())
    else:
        query = courses_df.writeStream \
            .format('parquet') \
            .option('path', '/data_lake/courses/data') \
            .option('checkpointLocation', '/data_lake/courses/checkpoint') \
            .outputMode('append') \
            .start()

    return query


def enrollments_streaming_query(spark, testing=False):
    df = read_kafka_topic(spark_conn=spark, topic='migsbyu.public.takes')

    json_df = df.selectExpr('cast(value as string) as value')

    courses_df = json_df \
        .withColumn('value', fc.from_json(json_df['value'], schemas.takes_schema)) \
        .select('value.payload.after.*', fc.from_unixtime(fc.col('value.payload.source.ts_ms') / 1000).alias('source_datetime')) \
    
    if testing:
        query = (courses_df.writeStream \
                .outputMode('append') \
                .format('console') \
                .option('truncate', 'false') \
                .start())
    else:
        query = courses_df.writeStream \
            .format('parquet') \
            .option('path', '/data_lake/takes/data') \
            .option('checkpointLocation', '/data_lake/takes/checkpoint') \
            .outputMode('append') \
            .start()

    return query



def assignments_streaming_query(spark, testing=False):
    df = read_kafka_topic(spark_conn=spark, topic='migsbyu.public.teaches')

    json_df = df.selectExpr('cast(value as string) as value')

    courses_df = json_df \
        .withColumn('value', fc.from_json(json_df['value'], schemas.teaches_schema)) \
        .select('value.payload.after.*', fc.from_unixtime(fc.col('value.payload.source.ts_ms') / 1000).alias('source_datetime')) \
    
    if testing:
        query = (courses_df.writeStream \
                .outputMode('append') \
                .format('console') \
                .option('truncate', 'false') \
                .start())
    else:
        query = courses_df.writeStream \
            .format('parquet') \
            .option('path', '/data_lake/teaches/data') \
            .option('checkpointLocation', '/data_lake/teaches/checkpoint') \
            .outputMode('append') \
            .start()

    return query
