DROP FUNCTION IF EXISTS find_tax();

CREATE OR REPLACE FUNCTION find_tax()
RETURNS TABLE(rate integer, tax_type text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        t.rate
       ,t.tax_type
    FROM tax AS t;
END $$;
