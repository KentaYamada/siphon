CREATE OR REPLACE FUNCTION find_auth_user(
    p_email text,
    p_password text
)
RETURNS SETOF users
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        u.id,
        u.name,
        u.nickname,
        u.email,
        u.password
    FROM users AS u
    WHERE u.email = p_email
      AND u.password = p_password;
END $$;

