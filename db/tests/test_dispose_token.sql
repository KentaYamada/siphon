-- トークンデータ作成
SELECT create_test_data_tokens();

-- testトークンをブラックリストへ
SELECT dispose_token('test');

-- データの変化を確認
SELECT * FROM black_lists;
SELECT * FROM tokens WHERE token = 'test';

-- データリセット
TRUNCATE TABLE tokens RESTART IDENTITY;
TRUNCATE TABLE black_lists RESTART IDENTITY;
