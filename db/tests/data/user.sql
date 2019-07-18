/**
 * ユーザーテストデータ作成
 */
CREATE OR REPLACE FUNCTION create_test_data_users()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO users
        (name, nickname, email, password)
    VALUES
        ('テスト 太郎', '太郎さん', 'test.taro@email.com', 'tarosan'),
        ('テスト 花子', '花子さん', 'test.hanako@email.com', 'hanakosan'),
        ('テスト トム', 'トミー', 'test.tom@email.com', 'tommy');
END $$;
