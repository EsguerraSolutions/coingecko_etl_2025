from pyspark.sql import functions as F

def url_format_and_null_check (df, column_name):
    url_pattern = r'^(https?://)([A-Za-z0-9.-]+)(:[0-9]+)?(/[A-Za-z0-9._~:/?#\[\]@!$&\'()*+,;=%-]*)?$'
    return df.filter(F.col(column_name).isNull() | (~F.col(column_name).rlike(url_pattern)))\
    .select(F.col("id"),F.col(column_name).alias(f"invalid_{column_name}_url"))\
    .show()
