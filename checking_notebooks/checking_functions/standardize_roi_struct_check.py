from pyspark.sql import functions as F

def standardize_roi_struct_check (df):
    return df.filter(F.col("roi").isNotNull()
    & 
    (
        F.col("roi.currency").isNull() |
        (F.trim(F.col("roi.currency")) != F.col("roi.currency")) |
        F.col("roi.percentage").isNull() |
        F.col("roi.times").isNull()
    )
    )\
    .select(F.col("id"), F.col("roi.currency"), F.col("roi.percentage"), F.col("roi.times")).show(truncate=False)

