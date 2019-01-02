from app.model.mapper.base_mapper import BaseMapper
from app.model.sales_item import SalesItem


class SalesItemMapper(BaseMapper):
    def __init__(self):
        super().__init__()

    def add_items(self, sales_items):
        if sales_items is None:
            raise ValueError()
        if not isinstance(sales_items, list):
            raise ValueError()
        if len(sales_items) == 0:
            return False
        query = """
            INSERT INTO sales_items (
                sales_id,
                item_no,
                item_name,
                unit_price,
                quantity,
                subtotal
            ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
        """
        data = tuple([(
            item.sales_id,
            item.item_no,
            item.item_name,
            item.unit_price,
            item.quantity,
            item.subtotal)
            for item in sales_items])
        saved = True
        try:
            self._db.bulk_insert(query, data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            saved = False
        return saved

    def cancel(self, sales_id, cancel_sales_id):
        ids = (sales_id, cancel_sales_id)
        for id in ids:
            if id is None:
                raise ValueError()
            if not isinstance(id, int):
                raise ValueError()
            if id < 0:
                raise ValueError()
        query = """
            INSERT INTO sales_items (
                sales_id,
                item_no,
                item_name,
                unit_price,
                quantity,
                subtotal
            )
            SELECT
                %s,
                item_no,
                item_name,
                unit_price * (-1),
                quantity * (-1),
                subtotal * (-1)
            FROM sales_items
            WHERE sales_id = %s;
        """
        canceled = False
        try:
            self._db.execute(query, (sales_id, cancel_sales_id))
            self._db.commit()
            canceled = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            canceled = False
        return canceled

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
