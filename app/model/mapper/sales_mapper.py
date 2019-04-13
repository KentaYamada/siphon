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
        sales_data = (
            sales.sales_date,
            sales.sales_time,
            sales.total_price,
            sales.discount_price,
            sales.discount_rate,
            sales.inclusive_tax,
            sales.exclusive_tax,
            sales.deposit
        )

        try:
            # 売上データ登録
            affected_row = self._db.execute_proc('save_sales', sales_data)
            if affected_row < 1:
                self._db.rollback()
                return False

            # 売上明細データ登録
            sales_id = self._db.fetch_last_row_id()
            for item in sales.items:
                item_data = (
                    sales_id,
                    item.item_no,
                    item.item_name,
                    item.unit_price,
                    item.quantity,
                    item.subtotal
                )
                affected_row = self._db.execute_proc('save_sales_item', item_data)
                if affected_row < 1:
                    self._db.rollback()
                    return False
            self._db.commit()
            saved = True
        except Exception as e:
            # todo: logging
            print(e)
            self._db.rollback()
            saved = False
        return saved

    def cancel(self, sales_id):
        if sales_id is None or not isinstance(sales_id, int):
            raise ValueError()
        if sales_id <= 0:
            raise ValueError('Invalid sales_id')
        try:
            self._db.execute_proc('save_cancel_sales', (sales_id,))
            self._db.commit()
            saved = True
        except Exception as e:
            # todo: logging
            print(e)
            self._db.rollback()
            saved = False
        return saved

    def find_daily_sales(self, sales_date):
        if sales_date is None or not isinstance(sales_date, datetime.datetime):
            raise ValueError()
        query = """
            SELECT
                id,
                sales_date,
                total_price,
                CASE
                    WHEN discount_price > 0 THEN
                        discount_rate
                    WHEN discount_rate > 0 THEN
                        discount_rate
                    ELSE
                        NULL
                END AS discount,
                CASE
                    WHEN discount_price > 0 THEN
                        total_price - discount_price
                    WHEN discount_rate > 0 THEN
                        total_price * (1 - (discount_rate * 1.0) / 100)
                    ELSE
                        total_price
                END AS proceeds
            FROM sales
            WHERE sales_date <= %s
              AND sales_date < %s
            ORDER BY sales_date ASC;
        """
        data = (
        )
        rows = None
        try:
            rows = self._db.find(query, data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        if rows is None or len(rows) != 0:
            rows = []
        return rows

    def find_monthly_sales(self, year, month):
        if year is None or not isinstance(year, int):
            raise ValueError('Invalid data type: year')
        if month is None or not isinstance(month, int):
            raise ValueError('Invalid data type: month')
        if month < 1 or month > 12:
            raise ValueError('Invalid period of month')
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
