from pyspark.sql import functions as F

def whitespaces_and_to_lowercase_clean (df, column_name):

    return df.withColumn(column_name, F.lower(F.trim(F.col(column_name))))
