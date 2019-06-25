CREATE OR REPLACE FUNCTION find_logged_in_user_token (
    p_user_id integer
)
RETURNS TABLE(token text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        t.token
    FROM tokens AS t
    WHERE t.user_id = p_user_id;
END $$;

