from pyspark.sql import functions as F

def whitespaces_clean (df, column_name):

    return df.withColumn(column_name, F.trim(F.col(column_name)))
