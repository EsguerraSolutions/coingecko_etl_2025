{{ config(materialized = 'table') }}

WITH fact_coin_markets AS (
    SELECT *
    FROM {{ ref('fact_coin_markets') }}
),

dim_coin AS (
    SELECT *
    FROM {{ ref('dim_coin') }}
),

joined_coin_markets AS (
    SELECT
        fcm.coin_id,
        dc.* EXCEPT(coin_key, coin_id),
        fcm.* EXCEPT(coin_key, coin_id)
    FROM fact_coin_markets fcm
    LEFT JOIN dim_coin dc
        ON fcm.coin_key = dc.coin_key
),

coin_markets_features AS (
    SELECT
        * EXCEPT(last_updated, ingestion_date, cleaning_date),
        (current_price / ath) AS price_to_ath_ratio,
        (market_cap / fully_diluted_valuation) AS market_cap_to_fdv_ratio,
        (circulating_supply / total_supply) AS circulating_supply_ratio,
        ((high_24h - low_24h) / current_price) AS volatility_24h,
        (market_cap_rank <= 100) AS is_top_100,
        ingestion_date,
        cleaning_date,
        last_updated

    FROM joined_coin_markets
)

SELECT * FROM coin_markets_features
