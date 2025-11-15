from pyspark.sql import functions as F

def null_value_clean (df, column_name):
    
    return df.filter(F.col(column_name).isNotNull())

