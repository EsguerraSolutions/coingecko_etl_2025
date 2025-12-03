import sys

from pyspark.sql.functions import current_timestamp
from pathlib import Path

current_file = Path(__file__).resolve()
project_root = current_file.parents[3]
sys.path.append(str(project_root))

from notebooks.cleaning_functions import (
    datestring_to_timestamp_clean,
    null_value_clean,
    whitespaces_clean,
    whitespaces_and_to_lowercase_clean,
    negative_value_clean,
    duplicates_clean,
    rank_clean,
    standardize_roi_struct_clean
)

from readers.bronze.coin_markets.bronze_reading import bronze_to_silver_df

from utils.get_date_today_iso_string import get_date_today_iso_string

def silver_cleaning(bronze_to_silver_df) :


    # CLEAN FOR NULL VALUES, UNWANTED WHITESPACES AND DUPLICATES OF ID COLUMN

    id_cleaning_functions = [null_value_clean, whitespaces_clean, duplicates_clean]

    for function in id_cleaning_functions:
        bronze_to_silver_df = function(bronze_to_silver_df, "id")

    # CLEAN FOR NULL VALUES, UNWANTED WHITESPACES and STANDARDIZE TO ALL LOWERCASE OF SYMBOL COLUMN

    symbol_cleaning_functions = [null_value_clean, whitespaces_and_to_lowercase_clean]

    for function in symbol_cleaning_functions:
        bronze_to_silver_df = function(bronze_to_silver_df, "symbol")


    # CLEAN FOR NULL VALUES abd UNWANTED WHITESPACES OF NAME COLUMN

    name_cleaning_functions = [null_value_clean, whitespaces_clean]

    for function in name_cleaning_functions:
        bronze_to_silver_df = function(bronze_to_silver_df, "symbol")

    # CLEAN NULL VALUES FOR IMAGE COLUMN
    ## THERE IS NO CLEANING YET FOR INVALID URL FORMATS FOR image COLUMN because there is NO BAD DATA

    bronze_to_silver_df = null_value_clean(bronze_to_silver_df, "image")

    # CLEAN FOR NEGATIVE VALUES OF CURRENT PRICE COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"current_price")

    # CLEAN FOR NEGATIVE VALUES OF MARKET CAP COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"market_cap")

    # CLEAN FOR NEGATIVE VALUES OF MARKET CAP RANK COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"market_cap_rank")

    # ADD FLAG FOR MISMATCHING market_cap_rank BASED ON VALUES OF market_cap ARRANGED MANUALLY

    bronze_to_silver_df = rank_clean(bronze_to_silver_df, "market_cap", "market_cap_rank")

    # CLEAN FOR NEGATIVE VALUES OF FULLY DILUATED VALUATION COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"fully_diluted_valuation")

    # CLEAN FOR NEGATIVE VALUES OF TOTAL VOLUME COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"total_volume")

    # CLEAN FOR NEGATIVE VALUES OF HIGH 24H COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"high_24h")

    # CLEAN FOR NEGATIVE VALUES OF LOW 24H COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"low_24h")

    # CLEAN FOR NEGATIVE VALUES OF CIRCULATING SUPPLY COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"circulating_supply")

    # CLEAN FOR NEGATIVE VALUES OF TOTAL SUPPLY COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"total_supply")

    # CLEAN FOR NEGATIVE VALUES OF MAX SUPPLY COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"max_supply")

    # CLEAN FOR NEGATIVE VALUES OF ath COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"ath")

    # CAST TO DATE TIME OBJECT FOR ath_date COLUMN

    bronze_to_silver_df = datestring_to_timestamp_clean(bronze_to_silver_df,"ath_date")

    # CLEAN FOR NEGATIVE VALUES OF atl COLUMN

    bronze_to_silver_df = negative_value_clean(bronze_to_silver_df,"atl")

    # CAST TO DATE TIME OBJECT FOR atl_date COLUMN

    bronze_to_silver_df = datestring_to_timestamp_clean(bronze_to_silver_df,"atl_date")

    # STANDARDIZE currency value on roi column

    bronze_to_silver_df = standardize_roi_struct_clean(bronze_to_silver_df)

    # CHECK FOR INVALID DATE FORMAT, DATE IS IN THE FUTURE AND NULL VALUES OF last_updated COLUMN

    bronze_to_silver_df = datestring_to_timestamp_clean(bronze_to_silver_df,"last_updated")

    # ADD A NEW COLUMN CALLED "cleaning_date" FOR THE SILVER LAYER

    silver_df = bronze_to_silver_df.withColumn("cleaning_date", current_timestamp())

    silver_parquet_dir = project_root / "data" / "silver" / "coin_markets" / "parquet" / get_date_today_iso_string()

    silver_df.coalesce(1).write.mode("overwrite").parquet(str(silver_parquet_dir))

silver_cleaning(bronze_to_silver_df)
