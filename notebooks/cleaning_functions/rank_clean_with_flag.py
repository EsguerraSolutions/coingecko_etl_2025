from pyspark.sql import functions as F, Window

def rank_clean_with_flag(df, column_name, rank_column_name):

    expected_rank_column_name = f"expected_{rank_column_name}"

    w = Window.orderBy(F.col(column_name).desc())

    df_with_expected_rank = df.withColumn(expected_rank_column_name, F.row_number().over(w))

    df_with_mismatch_rank = df_with_expected_rank.filter(F.col(rank_column_name) != F.col(expected_rank_column_name))

    if df_with_mismatch_rank.count() == 0:
        return df
    
    else:

        df_rank_cleaned = df_with_expected_rank.withColumn(
            f"{rank_column_name}_mismatch_flag",
                F.col(expected_rank_column_name) != F.col(rank_column_name)
            )  

        return df_rank_cleaned