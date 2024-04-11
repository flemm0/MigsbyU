from pyspark.sql.types import StringType, StructType, StructField, IntegerType, FloatType, ArrayType, BooleanType, BinaryType, LongType



schema = StructType([
    StructField("schema", StructType([
        StructField("type", StringType(), True),
        StructField("fields", ArrayType(StructType([
            StructField("type", StringType(), True),
            StructField("optional", BooleanType(), True),
            StructField("field", StringType(), True),
            StructField("name", StringType(), True),
            StructField("version", IntegerType(), True),
            StructField("doc", StringType(), True),
            StructField("parameters", StructType([
                StructField("allowed", StringType(), True),
                StructField("default", StringType(), True)
            ]), True)
        ])), True),
        StructField("name", StringType(), True),
        StructField("optional", BooleanType(), True),
        StructField("version", IntegerType(), True)
    ]), True),
    StructField("payload", StructType([
        StructField("before", StructType([
            # Fields for "before" structure
        ]), True),
        StructField("after", StructType([
            StructField("id", StringType(), True),
            StructField("first_name", StringType(), True),
            StructField("last_name", StringType(), True),
            StructField("gender", StringType(), True),
            StructField("address", StringType(), True),
            StructField("date_of_birth", StringType(), True),
            StructField("major", StringType(), True),
            StructField("year_of_study", IntegerType(), True),
            StructField("gpa", StructType([
                StructField("scale", IntegerType(), True),
                StructField("value", BinaryType(), True)
            ]), True),
            StructField("enrollment_status", StringType(), True)
        ]), True),
        StructField("source", StructType([
            StructField("version", StringType(), True),
            StructField("connector", StringType(), True),
            StructField("name", StringType(), True),
            StructField("ts_ms", LongType(), True),
            StructField("snapshot", StringType(), True),
            StructField("db", StringType(), True),
            StructField("sequence", StringType(), True),
            StructField("schema", StringType(), True),
            StructField("table", StringType(), True),
            StructField("txId", LongType(), True),
            StructField("lsn", LongType(), True),
            StructField("xmin", LongType(), True)
        ]), True),
        StructField("op", StringType(), True),
        StructField("ts_ms", LongType(), True),
        StructField("transaction", StructType([
            StructField("id", StringType(), True),
            StructField("total_order", LongType(), True),
            StructField("data_collection_order", LongType(), True)
        ]), True)
    ]), True),
    StructField("version", IntegerType(), True)
])