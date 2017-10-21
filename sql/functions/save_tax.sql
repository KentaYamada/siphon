CREATE OR REPLACE FUNCTION save_tax(p_rate integer, p_type text)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  DELETE FROM tax;
  INSERT INTO tax (
      rate
     ,tax_type
  ) VALUES (
      p_rate
     ,p_type
  );
END $$;
