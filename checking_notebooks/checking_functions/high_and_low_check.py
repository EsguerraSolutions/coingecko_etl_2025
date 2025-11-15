from pyspark.sql import functions as F

def high_and_low_check (df, high_column_name, low_column_name):
    return df.filter(F.col(high_column_name) < F.col(low_column_name))\
    .select(F.col("id"),F.col(high_column_name), F.col(low_column_name))\
    .show()