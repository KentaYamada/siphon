DROP FUNCTION IF EXISTS find_daily_sales(date);

CREATE OR REPLACE FUNCTION find_daily_sales(sales_date date)
RETURNS TABLE(
    sales_date timestamp
    total
   ,discount
   ,tax
   ,amount
   ,item_name  text
   ,price
   ,quantity
   ,subtotal
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
END $$;
