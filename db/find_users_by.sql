CREATE OR REPLACE FUNCTION find_users_by(
    p_keyword text
)
RETURNS TABLE(id integer, name text, nickname text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        u.id,
        u.name,
        u.nickname
    FROM users AS u
    WHERE p_keyword IS NULL
       OR p_keyword = ''
       OR u.name LIKE '%' || p_keyword || '%'
       OR u.nickname LIKE '%' || p_keyword || '%'
    ORDER BY u.id ASC;
END $$;
