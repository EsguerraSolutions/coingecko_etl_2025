WITH silver_coin_markets AS (
    SELECT 
        * EXCEPT(roi, last_updated, ingestion_date, cleaning_date),
        roi.currency AS roi_currency,
        roi.percentage AS roi_percentage,
        roi.times AS roi_times,
        ingestion_date,
        cleaning_date,
        last_updated
    FROM {{ source('silver', 'silver_coin_markets') }}
)
SELECT 
    *
FROM 
    silver_coin_markets