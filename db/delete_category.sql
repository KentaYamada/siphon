CREATE OR REPLACE FUNCTION delete_category(
    p_id integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    DELETE FROM categories WHERE id = p_id;
END $$
