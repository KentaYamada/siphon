CREATE OR REPLACE FUNCTION find_current_tax(
    p_current_date date
)
RETURNS SETOF tax_rates
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
    RETURN QUERY
    SELECT
        t.rate,
        t.reduced_rate,
        t.tax_type
    FROM tax_rates AS t
    WHERE t.start_date <= p_current_date
      AND t.end_date > p_current_date;
END $$;
