CREATE OR REPLACE FUNCTION create_test_data_daily_sales()
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
    (CURRENT_DATE, '09:00:00'::time, 800, 0, 0, 0, 0, 800, false),
    (CURRENT_DATE, '10:00:00'::time, 1900, 0, 0, 0, 0, 1900, false),
    (CURRENT_DATE, '11:00:00'::time, 1200, 200, 0, 0, 0, 1000, false),
    (CURRENT_DATE, '12:00:00'::time, 3000, 0, 20, 0, 0, 2400, false),
    (CURRENT_DATE+1, '10:00:00'::time, 900, 0, 0, 0, 0, 900, false);
END $$;
