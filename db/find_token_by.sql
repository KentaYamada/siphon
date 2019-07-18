CREATE OR REPLACE FUNCTION find_token_by (
    p_token text,
    p_access_date date
)
RETURNS TABLE(user_id integer, token text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        t.user_id,
        t.token
    FROM tokens AS t
    WHERE t.token = p_token
      AND t.expired >= p_access_date;
END $$;
