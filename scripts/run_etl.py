import subprocess
import sys

def run_step(name, script):
    print(f"=== Running {name} ===")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        raise Exception(f"{name} failed")

def run_etl():
    run_step("Bronze extraction", "pipelines/bronze/coin_markets/bronze_extraction.py")
    run_step("Silver cleaning", "pipelines/silver/coin_markets/silver_cleaning.py")
    run_step("Load into Bigquery Warehouse", "scripts/load_silver_to_bigquery.py")
    run_step("DBT Transformation", "scripts/run_dbt.py")

    print("=== All steps completed successfully ===")

if __name__ == "__main__":
    run_etl()
