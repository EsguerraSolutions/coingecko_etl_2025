import os
from google.cloud import bigquery

PROJECT_ID          = os.getenv("GCP_PROJECT")
DATASET             = os.getenv("DATASET")
SILVER_TABLE_NAME   = os.getenv("SILVER_TABLE_NAME", "silver_coin_markets")
GCS_URI             = os.getenv("GCS_URI", "gs://my-bucket/cleaned_file.parquet")

client = bigquery.Client(project=PROJECT_ID)
job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.PARQUET)

load_job = client.load_table_from_uri(
    GCS_URI,
    f"{PROJECT_ID}.{DATASET}.{TABLE}",
    job_config=job_config,
)

load_job.result()
print(f"Loaded {TABLE} from {GCS_URI}")
