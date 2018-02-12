DROP FUNCTION IF EXISTS find_by_yearly_sales(text);

CREATE OR REPLACE FUNCTION find_by_yearly_sales(p_year text)
RETURNS TABLE(sales_month text, amount bigint)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    month_from date := to_date(p_year || '-01-01', 'YYYY-MM-DD');
    month_to date := to_date(p_year || '-12-31', 'YYYY-MM-DD');
BEGIN
    RETURN QUERY
    SELECT
        to_char(s.sales_date, 'YYYY') AS sales_month
       ,SUM(s.amount) AS amount
    FROM monthly_sales AS s
    WHERE s.sales_date BETWEEN month_from AND month_to
    GROUP BY to_char(s.sales_date, 'YYYY')
    ORDER BY to_char(s.sales_date, 'YYYY');
END $$;
