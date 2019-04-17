CREATE OR REPLACE FUNCTION find_items(
    p_category_id integer,
    p_keyword text
)
RETURNS SETOF items
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        i.id,
        i.category_id,
        i.name,
        i.unit_price
    FROM items AS i
    WHERE (i.category_id = p_category_id OR p_category_id IS NULL)
      AND (
        p_keyword IS NULL OR
        p_keyword = '' OR
        i.name LIKE '%' || p_keyword || '%');
END $$;
