CREATE OR REPLACE FUNCTION create_test_data_tokens()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO tokens (
        user_id,
        token,
        expired
    ) VALUES
    (1, 'test', CURRENT_DATE),
    (2, 'hoge', (CURRENT_DATE + INTERVAL '7 DAY')),
    (3, 'fuga', (CURRENT_DATE - INTERVAL '7 DAY'));
END $$;
