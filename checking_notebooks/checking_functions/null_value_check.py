from pyspark.sql import functions as F

def null_value_check (df, column_name):
    return df.filter(F.col(column_name).isNull())\
    .select(F.col("id"),F.col(column_name).alias(f"null_{column_name}"))\
    .show()
