-- 全件検索
SELECT find_categories(NULL);
SELECT find_categories('');

-- キーワード検索
SELECT find_categories('セット');

TRUNCATE TABLE categories RESTART IDENTITY;
