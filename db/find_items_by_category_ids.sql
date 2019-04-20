CREATE OR REPLACE FUNCTION find_items_by_category_ids(
    p_category_ids int[]
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
    WHERE i.category_id = ANY(p_category_ids);
END $$;

