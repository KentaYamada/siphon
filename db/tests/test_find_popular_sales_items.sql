-- データ作成
SELECT create_popular_sales_items();

-- 検索
SELECT find_popular_sales_items(CURRENT_DATE, CURRENT_DATE);

--データリセット
TRUNCATE TABLE sales RESTART IDENTITY;
TRUNCATE TABLE sales_items RESTART IDENTITY;
