from app.model.mapper.base_mapper import BaseMapper
from app.model.sales_item import SalesItem


class SalesItemMapper(BaseMapper):
    def __init__(self):
        super().__init__()

    def find_by_sales_id(self, sales_id):
        if sales_id is None:
            raise ValueError()
        if not isinstance(sales_id, int):
            raise ValueError()
        if sales_id < 0:
            raise ValueError()
        query = """
            SELECT
                sales_id,
                item_no,
                item_name,
                unit_price,
                quantity,
                subtotal
            FROM sales_items
            WHERE sales_id = %s
            ORDER BY sales_id ASC;
        """
        rows = None
        data = (sales_id,)
        try:
            rows = self._db.find(query, data)
            self._db.commit()
            print(rows)
        except Exception as e:
            # todo: logging
            print(e)
            print('hoge')
            self._db.rollback()
        if rows is None:
            return rows
        return [SalesItem(
            None,
            row['sales_id'],
            row['item_no'],
            row['item_name'],
            row['unit_price'],
            row['quantity'],
            row['subtotal'])
            for row in rows]
