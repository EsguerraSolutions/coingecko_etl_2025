{{ config(materialized='table') }}

SELECT
    FARM_FINGERPRINT(id) AS coin_key,
    id AS coin_id,
    symbol,
    name,
    image,

FROM {{ ref('staging_coin_markets') }}
