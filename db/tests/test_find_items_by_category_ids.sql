-- 初期データ投入
SELECT create_test_data_items();

-- 全件検索
SELECT find_items_by_category_ids(ARRAY[1, 2]::int[]);

-- データリセット
TRUNCATE TABLE items RESTART IDENTITY;

