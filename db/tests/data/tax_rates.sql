CREATE OR REPLACE FUNCTION create_test_data_tax_rates()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    max_end_date CONSTANT date := '9999/12/31';
BEGIN
    INSERT INTO tax_rates (
        rate,
        reduced_rate,
        start_date,
        end_date,
        tax_type
    ) VALUES (
        10,
        8,
        CURRENT_DATE,
        max_end_date,
    1);
END $$;
