CREATE OR REPLACE FUNCTION create_test_data_daily_sales_items()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
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
    ) VALUES
    (CURRENT_DATE, CURRENT_TIME::time, 800, 0, 0, 0, 0, 800, false),
    (CURRENT_DATE, CURRENT_TIME::time, 1900, 0, 0, 0, 0, 1900, false),
    (CURRENT_DATE+1, CURRENT_TIME::time, 1250, 0, 0, 0, 0, 1250, false);

    INSERT INTO sales_items (
        sales_id,
        item_no,
        item_name,
        unit_price,
        quantity,
        subtotal
    ) VALUES
    (1, 1, 'Siphon Coffee', 450, 1, 450),
    (1, 2, 'ケーキ350', 350, 1, 350),
    (2, 1, 'パスタセット', 1000, 1, 1000),
    (2, 2, 'Siphon Coffee', 450, 2, 900),
    (3, 1, 'Gamoyonカレー', 800, 1, 800),
    (3, 2, '紅茶', 450, 1, 450);
END $$;
