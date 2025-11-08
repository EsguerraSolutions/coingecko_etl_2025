from pyspark.sql import functions as F

def datestring_format_and_null_check (df, column_name):
    url_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$'
    return df.filter(F.col(column_name).isNull() | (~F.col(column_name).rlike(url_pattern)))\
    .select(F.col("id"),F.col(column_name).alias(f"invalid_{column_name}_url"))\
    .show()
