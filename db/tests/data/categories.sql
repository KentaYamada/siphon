/**
 * 商品カテゴリテストデータ作成
 */
CREATE OR REPLACE FUNCTION create_test_data_categories()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO categories
        (name)
    VALUES
        ('モーニングセット'),
        ('ランチセット'),
        ('ディナー'),
        ('ソフトドリンク'),
        ('アルコール'),
        ('ケーキ'),
        ('食事単品'),
        ('雑貨'),
        ('委託販売'),
        ('その他');
END $$;
