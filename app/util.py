# -*- coding: utf-8 -*-


def to_dimention_array(arr, row, col):
    # 一次元配列から二次元配列へ変換
    res = []
    offset = 0

    for i in range(0, row):
        res.append(arr[offset:col+offset])
        offset += col
    return res


def get_dummy():
    # 売上登録で利用する商品リストのダミーデータ生成
    res = []
    product_id = 1

    for i in range(1, 11):
        category = {
            "id": i,
            "name": "Category{0}".format(i),
            "products": []
        }

        for j in range(1, 31):
            category['products'].append({
                "id": product_id,
                "name": "Product{0}".format(product_id),
                "price": j * 100
            })
            product_id += 1
        category['products'] = to_dimention_array(category['products'], 10, 3)
        res.append(category)

    res = to_dimention_array(res, 2, 5)
    return res
