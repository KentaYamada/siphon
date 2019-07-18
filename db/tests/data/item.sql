/**
 * 商品テストデータ作成
 */
CREATE OR REPLACE FUNCTION create_test_data_items()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO items
        (category_id, name, unit_price)
    VALUES
        (1, 'gamoyonランチ', 980),
        (1, 'パスタランチ', 900),
        (1, 'オムライスランチ', 900),
        (2, 'サイフォンコーヒー', 470),
        (2, 'カフェオレ', 520),
        (2, '紅茶', 470),
        (3, '照り焼きサンド', 750),
        (3, 'カフェパスタ', 830),
        (3, 'ガモヨンカレー', 980);
END $$;
