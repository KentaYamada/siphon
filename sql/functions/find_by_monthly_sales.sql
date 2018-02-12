DROP FUNCTION IF EXISTS find_by_monthly_sales(text);

CREATE OR REPLACE FUNCTION find_by_monthly_sales(p_month text)
RETURNS TABLE(sales_date date, amount integer)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    date_from date := to_date(p_month || '-01', 'YYYY-MM-DD')
    date_to date:= to_date(p_month || '-01', 'YYYY-MM-DD')
BEGIN
    RETURN QUERY
    SELECT
        s.sales_date
       ,s.amount
    FROM montyly_sales AS s
    WHERE s.sales_date BETWEEN to_timestamp(date_from) and to_timestamp(date_to)
    ORDER BY s.sales_date;
END $$;
