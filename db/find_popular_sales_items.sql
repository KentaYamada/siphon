CREATE OR REPLACE FUNCTION find_popular_sales_items (
    p_start_date date,
    p_end_date date
)
RETURNS TABLE(rank_no bigint, item_name text, quantity bigint)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        RANK() OVER (ORDER BY SUM(si.quantity) DESC) AS rank_no,
        si.item_name,
        SUM(si.quantity) AS quantity
    FROM sales AS s
    INNER JOIN sales_items AS si ON s.id = si.sales_id
    WHERE s.sales_date <= p_start_date
      AND s.sales_date >= p_end_date
    GROUP BY
        si.item_name
    ORDER BY
        rank_no ASC,
        si.item_name ASC;
END $$;
