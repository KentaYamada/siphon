DROP FUNCTION IF EXISTS find_by_products(integer);

CREATE OR REPLACE FUNCTION find_by_products(p_category_id integer)
RETURNS TABLE(id integer, category_id integer, name text, price integer)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.id
       ,p.category_id
       ,p.name
       ,p.price
    FROM products AS p
    WHERE p.category_id = p_category_id;
END $$;
