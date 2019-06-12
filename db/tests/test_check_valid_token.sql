-- 初期データ投入
SELECT create_test_data_tokens();

-- 今日が有効期限なユーザー
SELECT check_valid_token('test', CURRENT_DATE);

-- 有効期限を過ぎたトークン
SELECT check_valid_token('fuga', CURRENT_DATE);

-- 有効期間中のトークン
SELECT check_valid_token('hoge', CURRENT_DATE);

-- 該当するトークンがない
SELECT check_valid_token('spam', CURRENT_DATE);

-- データリセット
TRUNCATE TABLE tokens RESTART IDENTITY;
