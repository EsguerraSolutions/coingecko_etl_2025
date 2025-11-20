SELECT *
FROM {{ model }}
WHERE TRY_CAST({{ column_name }} AS TIMESTAMP) IS NULL
