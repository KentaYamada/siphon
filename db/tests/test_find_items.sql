-- 初期データ投入
SELECT create_test_data_items();

-- 全件検索
SELECT find_items(NULL, NULL);
SELECT find_items(NULL, '');

-- カテゴリ検索
SELECT find_items(1, NULL);
SELECT find_items(1, '');

-- キーワード検索
SELECT find_items(NULL, 'パスタ');

-- 組み合わせ検索
SELECT find_items(3, 'パスタ');

-- データリセット
TRUNCATE TABLE items RESTART IDENTITY;
