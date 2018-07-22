CREATE OR REPLACE FUNCTION find_users_by(
    p_keyword text
)
RETURNS TABLE(id integer, name text, nickname text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    IF p_keyword IS NOT NULL THEN
        p_keyword := '%' || p_keyword || '%';
    END IF;

    RETURN QUERY
    SELECT
        u.id,
        u.name,
        u.nickname
    FROM users AS u
    WHERE p_keyword IS NULL
       OR u.name LIKE p_keyword
       OR u.nickname LIKE p_keyword;
END $$;
