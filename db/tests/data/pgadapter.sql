CREATE OR REPLACE FUNCTION create_test_data_pgadapter()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO car_makers (name)
    VALUES
        ('toyota'),
        ('nissan'),
        ('honda');

    INSERT INTO cars (maker_id, name)
    VALUES
        (1, 'カローラ'),
        (1, 'クレスタ'),
        (1, '86'),
        (2, 'スカイライン'),
        (2, 'フェアレディZ'),
        (2, 'マーチ'),
        (3, 'Civic'),
        (3, 'S2000'),
        (3, 'フリード');
END $$;
