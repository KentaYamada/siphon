CREATE OR REPLACE FUNCTION find_logged_in_user (
    p_token text
)
RETURNS (user_id integer)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        t.user_id
    FROM tokens AS t
    WHERE t.token = p_token;
END $$;
