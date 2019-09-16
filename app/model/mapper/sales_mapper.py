from datetime import datetime
from calendar import TextCalendar
from app.model.sales import Sales
from app.model.daily_sales import DailySalesSearchOption
from app.model.monthly_sales import MonthlySalesSearchOption
from app.model.mapper.base_mapper import BaseMapper


class SalesMapper(BaseMapper):
    SATURDAY = 5
    SUNDAY = 6
    DAILY_SALES_URL = '/sales/daily?sales_date={0}'

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
        for row in rows:
            row['sales_date'] = row['sales_date'].strftime('%Y年%m月%d日')
            row['sales_time'] = row['sales_time'].strftime('%H:%M:%S')
        fields = [
            'id',
            'sales_date',
            'sales_time',
            'total_price',
            'discount_mode',
            'discount',
            'deposit',
            'grand_total',
            'canceled'
        ]
        daily_sales = self.format_rows(rows, fields)
        for d in daily_sales:
            d['is_red'] = True if d['grand_total'] < 0 else False
        return daily_sales

    def find_monthly_sales(self, year, month, option):
        if option is None or not isinstance(option, MonthlySalesSearchOption):
            raise ValueError()
        data = (
            option.sales_date_from,
            option.sales_date_to
        )
        rows = []
        try:
            rows = self._db.find_proc('find_monthly_sales', data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            # todo: logging
            # print(e)
        fields = ['sales_date', 'sales_day', 'total_price']
        return self.__format_calendar(
            year,
            month,
            self.format_rows(rows, fields)
        )

    def __format_calendar(self, year, month, rows):
        """ カレンダー形式のレスポンスに整形 """
        # 日曜始まり
        cl = TextCalendar(firstweekday=6)
        # 週単位での日付と曜日を取得
        weeks = cl.monthdays2calendar(year, month)
        res = []

        for week in weeks:
            week_data = []
            for day in week:
                current_date, weekday = day
                day_data = {
                    'sales_date': current_date,
                    'sales_day': None,
                    'amount': None,
                    'is_saturday': (weekday == self.SATURDAY),
                    'is_holiday': (weekday == self.SUNDAY),
                    'daily_sales_url': ''
                }
                if rows is not None:
                    # todo: スマートに書きたい
                    data = next((row for row in rows if row['sales_day'] == current_date), None)
                    if data is not None:
                        sales_day = data['sales_date'].strftime('%Y-%m-%d')
                        day_data['sales_day'] = sales_day
                        day_data['amount'] = int(data['total_price'])
                        day_data['daily_sales_url'] = self.DAILY_SALES_URL.format(sales_day)
                week_data.append(day_data)
            res.append(week_data)
        return res
