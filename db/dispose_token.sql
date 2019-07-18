CREATE OR REPLACE FUNCTION dispose_token (
    p_token text
)
RETURNS TABLE(valid_token_count bigint)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    -- 対象のトークンをブラックリストへ
    INSERT INTO black_lists (token) VALUES (p_token);

    -- 有効となっているトークンを削除
    DELETE FROM tokens WHERE token = p_token;
END $$;
