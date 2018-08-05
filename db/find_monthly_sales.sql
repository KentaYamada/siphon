CREATE OR REPLACE FUNCTION find_monthly_sales(
    sales_month text
)
RETURNS TABLE (
    sales_date timestamp,
    sales_day integer,
    total_price
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    sales_date_from timestamp with time zone;
    sales_date_to timestamp with time zone;
BEGIN
    RETURN QUERY
    SELECT
        s.sales_date
        SUM(CASE
          WHEN s.discount_price > 0 THEN
            s.total_price - s.discount_price
          WHEN s.discount_rate > 0 THEN
            s.total_price - (s.total_price * (100 / s.discount_rate))
        END) AS total_price
    FROM sales AS s
    GROUP BY
        s.sales_date
    WHERE s.sales_date >= sales_date_from
      AND s.sales_date <= sales_date_to;
    ORDER BY
        s.sales_date
END $$;
