from fastapi import FastAPI
from google.cloud import bigquery
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

import os

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# The path to your service account JSON is set in .env as GOOGLE_APPLICATION_CREDENTIALS
# Example .env content: GOOGLE_APPLICATION_CREDENTIALS=api/credentials/bigquery-key.json

# Create BigQuery client
client = bigquery.Client()

ANALYTICS_DATASET_ID = os.getenv("ANALYTICS_DATASET_ID")
ANALYTICS_TABLE_ID = os.getenv("ANALYTICS_TABLE_ID")

@app.get("/")
def get_crypto_data():
    query = f"""
        SELECT *
        FROM `{ANALYTICS_DATASET_ID}.{ANALYTICS_TABLE_ID}`
        LIMIT 1000
    """

    query_job = client.query(query)
    results = query_job.result()

    # Convert rows to list of dicts
    rows = [dict(row) for row in results]
    return {"rows": rows}
