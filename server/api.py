from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from google.cloud import bigquery
from dotenv import load_dotenv
from google.oauth2 import service_account

import os
import json
import base64

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

FRONTEND_API_URL_LIST = os.getenv("FRONTEND_API_URL_LIST")

origins = FRONTEND_API_URL_LIST

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

b64 = os.environ["GOOGLE_CREDENTIALS_B64"]
decoded = base64.b64decode(b64)
service_account_info = json.loads(decoded)
credentials = service_account.Credentials.from_service_account_info(service_account_info)


# Create BigQuery client
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

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

    rows = [dict(row) for row in results]
    return {"rows": rows}
