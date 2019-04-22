-- 新規作成
SELECT create_test_data_daily_sales_items();

-- 検索
SELECT find_daily_sales_items(ARRAY[1, 2]::int[]);

-- データリセット
TRUNCATE TABLE sales_items RESTART IDENTITY;
