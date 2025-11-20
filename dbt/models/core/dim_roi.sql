WITH dim_roi AS (
    SELECT 
        return_on_investment.currency,
        return_on_investment.percentage,
        return_on_investment.times
    FROM {{ ref('staging_coin_markets') }}

)
SELECT 
    *
FROM 
    dim_roi