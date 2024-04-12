from pyspark.sql.types import StringType, StructType, StructField, IntegerType, FloatType, ArrayType, BooleanType, BinaryType, LongType



students_schema = StructType([
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


professors_schema = StructType([
    StructField("schema", StructType([
        StructField("type", StringType(), nullable=False),
        StructField("fields", StructType([
            StructField("type", StringType(), nullable=False),
            StructField("fields", StructType([
                StructField("type", StringType(), nullable=False),
                StructField("optional", StringType(), nullable=False),
                StructField("field", StringType(), nullable=False)
            ]), nullable=True),
            StructField("optional", StringType(), nullable=True),
            StructField("name", StringType(), nullable=True),
            StructField("version", IntegerType(), nullable=True),
            StructField("field", StringType(), nullable=False)
        ]), nullable=True),
        StructField("optional", StringType(), nullable=True),
        StructField("name", StringType(), nullable=False),
        StructField("version", IntegerType(), nullable=True),
        StructField("field", StringType(), nullable=False)
    ]), nullable=False),
    StructField("payload", StructType([
        StructField("before", StructType([
            StructField("id", StringType(), nullable=False),
            StructField("title", StringType(), nullable=True),
            StructField("first_name", StringType(), nullable=True),
            StructField("last_name", StringType(), nullable=True),
            StructField("gender", StringType(), nullable=True),
            StructField("address", StringType(), nullable=True),
            StructField("department", StringType(), nullable=True),
            StructField("date_of_birth", IntegerType(), nullable=True),
            StructField("annual_salary", IntegerType(), nullable=True)
        ]), nullable=True),
        StructField("after", StructType([
            StructField("id", StringType(), nullable=False),
            StructField("title", StringType(), nullable=True),
            StructField("first_name", StringType(), nullable=True),
            StructField("last_name", StringType(), nullable=True),
            StructField("gender", StringType(), nullable=True),
            StructField("address", StringType(), nullable=True),
            StructField("department", StringType(), nullable=True),
            StructField("date_of_birth", IntegerType(), nullable=True),
            StructField("annual_salary", IntegerType(), nullable=True)
        ]), nullable=True),
        StructField("source", StructType([
            StructField("version", StringType(), nullable=False),
            StructField("connector", StringType(), nullable=False),
            StructField("name", StringType(), nullable=False),
            StructField("ts_ms", LongType(), nullable=False),
            StructField("snapshot", StringType(), nullable=True),
            StructField("db", StringType(), nullable=False),
            StructField("sequence", StringType(), nullable=True),
            StructField("schema", StringType(), nullable=False),
            StructField("table", StringType(), nullable=False),
            StructField("txId", LongType(), nullable=True),
            StructField("lsn", LongType(), nullable=True),
            StructField("xmin", StringType(), nullable=True)
        ]), nullable=False),
        StructField("op", StringType(), nullable=False),
        StructField("ts_ms", LongType(), nullable=True),
        StructField("transaction", StructType([
            StructField("id", StringType(), nullable=False),
            StructField("total_order", LongType(), nullable=False),
            StructField("data_collection_order", LongType(), nullable=False)
        ]), nullable=True)
    ]), nullable=False)
])


courses_schema = StructType([
    StructField("schema", StructType([
        StructField("type", StringType(), nullable=False),
        StructField("fields", StructType([
            StructField("type", StringType(), nullable=False),
            StructField("fields", StructType([
                StructField("type", StringType(), nullable=False),
                StructField("optional", StringType(), nullable=False),
                StructField("field", StringType(), nullable=False)
            ]), nullable=True),
            StructField("optional", StringType(), nullable=True),
            StructField("name", StringType(), nullable=True),
            StructField("version", IntegerType(), nullable=True),
            StructField("field", StringType(), nullable=False)
        ]), nullable=True),
        StructField("optional", StringType(), nullable=True),
        StructField("name", StringType(), nullable=False),
        StructField("version", IntegerType(), nullable=True),
        StructField("field", StringType(), nullable=False)
    ]), nullable=False),
    StructField("payload", StructType([
        StructField("before", StructType([
            StructField("id", StringType(), nullable=False),
            StructField("name", StringType(), nullable=True),
            StructField("units", IntegerType(), nullable=True),
            StructField("department", StringType(), nullable=True)
        ]), nullable=True),
        StructField("after", StructType([
            StructField("id", StringType(), nullable=False),
            StructField("name", StringType(), nullable=True),
            StructField("units", IntegerType(), nullable=True),
            StructField("department", StringType(), nullable=True)
        ]), nullable=True),
        StructField("source", StructType([
            StructField("version", StringType(), nullable=False),
            StructField("connector", StringType(), nullable=False),
            StructField("name", StringType(), nullable=False),
            StructField("ts_ms", LongType(), nullable=False),
            StructField("snapshot", StringType(), nullable=True),
            StructField("db", StringType(), nullable=False),
            StructField("sequence", StringType(), nullable=True),
            StructField("schema", StringType(), nullable=False),
            StructField("table", StringType(), nullable=False),
            StructField("txId", LongType(), nullable=True),
            StructField("lsn", LongType(), nullable=True),
            StructField("xmin", StringType(), nullable=True)
        ]), nullable=False),
        StructField("op", StringType(), nullable=False),
        StructField("ts_ms", LongType(), nullable=True),
        StructField("transaction", StructType([
            StructField("id", StringType(), nullable=False),
            StructField("total_order", LongType(), nullable=False),
            StructField("data_collection_order", LongType(), nullable=False)
        ]), nullable=True)
    ]), nullable=False)
])