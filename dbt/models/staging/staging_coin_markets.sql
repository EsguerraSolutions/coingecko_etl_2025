WITH silver_coin_markets AS (
    SELECT 
        * EXCEPT(roi),
        roi AS return_on_investment
    FROM 
        {{ source('silver', 'silver_coin_markets') }}
)
SELECT 
    *
FROM 
    silver_coin_markets