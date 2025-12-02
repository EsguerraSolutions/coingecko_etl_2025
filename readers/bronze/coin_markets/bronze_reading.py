import sys

from pyspark.sql import SparkSession
from pathlib import Path

current_file = Path(__file__).resolve()
project_root = current_file.parents[3]
sys.path.append(str(project_root))

from utils.get_date_today_iso_string import get_date_today_iso_string

spark = SparkSession.builder.appName("ReadParquetFile").getOrCreate()

reading_date = get_date_today_iso_string()

bronze_parquet_dir = project_root / "data" / "bronze" / "coin_markets" / "parquet" / reading_date

bronze_df = spark.read.parquet(str(bronze_parquet_dir))

schema_order_path = project_root / "schema" / "bronze" / "coin_markets" / "schema_order.txt"

with open(schema_order_path) as f:
    bronze_to_silver_df_column_order = f.read().split(",")

bronze_to_silver_df = bronze_df.select(*bronze_to_silver_df_column_order)