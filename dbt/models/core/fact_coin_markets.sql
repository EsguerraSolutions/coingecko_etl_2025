{{ config(materialized='table') }}

WITH fact_coin_markets AS (
    SELECT
        id AS coin_id,
        current_price,
        market_cap,
        market_cap_rank,
        fully_diluted_valuation,
        total_volume,
        high_24h,
        low_24h,
        price_change_24h,
        price_change_percentage_24h,
        market_cap_change_24h,
        market_cap_change_percentage_24h,
        circulating_supply,
        total_supply,
        max_supply,
        ath,
        ath_change_percentage,
        ath_date,
        atl,
        atl_change_percentage,
        atl_date,
        roi_currency,
        roi_percentage,
        roi_times,
        ingestion_date,
        cleaning_date,
        last_updated,
    FROM {{ ref('staging_coin_markets') }}
),

fact_coin_markets_with_key AS (
    SELECT
        dc.coin_key,
        fcm.* 
    FROM fact_coin_markets fcm
    LEFT JOIN {{ ref('dim_coin') }} dc
        ON fcm.coin_id = dc.coin_id
)

SELECT *
FROM fact_coin_markets_with_key
