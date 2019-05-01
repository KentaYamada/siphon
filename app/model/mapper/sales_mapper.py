from calendar import TextCalendar
from app.model.sales import Sales
from app.model.daily_sales import DailySalesSearchOption
from app.model.monthly_sales import MonthlySalesSearchOption
from app.model.mapper.base_mapper import BaseMapper


class SalesMapper(BaseMapper):
    SATURDAY = 5
    SUNDAY = 6

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
                affected_row = self._db.execute_proc(
                    'save_sales_item',
                    item_data
                )
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

    def find_daily_sales(self, option):
        if option is None or not isinstance(option, DailySalesSearchOption):
            raise ValueError()
        data = (
            option.sales_date,
            option.start_time,
            option.end_time
        )
        rows = []
        try:
            rows = self._db.find_proc('find_daily_sales', data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
        fields = [
            'sales_date',
            'sales_time',
            'total_price',
            'discount_mode',
            'discount',
            'deposit',
            'grand_total'
        ]
        daily_sales = self.format_rows(rows, fields)
        return daily_sales

    # def find_monthly_sales(self, option):
    #     if option is None or not isinstance(option, MonthlySalesSearchOption):
    #         raise ValueError()
    #     data = (
    #         option.sales_date_from,
    #         option.sales_date_to
    #     )
    #     rows = []
    #     try:
    #         rows = self._db.find_proc('find_monthly_sales', data)
    #         self._db.commit()
    #     except Exception as e:
    #         self._db.rollback()
    #         # todo: logging
    #         print(e)
    #     fields = ['sales_date', 'sales_day', 'total_price']
    #     rows = self.format_rows(rows, fields)
    #     if len(rows) > 0:
    #         rows = self.__format_calendar(rows)
    #     return rows

    # def __format_calendar(self, year, month, rows):
    #     """ カレンダー形式のレスポンスに整形 """
    #     # 日曜始まり
    #     cl = TextCalendar(firstweekday=6)
    #     # 週単位での日付と曜日を取得
    #     weeks = cl.monthdays2calendar(year, month)
    #     res = []

    #     for week in weeks:
    #         week_data = []
    #         for day in week:
    #             current_date, weekday = day
    #             data = next(
    #                 (row for row in rows if row['sales_day'] == current_date),
    #                 None
    #             )
    #             is_saturday = True if weekday == self.SATURDAY else False
    #             is_sunday = True if weekday == self.SUNDAY else False
    #             sales_date = data['sales_date'] if data is not None else None
    #             total_price = data['total_price'] if data is not None else None
    #             week_data.append({
    #                 'sales_date': sales_date,
    #                 'sales_day': current_date,
    #                 'total_price': total_price,
    #                 'is_saturday': is_saturday,
    #                 'is_sunday': is_sunday
    #             })
    #         res.append(week_data)
    #     return res
