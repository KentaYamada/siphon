CREATE OR REPLACE FUNCTION delete_user(
    p_id integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    DELETE FROM users WHERE id = p_id;
END $$;
