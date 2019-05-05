-- テストデータ作成
SELECT create_test_data_users();

-- 登録済ユーザー検索
SELECT find_auth_user('test.taro@email.com', 'tarosan');

-- 未登録ユーザー検索
SELECT find_auth_user('test.taro@email.com', 'jiro');

-- テストデータ初期化
TRUNCATE TABLE users RESTART IDENTITY;
