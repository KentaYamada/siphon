-- 新規作成
SELECT save_sales(CURRENT_DATE, CURRENT_TIME::time, 1000, 0, 0, 0, 0, 1000);
SELECT save_sales_item(1, 1, 'Siphon coffee', 450, 1, 450);
SELECT save_sales_item(1, 2, 'ケーキ550', 550, 1, 550);

-- 売上取消
SELECT save_cancel_sales(1);

-- データ確認
SELECT * FROM sales;
SELECT * FROM sales_items;

-- データ初期化
TRUNCATE TABLE sales RESTART IDENTITY;
TRUNCATE TABLE sales_items RESTART IDENTITY;

