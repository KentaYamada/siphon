CREATE OR REPLACE FUNCTION save_sales_item (
    p_sales_id integer,
    p_item_no integer,
    p_item_name text,
    p_unit_price integer,
    p_quantity integer,
    p_subtotal integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO sales_items (
        sales_id,
        item_no,
        item_name,
        unit_price,
        quantity,
        subtotal
    ) VALUES (
        p_sales_id,
        p_item_no,
        p_item_name,
        p_unit_price,
        p_quantity,
        p_subtotal
    );
END $$;
