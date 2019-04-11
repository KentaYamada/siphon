-- 初期データ投入
SELECT create_test_data_categories();

-- 全件検索
SELECT find_categories(NULL);
SELECT find_categories('');

-- キーワード検索
SELECT find_categories('セット');

-- データリセット
TRUNCATE TABLE categories RESTART IDENTITY;
