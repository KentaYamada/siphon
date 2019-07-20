CREATE OR REPLACE FUNCTION find_current_tax_rate (
    p_current_date date
)
RETURNS SETOF tax_rates
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        t.id,
        t.rate,
        t.reduced_rate,
        t.start_date,
        t.end_date,
        t.tax_type
    FROM tax_rates AS t
    WHERE t.start_date <= p_current_date
      AND t.end_date >= p_current_date;
END $$;
