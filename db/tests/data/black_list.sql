CREATE OR REPLACE FUNCTION create_test_data_black_lists()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO black_lists (token) VALUES
    ('test'),
    ('hoge'),
    ('fuga');
END $$;
