{{ config(materialized='table') }}

WITH staging_data AS (
    -- merged staging model
    SELECT * FROM {{ ref('stg_superstore') }}
)

SELECT 
    REGION,
    CATEGORY,
    SUM(SALES) as total_sales,
    SUM(PROFIT) as total_profit,
    -- Calculate average profit margin using the decimal column
    AVG(profit_margin_decimal) as avg_profit_margin
FROM staging_data
GROUP BY 1, 2