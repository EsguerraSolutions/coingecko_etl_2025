from pyspark.sql import functions as F

def duplicates_clean (df, column_name):
    
    return df.dropDuplicates([column_name])