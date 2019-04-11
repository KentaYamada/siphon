-- 初期データ投入
SELECT create_test_data_users();

-- データ削除
SELECT delete_user(1);

-- データ確認
SELECT COUNT(id) FROM users WHERE id = 1;

-- データ初期化
TRUNCATE TABLE users RESTART IDENTITY;
