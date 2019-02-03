from app.model.mapper.base_mapper import BaseMapper
from app.model.sales_item import SalesItem


class SalesItemMapper(BaseMapper):
    def __init__(self):
        super().__init__()

    def find_by_sales_ids(self, sales_ids):
        if sales_ids is None or len(sales_ids) == 0:
            raise ValueError()
        if not isinstance(sales_ids, list):
            raise ValueError()
        if sum(1 for i in sales_ids if not isinstance(i, int)) > 0:
            raise ValueError('sales_ids include invalid data type')
        if sum(1 for i in sales_ids if i <= 0) > 0:
            raise ValueError('sales_ids include invalid value')
        query = """
            SELECT
                sales_id,
                item_no,
                item_name,
                unit_price,
                quantity,
                subtotal
            FROM sales_items
            WHERE sales_id IN %s
            ORDER BY item_no ASC;
        """
        rows = None
        try:
            rows = self._db.find(query, (tuple(sales_ids),))
            self._db.commit()
        except Exception as e:
            # todo: logging
            print(e)
            self._db.rollback()
        if rows is not None:
            rows = [SalesItem(
                None,
                row['sales_id'],
                row['item_no'],
                row['item_name'],
                row['unit_price'],
                row['quantity'],
                row['subtotal'])
                for row in rows]
        return rows

    def find_popular_items(self, sales_ids):
        if sales_ids is None or not isinstance(sales_ids, list):
            raise ValueError()
        if len(sales_ids) == 0:
            raise ValueError()
        query = """
            SELECT
                item_name,
                SUM(quantity) AS quantity
            FROM sales_items
            WHERE sales_id IN %s
            GROUP BY item_name
            LIMIT 10;
        """

        try:
            self._db.find(query, (tuple(sales_ids),))
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        return [
            {'rank': i, 'item': 'test {}'.format(i)}
            for i in range(1, 11)
        ]
