from pyspark.sql import functions as F

def duplicates_check (df, column_name):
    return df.withColumn(f"cleaned_{column_name}", F.trim(F.lower(F.col(column_name))))\
        .groupBy(f"cleaned_{column_name}")\
        .agg(F.count("*").alias(f"cleaned_{column_name}_distinct_count"))\
        .filter(F.col(f"cleaned_{column_name}_distinct_count") > 1 )\
        .show()