CREATE OR REPLACE FUNCTION save_tax_rate(
    p_rate integer,
    p_reduced_rate integer,
    p_start_date date,
    p_tax_type integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    has_tax_rate bigint := 0;
    max_end_date CONSTANT date := '9999/12/31';
BEGIN
    has_tax_rate := (SELECT COUNT(*) FROM tax_rates WHERE end_date = max_end_date);

    IF has_tax_rate = 1 THEN
        -- 適用中の適用終了日を適用開始日-1日に更新
        UPDATE tax_rates SET
            end_date = p_start_date - integer '1'
        WHERE end_date = max_end_date;
    END IF;

    INSERT INTO tax_rates (
        rate,
        reduced_rate,
        start_date,
        end_date,
        tax_type
    ) VALUES (
        p_rate,
        p_reduced_rate,
        p_start_date,
        max_end_date,
        p_tax_type
    );
END $$;
