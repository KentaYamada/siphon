-- 削除
SELECT delete_category(1);

-- データ確認
SELECT COUNT(id) FROM categories WHERE id = 1;

-- データ初期化
TRUNCATE TABLE categories RESTART IDENTITY;

-- 初期化確認
SELECT COUNT(*) FROM categories;
