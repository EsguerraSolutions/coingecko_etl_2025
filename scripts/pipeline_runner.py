import sys

from pathlib import Path

current_file = Path(__file__).resolve()
bootstrap_root = current_file.parents[1]
sys.path.append(str(bootstrap_root))

from utils.get_project_root import get_project_root

project_root = get_project_root()

from pipelines.bronze.coin_markets.bronze_extraction import bronze_extraction
from pipelines.silver.coin_markets.silver_cleaning import silver_cleaning
from readers.bronze.coin_markets.bronze_reading import bronze_to_silver_df

def pipeline_runner():
    bronze_extraction()
    silver_cleaning(bronze_to_silver_df)

if __name__ == "__main__":
    pipeline_runner()
