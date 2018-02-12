DROP FUNCTION IF EXISTS cancel_sales(integer);

CREATE OR REPLACE FUNCTION cancel_sales(p_sales_no integer)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO sales (
        sales_date
       ,total
       ,discount_price
       ,discount_rate
       ,inclusive_tax
       ,external_tax
       ,deposit
    )
    SELECT
        s.sales_date
       ,s.total * (-1)
       ,case
          when s.discount_price > 0 then s.discount_price * (-1)
          else 0
        end
       ,s.discount_rate
       ,s.inclusive_tax
       ,s.external_tax
       ,s.deposit * (-1)
    FROM sales AS s
    WHERE s.no = p_sales_no;
END $$;
