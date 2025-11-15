from pyspark.sql import functions as F

def standardize_roi_struct_clean (df):
    return df.withColumn("roi",
    F.when(
        F.col("roi").isNotNull(),
        F.struct(
            F.trim(F.col("roi.currency")).alias("currency"),
            F.col("roi.percentage").alias("percentage"),
            F.col("roi.times").alias("times")
        )
    ).otherwise(None))