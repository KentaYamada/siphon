-- テストデータ投入
SELECT create_test_data_tax_rates();

-- 税率取得
SELECT find_current_tax_rate();

-- データリセット
TRUNCATE TABLE tax_rates RESTART IDENTITY;
