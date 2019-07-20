from app.model.base import BaseModel


class TaxRate(BaseModel):
    def __init__(self, rate, reduced_rate, start_date, tax_type, **kwargs):
        super().__init__()
        self.rate = rate
        self.reduced_rate = reduced_rate
        self.start_date = start_date
        self.tax_type = tax_type

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        super()._clear_validation_error('rate')
        if value is None:
            super()._add_validation_error('rate', '税率必須入力です')
        elif not isinstance(value, int):
            super()._add_validation_error('rate', '税率は整数をセットしてください')
        elif value < 1:
            super()._add_validation_error('rate', '1%以上の税率をセットしてください')
        else:
            self.__rate = value

    @property
    def reduced_rate(self):
        return self.__reduced_rate

    @reduced_rate.setter
    def reduced_rate(self, value):
        super()._clear_validation_error('reduced_rate')
        if value is None:
            super()._add_validation_error('reduced_rate', '軽減税率必須入力です')
        elif not isinstance(value, int):
            super()._add_validation_error('reduced_rate', '軽減税率は整数をセットしてください')
        elif value < 1:
            super()._add_validation_error('reduced_rate', '軽減税率は1%以上セットしてください')
        else:
            self.__rreduced_ate = value

    @property
    def tax_type(self):
        return self.__tax_type

    @tax_type.setter
    def tax_type(self, value):
        super()._clear_validation_error('tax_type')
        if value is None:
            super()._add_validation_error('tax_type', '税タイプ必須入力です')
        elif not isinstance(value, int):
            super()._add_validation_error('tax_type', '税タイプは整数をセットしてください')
        elif value not in (1, 2):
            super()._add_validation_error('tax_type', '無効な税タイプです')
        else:
            self.__tax_type = value

