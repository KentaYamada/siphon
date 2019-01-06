import datetime
from app.model.sales import Sales
from app.model.monthly_sales import MonthlySales
from app.model.mapper.base_mapper import BaseMapper


class SalesMapper(BaseMapper):
    def __init__(self):
        super().__init__()

    def add(self, sales):
        if sales is None or not isinstance(sales, Sales):
            raise ValueError()
        if not sales.is_valid():
            return False
        sales_query = """
            INSERT INTO sales (
                sales_date,
                total_price,
                discount_price,
                discount_rate,
                inclusive_tax,
                exclusive_tax,
                deposit
            ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );

        """
        sales_item_query = """
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
        sales_data = (
            sales.sales_date,
            sales.total_price,
            sales.discount_price,
            sales.discount_rate,
            sales.inclusive_tax,
            sales.exclusive_tax,
            sales.deposit
        )

        try:
            self._db.execute(sales_query, sales_data)
            sales_id = self._db.fetch_last_row_id()
            sales_item_data = tuple([(
                sales_id,
                item.item_no,
                item.item_name,
                item.unit_price,
                item.quantity,
                item.subtotal
            ) for item in sales.items])
            self._db.bulk_insert(sales_item_query, sales_item_data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.commit()
            print(e)
            saved = False
        return saved

    def cancel(self, sales_id):
        if sales_id is None or not isinstance(sales_id, int):
            raise ValueError()
        if sales_id <= 0:
            raise ValueError('Invalid sales_id')

        data = (sales_id,)
        try:
            self._db.execute_proc('save_cancel_sales', data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            print(e)
            saved = False
        return saved

    def find_monthly_sales(self, year, month):
        if year is None or not isinstance(year, int):
            raise ValueError()
        if month is None or not isinstance(month, int):
            raise ValueError()
        if month < 1 or month > 12:
            raise ValueError('Invalid month')
        query = """
            SELECT
                s.sales_date,
                to_char(s.sales_date, 'DD') as sales_day,
                SUM(
                    CASE
                      WHEN s.discount_price > 0 THEN
                        s.total_price - s.discount_price
                      WHEN s.discount_rate > 0 THEN
                        s.total_price * (1 - (s.discount_rate * 1.0) / 100)
                      ELSE
                        s.total_price
                    END
                ) AS proceeds
            FROM sales AS s
            WHERE sales_date >= %s
              AND sales_date < %s
            GROUP BY s.sales_date
            ORDER BY s.sales_date ASC;
        """
        data = (
            datetime.datetime(year, month, 1, 0, 0, 0),
            datetime.datetime(year, month+1, 1, 0, 0, 0)
        )
        rows = None

        try:
            rows = self._db.find(query, data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)

        rows = [MonthlySales(
            row['sales_date'],
            row['sales_day'],
            row['proceeds'])
            for row in rows]
        return rows

    def find_yearly_sales(self, year):
        if year is None or not isinstance(year, int):
            raise ValueError()
        query = """
            SELECT
                *
            FROM sales
            WHERE sales_date >= %s
              AND sales_date < %s;
        """
        data = (
            datetime.datetime(year, 1, 1, 0, 0, 0),
            datetime.datetime(year+1, 1, 1, 0, 0, 0)
        )
        rows = None
        try:
            rows = self._db.find(query, data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        return rows
