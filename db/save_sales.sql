CREATE OR REPLACE FUNCTION save_sales (
    p_sales_date date,
    p_sales_time time,
    p_total_price integer,
    p_dicount_price integer,
    p_discount_rate integer,
    p_inclusive_tax integer,
    p_exclusive_tax integer,
    p_deposit integer
)
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
    ) VALUES (
        p_sales_date,
        p_sales_time,
        p_total_price,
        p_dicount_price,
        p_discount_rate,
        p_inclusive_tax,
        p_exclusive_tax,
        p_deposit,
        false
    );
END $$;
