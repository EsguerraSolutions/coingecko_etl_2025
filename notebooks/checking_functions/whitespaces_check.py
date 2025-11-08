from pyspark.sql import functions as F

def whitespaces_check (df, column_name):
    return df.filter(F.trim(F.col(column_name)) != (F.col(column_name)))\
    .select(F.col("id"),F.col(column_name).alias(f"whitespaced_{column_name}"))\
    .show()