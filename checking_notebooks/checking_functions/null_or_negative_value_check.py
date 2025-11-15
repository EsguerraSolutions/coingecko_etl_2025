from pyspark.sql import functions as F

def null_or_negative_value_check (df, column_name):
    return df.filter((F.col(column_name) < 0) | (F.col(column_name).isNull()))\
    .select(F.col("id"),F.col(column_name).alias(f"invalid_{column_name}"))\
    .show()