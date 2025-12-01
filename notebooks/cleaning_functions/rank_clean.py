from pyspark.sql import functions as F, Window

def rank_clean(df, column_name, rank_column_name):


    w = Window.orderBy(F.col(column_name).desc())

    df_with_cleaned_rank = df.withColumn(rank_column_name, F.row_number().over(w))

    return df_with_cleaned_rank