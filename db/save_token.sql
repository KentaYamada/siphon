CREATE OR REPLACE FUNCTION save_token (
    p_user_id integer,
    p_token text,
    p_expired date
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO tokens (
        user_id,
        token,
        expired
    ) VALUES (
        p_user_id,
        p_token,
        p_expired
    );
END $$;
