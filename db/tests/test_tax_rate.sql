-- 新規作成
SELECT save_tax_rate(10, 8, CURRENT_DATE, 1);

-- 登録確認
SELECT * FROM tax_rates;

-- 税率更新
SELECT save_tax_rate(12, 10, '2022-10-01', 1);

-- 登録確認
SELECT * FROM tax_rates;

-- データリセット
TRUNCATE TABLE tax_rates RESTART IDENTITY;
