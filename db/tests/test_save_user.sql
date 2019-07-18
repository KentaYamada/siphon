-- 新規作成
SELECT save_user(NULL, 'Test user', 'Tester chan', 'test@email.com', 'test');

-- 確認
SELECT * FROM users WHERE nickname like '%Tester%';

-- 更新
SELECT save_user(1, 'Edit user', 'Edit Tester chan', 'test@email.com', 'test');

-- 確認
SELECT * FROM users WHERE nickname like '%Tester%';

-- データ初期化
TRUNCATE TABLE users RESTART IDENTITY;

