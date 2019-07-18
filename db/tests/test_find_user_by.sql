-- 初期データ投入
SELECT create_test_data_users();

-- 全件検索
SELECT find_users_by(NULL);
SELECT find_users_by('');

-- キーワード検索
SELECT find_users_by('太郎');

-- データ初期化
TRUNCATE TABLE users RESTART IDENTITY;
