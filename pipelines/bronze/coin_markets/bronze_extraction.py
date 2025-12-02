import os
import sys
import json
import requests

from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit
from pyspark.sql.types import *
from pathlib import Path

current_file = Path(__file__).resolve()
project_root = current_file.parents[3]
sys.path.append(str(project_root))

from schema.bronze.coin_markets.column_order import bronze_df_column_order
from utils.get_date_today_iso_string import get_date_today_iso_string

def bronze_extraction() :

    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    API_URL = os.getenv("API_URL")

    coin_markets_url = f"{API_URL}/coins/markets?vs_currency=usd"

    headers = {
        "x-cg-demo-api-key": API_KEY,
    }

    coin_markets_response = requests.get(coin_markets_url, headers=headers)

    coin_markets_list = coin_markets_response.json()

    formatted_coin_markets_response = json.dumps(coin_markets_list, indent = 4)

    extraction_date = get_date_today_iso_string()
    bronze_json_dir = project_root / "data" / "bronze" / "coin_markets" / "raw_json" / extraction_date
    bronze_json_dir.mkdir(parents=True, exist_ok=True)
    bronze_json_file = bronze_json_dir / "coin_markets.json"

    with open(bronze_json_file, "w") as f:
        json.dump(coin_markets_list, f)

    spark = SparkSession.builder.appName("ConvertJSONtoParquet").getOrCreate()

    bronze_df = spark.read.option("inferSchema", True).json(str(bronze_json_file))
    bronze_df = bronze_df.withColumn("ingestion_date", current_timestamp())
    bronze_df = bronze_df.select(*bronze_df_column_order, "ingestion_date")

    schema_order_path = project_root / "schema" / "bronze" / "coin_markets" / "schema_order.txt"

    with open(schema_order_path, "w") as f:
        f.write(",".join(bronze_df.columns))

    bronze_parquet_dir = project_root / "data" / "bronze" / "coin_markets" / "parquet" / extraction_date

    bronze_df.write.mode("overwrite").parquet(str(bronze_parquet_dir))

bronze_extraction()


