CREATE OR REPLACE FUNCTION find_monthly_sales(
    start_date date,
    end_date date
)
RETURNS TABLE (
    sales_date date,
    sales_day integer,
    total_price numeric
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.sales_date,
        to_char(s.sales_date, 'DD')::int,
        SUM(CASE
              WHEN s.discount_price > 0 THEN
                s.total_price - s.discount_price
              WHEN s.discount_rate > 0 THEN
                s.total_price * (1 - (s.discount_rate * 1.0) / 100)
              ELSE
                s.total_price
            END
        ) AS total_price
    FROM sales AS s
    WHERE s.sales_date >= start_date
      AND s.sales_date <= end_date
    GROUP BY
        s.sales_date
    ORDER BY
        s.sales_date ASC;
END $$;
