-- 新規作成
SELECT save_category(NULL, '新しい新規カテゴリ');

-- 更新
SELECT save_category(1, 'Morning set');

-- データ確認
SELECT * FROM categories ORDER BY id ASC;

-- データ初期化
TRUNCATE TABLE categories RESTART IDENTITY;
