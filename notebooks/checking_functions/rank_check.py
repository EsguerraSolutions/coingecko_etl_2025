from pyspark.sql import functions as F, Window

def rank_check(df, column, rank_column):

    w = Window.orderBy(F.col(column).desc())

    ranked_df = df.withColumn("expected_rank", F.dense_rank().over(w))

    invalid_rank_df = ranked_df.filter(
        F.col(rank_column) != F.col("expected_rank")
    ).select(
        "id", column, rank_column, "expected_rank"
    )

    invalid_rank_df.show()

    return invalid_rank_df
