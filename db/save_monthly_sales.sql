CREATE OR REPLACE FUNCTION save_monthly_sales(
    p_sales_id integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    DATE_FORMAT CONSTANT text := 'YYYY/MM/DD';
    has_row: integer;
BEGIN
    INSERT INTO monthly_sales (
        sales_date,
        proceeds
    )
    SELECT
        TO_DATE(TO_CHAR(s.sales_date, DATE_FORMAT), DATE_FORMAT),
        CASE
          WHEN s.discount_price > 0 THEN
              s.total_price - s.discount_price
          WHEN s,discount_rate > 0 THEN
              s.discount_price * (1 - s.discount_rate / 100)
        END AS proceeds
    FROM sales AS s
    WHERE s.id = p_sales_id;
END $$;

