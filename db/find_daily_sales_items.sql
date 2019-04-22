CREATE OR REPLACE FUNCTION find_daily_sales_items(
    p_sales_ids int[]
)
RETURNS TABLE(
    sales_id integer,
    item_no integer,
    item_name text,
    unit_price integer,
    quantity integer,
    subtotal integer
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        si.sales_id,
        si.item_no,
        si.item_name,
        si.unit_price,
        si.quantity,
        si.subtotal
    FROM sales_items AS si
    WHERE si.sales_id = ANY(p_sales_ids)
    ORDER BY
        si.sales_id ASC,
        si.item_no ASC;
END $$;
