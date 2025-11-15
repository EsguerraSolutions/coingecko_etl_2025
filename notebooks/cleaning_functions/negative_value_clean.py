from pyspark.sql import functions as F

def negative_value_clean (df, column_name):

    return df.withColumn(
        column_name,
        F.when(F.col(column_name) < 0, F.lit(None)).otherwise(F.col(column_name))
    )