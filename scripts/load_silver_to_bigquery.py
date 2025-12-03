import os
import sys

from google.cloud import bigquery
from pathlib import Path

current_file = Path(__file__).resolve()
project_root = current_file.parents[1]
sys.path.append(str(project_root))

from utils.get_date_today_iso_string import get_date_today_iso_string

client = bigquery.Client()

PROJECT_ID          = os.getenv("GCP_PROJECT","coingecko-etl-pipeline")
SILVER_DATASET      = os.getenv("SILVER_DATASET","silver")
SILVER_TABLE_NAME   = os.getenv("SILVER_TABLE_NAME", "silver_coin_markets")

table_id = f"{PROJECT_ID}.{SILVER_DATASET}.{SILVER_TABLE_NAME}"

parquet_path = project_root / "data" / "silver" / "coin_markets" / "parquet" / get_date_today_iso_string()

parquet_file = next(parquet_path.glob("*.parquet"))

with open(parquet_file, "rb") as f:
    job = client.load_table_from_file(
        f,
        table_id,
        job_config=bigquery.LoadJobConfig(source_format="PARQUET", write_disposition="WRITE_TRUNCATE")
    )

job.result() 
