CREATE OR REPLACE FUNCTION find_categories(p_keyword text)
RETURNS TABLE(id integer, name text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name
    FROM categories AS c
    WHERE p_keyword IS NULL
       OR p_keyword = ''
       OR c.name like '%' || p_keyword || '%';
END $$;
