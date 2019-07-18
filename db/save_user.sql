CREATE OR REPLACE FUNCTION save_user(
    p_id integer,
    p_name text,
    p_nickname text,
    p_email text,
    p_password text
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    IF p_id IS NOT NULL THEN
        UPDATE users SET
            name = p_name,
            nickname = p_nickname,
            email = p_email,
            password = p_password
        WHERE id = p_id;
    ELSE
        INSERT INTO users (
            name,
            nickname,
            email,
            password
        ) VALUES (
            p_name,
            p_nickname,
            p_email,
            p_password
        );
    END IF;
END $$;
