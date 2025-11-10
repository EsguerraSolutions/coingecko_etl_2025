from pyspark.sql import functions as F, Window

def rank_clean_with_flag(df, column_name, rank_column_name):

    expected_rank_column_name = f"expected_{rank_column_name}"

    w = Window.orderBy(F.col(column_name).desc())
    df_rank_cleaned = df.withColumn(expected_rank_column_name, F.dense_rank().over(w))

    df_rank_cleaned = df_rank_cleaned.withColumn(
        f"{rank_column_name}_mismatch_flag",
        F.col(expected_rank_column_name) != F.col(rank_column_name)
    )

    return df_rank_cleaned