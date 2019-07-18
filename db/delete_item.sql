CREATE OR REPLACE FUNCTION delete_item(
    p_id integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    DELETE FROM items WHERE id = p_id;
END $$;
