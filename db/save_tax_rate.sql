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
    max_end_date CONSTANT date := '9999/12/31'
BEGIN
    -- todo: レコードあるか確認(新規の場合を考慮)
    -- 適用中の適用終了日を適用開始日-1日に更新
    UPDATE tax_rates SET
        end_date = p_start_date - integer '1'
    WHERE end_date = max_end_date;

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
        tax_type
    );
END $$;
