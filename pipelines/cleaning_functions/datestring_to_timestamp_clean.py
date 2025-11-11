from pyspark.sql import functions as F

def datestring_to_timestamp_clean (df, column_name):

        return df.withColumn(column_name, F.to_timestamp(F.col(column_name), "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"))
