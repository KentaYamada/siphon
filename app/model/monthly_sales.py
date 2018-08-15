import calendar
# import datetime


class MonthlySales():
    def __init__(self):
        self.sales_date = None
        self.sales_proceeds = None

    def findBy(self, year, month):
        calendar.setfirstweekday(calendar.SUNDAY)
        current = calendar.monthcalendar(year, month)
        monthly_sales = []

        for days in current:
            week = [{'sales_date': day, 'amount': 100} for day in days]
            monthly_sales.append(week)
        return monthly_sales
