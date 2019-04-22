-- データ作成
SELECT create_test_data_daily_sales();

-- 検索(時間指定なし)
SELECT find_daily_sales(CURRENT_DATE, NULL, NULL);

-- 検索(From指定)
SELECT find_daily_sales(CURRENT_DATE, '10:00:00'::time, NULL);

-- 検索(To指定)
SELECT find_daily_sales(CURRENT_DATE, NULL, '11:00:00'::time);

-- 検索(From / To指定)
SELECT find_daily_sales(CURRENT_DATE, '10:00:00'::time, '11:00:00'::time);

-- データリセット
TRUNCATE TABLE sales RESTART IDENTITY;
