# Fabric


## Table Time Travel

```sql
# show tables
df = spark.sql("SHOW TABLES")
display(df)
  
--------------------------

# this shows all of the time travel info
%%sql
DESCRIBE HISTORY delta.`abfss://uuid-inserted-here@onelake.dfs.fabric.microsoft.com/uuid-inserted-here/Tables/fact_ws_adr`
;
  
--------------------------

# view the table at a specific version
%%sql
SELECT *
FROM delta.`abfss://uuid-inserted-here@onelake.dfs.fabric.microsoft.com/uuid-inserted-here/Tables/fact_ws_adr` 
VERSION AS OF 5431;

--------------------------

# queries of all kinds can be run on these
%%sql
SELECT 
LEFT(dim_disposition_date_id, 6) as date_id,
SUM(write_off_amount) as write_off_amount
FROM delta.`abfss://uuid-inserted-here@onelake.dfs.fabric.microsoft.com/uuid-inserted-here/Tables/fact_ws_adr` VERSION AS OF 5405
WHERE final_disposition = 'Partially Denied'
group by LEFT(dim_disposition_date_id, 6)
ORDER BY LEFT(dim_disposition_date_id, 6) DESC
;

--------------------------

%%sql
SELECT 
    LEFT(dim_disposition_date_id, 4) AS date_id,

    -- Partially Denied → sum(write_off_amount)
    SUM(
        CASE 
            WHEN final_disposition = 'Partially Denied' 
            THEN write_off_amount 
            ELSE 0 
        END
    )
    +
    -- Fully Denied → sum(revenue_amount)
    SUM(
        CASE 
            WHEN final_disposition = 'Fully Denied' 
            THEN revenue_amount 
            ELSE 0 
        END
    ) AS total_amount

FROM delta.`abfss://uuid-inserted-here@onelake.dfs.fabric.microsoft.com/uuid-inserted-here/Tables/fact_ws_adr` 
    VERSION AS OF 5442
WHERE dim_date_id >= 20250101
GROUP BY LEFT(dim_disposition_date_id, 4)
ORDER BY LEFT(dim_disposition_date_id, 4) DESC;

--------------------------
```
