-- 保存
SELECT save_token(1, 'testtest', CURRENT_DATE);

-- データ確認
SELECT * FROM tokens;

-- データ初期化
TRUNCATE TABLE tokens RESTART IDENTITY;
