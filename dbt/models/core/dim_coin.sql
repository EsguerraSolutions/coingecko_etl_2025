{{ config(
    materialized='incremental',
    unique_key='coin_id'
) }}

WITH dim_coin AS (
    SELECT
        id AS coin_id,
        symbol,
        name,
        image
    FROM {{ source('raw', 'coin_markets') }}
)

SELECT
    COALESCE((SELECT coin_key FROM {{ this }} WHERE coin_id = stg_coin.coin_id),
             MAX(coin_key) OVER () + 1) AS coin_key,
    coin_id,
    symbol,
    name,
    image
FROM dim_coin
