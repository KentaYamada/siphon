CREATE OR REPLACE FUNCTION save_product(p_id integer, p_category_id integer, p_name text, p_price integer)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
   IF p_id IS NOT NULL THEN
       UPDATE products SET
            category_id = p_category_id
           ,name = p_name
           ,price = p_price
       WHERE id = p_id;
   ELSE
       INSERT INTO products (
             category_id
            ,name
            ,price
        ) VALUES(
             p_category_id
            ,p_name
            ,p_price
        );
   END IF;
END $$;
