WITH raw_data AS (
    SELECT * FROM SNOWFLAKE_LEARNING_DB.PUBLIC.SUPERSTORE_RAW
)

SELECT 
    *,
    -- Clean the Profit Margin: remove '%' and convert to a decimal number
    TRY_CAST(REPLACE(PROFIT_MARGIN, '%', '') AS FLOAT) / 100 AS profit_margin_decimal,
    TRY_CAST(REPLACE(TARGET_PROFIT_MARGIN, '%', '') AS FLOAT) / 100 AS target_margin_decimal
FROM raw_data