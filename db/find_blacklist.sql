CREATE OR REPLACE FUNCTION find_blacklist (
    p_token text
)
RETURNS TABLE (hits bigint)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        COUNT(b.id)
    FROM black_lists AS b
    WHERE b.token = p_token;
END $$;
