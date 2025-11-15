from pyspark.sql import functions as F

def change_percentage_check (df, current_column_name, change_column_name, change_percentage_column_name):

    tolerance = 0.1

    previous_column_name = f"previous_{current_column_name}"
    derived_change_percentage_column_name = f"derived_{change_percentage_column_name}"

    previous_column_value = F.col(current_column_name) - F.col(change_column_name)
    derived_change_percentage_column_value = F.col(change_column_name) / F.col(previous_column_name) * 100

    compare_derived_and_actual_change_percentage = F.abs((F.col(derived_change_percentage_column_name))) - F.abs((F.col(change_percentage_column_name))) > tolerance

    return df.withColumn(previous_column_name, previous_column_value)\
    .withColumn(derived_change_percentage_column_name, derived_change_percentage_column_value)\
    .filter(compare_derived_and_actual_change_percentage)\
    .select(F.col("id"),F.col(current_column_name),F.col(change_column_name),F.col(previous_column_name),\
            F.col(derived_change_percentage_column_name),F.col(change_percentage_column_name))\
    .show()