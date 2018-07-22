CREATE OR REPLACE FUNCTION save_item(
    p_id integer,
    p_category_id integer,
    p_name text,
    p_unit_price integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    IF p_id IS NOT NULL THEN
        UPDATE items SET
            category_id = p_category_id,
            name = p_name,
            unit_price = p_unit_price
        WHERE id = p_id;
    ELSE
        INSERT INTO items (
            category_id,
            name,
            unit_price
        ) VALUES (
            p_category_id,
            p_name,
            p_unit_price
        );
    END IF;
END $$;
