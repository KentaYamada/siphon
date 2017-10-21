CREATE OR REPLACE FUNCTION save_category(p_id integer, p_name text)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
   IF p_id IS NOT NULL THEN
       UPDATE categories SET
           name = p_name
       WHERE id = p_id;
   ELSE
       INSERT INTO categories (name) VALUES(p_name);
   END IF;
END $$;
