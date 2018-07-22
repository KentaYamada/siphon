CREATE OR REPLACE FUNCTION find_items_by(
    p_category_id integer,
    p_name text
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
    WHERE i.category_id = p_category_id
      AND (
        p_name IS NULL OR
        i.name LIKE '%' || p_name || '%'
    );
END $$;
