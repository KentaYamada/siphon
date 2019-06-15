CREATE OR REPLACE FUNCTION save_cancel_sales (
    p_id integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    cancel_sales_id integer;
BEGIN
    -- 取り消し元データを取消済にする
    UPDATE sales SET
        canceled = true
    WHERE id = p_id;

    -- 取消データ作成
    INSERT INTO sales (
        sales_date,
        sales_time,
        total_price,
        discount_price,
        discount_rate,
        inclusive_tax,
        exclusive_tax,
        deposit,
        canceled
    )
    SELECT
        s.sales_date,
        s.sales_time,
        s.total_price * (-1),
        s.discount_price * (-1),
        s.discount_rate,
        s.inclusive_tax,
        s.exclusive_tax,
        s.deposit * (-1),
        true
    FROM sales AS s
    WHERE s.id = p_id;

    IF FOUND THEN
        cancel_sales_id := (SELECT LASTVAL());
        INSERT INTO sales_items (
            sales_id,
            item_no,
            item_name,
            unit_price,
            quantity,
            subtotal
        )
        SELECT
            cancel_sales_id,
            s.item_no,
            s.item_name,
            s.unit_price,
            s.quantity * (-1),
            s.subtotal * (-1)
        FROM sales_items AS s
        WHERE s.sales_id = p_id;
    ELSE
        ROLLBACK;
    END IF;
END $$;
