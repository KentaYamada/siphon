CREATE OR REPLACE FUNCTION find_daily_sales(
    p_sales_date date,
    p_sales_time_start time without time zone,
    p_sales_time_end time without time zone
)
RETURNS TABLE(
    id integer,
    sales_date date,
    sales_time time without time zone,
    total_price integer,
    discount_mode integer,
    discount integer,
    grand_total integer,
    deposit integer
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.id,
        s.sales_date,
        s.sales_time,
        s.total_price,
        CASE
          -- 値引額
          WHEN s.discount_price > 0 THEN 1
          -- 値引率
          WHEN s.discount_rate > 0 THEN 2
          -- 値引なし
          ELSE 0
        END AS discount_mode,
        CASE
          WHEN s.discount_price > 0 THEN
            s.discount_price
          WHEN s.discount_rate > 0 THEN
            s.discount_rate
          ELSE 0
        END AS discount,
        CASE
          WHEN s.discount_price > 0 THEN
            s.total_price - s.discount_price
          WHEN s.discount_rate > 0 THEN
            (s.total_price * (1 - (s.discount_rate * 1.0) / 100))::integer
          ELSE s.total_price
        END AS grand_total,
        s.deposit
    FROM sales AS s
    WHERE s.sales_date = p_sales_date
      AND (s.sales_time >= p_sales_time_start OR p_sales_time_start IS NULL)
      AND (s.sales_time <= p_sales_time_end OR p_sales_time_end IS NULL)
    ORDER BY
        s.sales_date ASC;
END $$;
