from pyspark.sql import functions as F

def datestring_format_and_null_check (df, column_name):
    date_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$'

    current_time = F.current_timestamp()

    parsed_datestring = F.to_timestamp(F.col(column_name), "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'")

    return df.filter(
                    (F.col(column_name).isNull()) |
                    (~F.col(column_name).rlike(date_pattern)) |
                    (parsed_datestring > current_time)
                    )\
    .select(F.col("id"),F.col(column_name).alias(f"invalid_{column_name}_url"))\
    .show()
