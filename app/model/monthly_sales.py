
class MonthlySales():
    WEEKDAY = {
        0: 'Mon',
        1: 'Tue',
        2: 'Wed',
        3: 'Thu',
        4: 'Fri',
        5: 'Sat',
        6: 'Sun'
    }

    def __init__(self, sales_date, sales_day, proceeds):
        self.__sales_date = sales_date
        self.__sales_day = sales_day
        self.__weekday = self.__get_weekday(self.__sales_date)
        self.__proceeds = proceeds

    @property
    def sales_date(self):
        return self.__sales_date

    @property
    def sales_day(self):
        return self.__sales_day

    @property
    def weekday(self):
        return self.__weekday

    @property
    def proceeds(self):
        return self.__proceeds

    def __get_weekday(cls, target_date):
        weekday = target_date.weekday()
        return MonthlySales.WEEKDAY[weekday]


class MonthlySalesSearchOption:
    def __init__(self, sales_date_from, sales_date_to):
        self.sales_date_from = sales_date_from
        self.sales_date_to = sales_date_to
