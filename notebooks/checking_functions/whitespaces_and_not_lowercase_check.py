from pyspark.sql import functions as F

# CHECK FOR NON-STANDARDIZED VALUES WHICH HAVE UNWANTED WHITESPACES OR NOT FOLLOWING ALL lowercase CHARACTERS

def whitespaces_and_not_lowercase_check (df, column_name):
    return df.filter(F.lower(F.trim(F.col(column_name))) != (F.col(column_name)))\
    .select(F.col("id"),F.col(column_name).alias(f"nonstandardized_{column_name}"))\
    .show()