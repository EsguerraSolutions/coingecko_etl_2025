import sys

from pyspark.sql import SparkSession

sys.path.append("../../..")
from utils.get_date_today_iso_string import get_date_today_iso_string

spark = SparkSession.builder.appName("ReadParquetFile").getOrCreate()

reading_date = get_date_today_iso_string()

bronze_df = spark.read.parquet(f"../../../data/bronze/coin_markets/parquet/{reading_date}/")

with open("../../../schema/bronze/coin_markets/schema_order.txt") as f:
    bronze_to_silver_df_column_order = f.read().split(",")

bronze_to_silver_df = bronze_df.select(*bronze_to_silver_df_column_order)