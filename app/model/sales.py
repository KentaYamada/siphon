import datetime
from app.model.base import BaseModel


class Sales(BaseModel):
    def __init__(
        self,
        id=None,
        sales_date=None,
        sales_time=None,
        total_price=None,
        discount_price=None,
        discount_rate=None,
        inclusive_tax=0,
        exclusive_tax=0,
        deposit=None,
        items=None,
        **kwargs
    ):
        super().__init__()
        self.id = id
        self.sales_date = sales_date
        self.sales_time = sales_time
        self.total_price = total_price
        self.discount_price = discount_price
        self.discount_rate = discount_rate
        self.inclusive_tax = inclusive_tax
        self.exclusive_tax = exclusive_tax
        self.deposit = deposit
        self.items = items

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        super()._clear_validation_error('id')
        if value is not None and not isinstance(value, int):
            super()._add_validation_error('id', 'IDには整数をセットしてください')
        else:
            self.__id = value

    @property
    def sales_date(self):
        return self.__sales_date

    @sales_date.setter
    def sales_date(self, value):
        super()._clear_validation_error('sales_date')
        if value is None:
            super()._add_validation_error(
                'sales_date',
                '売上日は必須です'
            )
        elif not isinstance(value, datetime.date):
            super()._add_validation_error(
                'sales_date',
                '売上日は日付をセットしてください'
            )
        else:
            self.__sales_date = value

    @property
    def sales_time(self):
        return self.__sales_time

    @sales_time.setter
    def sales_time(self, value):
        super()._clear_validation_error('sales_date')
        if value is None:
            super()._add_validation_error(
                'sales_time',
                '売上時間をセットしてください'
            )
        elif not isinstance(value, datetime.time):
            super()._add_validation_error(
                'sales_time',
                '売上時間のデータ型が不正です'
            )
        else:
            self.__sales_time = value

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, value):
        if value is None:
            super()._add_validation_error(
                'total_price',
                '合計金額は必須です'
            )
        elif not isinstance(value, int):
            super()._add_validation_error(
                'total_price',
                '合計金額は整数をセットしてください'
            )
        elif value <= 0:
            super()._add_validation_error(
                'total_price',
                '合計金額は0円以上をセットしてください'
            )
        else:
            self.__total_price = value

    @property
    def discount_price(self):
        return self.__discount_price

    @discount_price.setter
    def discount_price(self, value):
        if not isinstance(value, int):
            super()._add_validation_error(
                'discount_price',
                '値引額は整数をセットしてください'
            )
        else:
            self.__discount_price = value

    @property
    def discount_rate(self):
        return self.__discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        if not isinstance(value, int):
            super()._add_validation_error(
                'discount_rate',
                '値引率は整数をセットしてください'
            )
        elif value >= 100:
            super()._add_validation_error(
                'discount_rate',
                '無効な値引き率です'
            )
        else:
            self.__discount_rate = value

    @property
    def deposit(self):
        return self.__deposit

    @deposit.setter
    def deposit(self, value):
        if value is None:
            super()._add_validation_error(
                'deposit',
                '預かり金は必須です'
            )
        elif not isinstance(value, int):
            super()._add_validation_error(
                'deposit',
                '預かり金には整数をセットしてください'
            )
        else:
            self.__deposit = value

    def is_valid(self):
        if not super().is_valid():
            return False
        if self.total_price < self.discount_price:
            super()._add_validation_error(
                'discount_price',
                '合計金額以上の値引額が設定されています'
            )
            return False
        if self.deposit < self.total_price:
            super()._add_validation_error(
                'deposit',
                '預かり金が合計金額より少ないです'
            )
            return False
        if self.items is None or len(self.items) == 0:
            super()._add_validation_error(
                'items',
                '明細データがセットされていません'
            )
            return False
        return True
