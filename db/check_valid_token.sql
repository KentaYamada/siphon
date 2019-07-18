CREATE OR REPLACE FUNCTION check_valid_token(
    p_token text,
    p_expired date
)
RETURNS TABLE(valid_token_count bigint)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        COUNT(*) AS valid_token_count
    FROM tokens
    WHERE token = p_token
      AND expired >= p_expired;
END $$;
