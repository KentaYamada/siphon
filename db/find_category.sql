CREATE OR REPLACE FUNCTION find_categories()
RETURNS TABLE(id integer, name text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name
    FROM categories AS c;
END $$;
