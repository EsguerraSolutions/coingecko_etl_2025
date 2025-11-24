{{ config(materialized='table') }}

WITH silver_coin_markets AS (
    SELECT 
        * EXCEPT(roi),
        roi.currency AS roi_currency,
        roi.percentage AS roi_percentage,
        roi.times AS roi_times
    FROM {{ ref('staging_coin_markets') }}
)
SELECT 
    *
FROM 
    silver_coin_markets