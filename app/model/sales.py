# from app.model.sale_item import SalesItem


class Sales():
    def __init__(self, id=None, sales_date=None,
                 total_price=None, discount_price=None, discount_rate=None,
                 inclusive_tax=None, exclusive_tax=None, deposit=None,
                 items=None):
        self.__id = id
        self.__sales_date = sales_date
        self.__total_price = total_price
        self.__discount_price = discount_price
        self.__discount_rate = discount_rate
        self.__inclusive_tax = inclusive_tax
        self.__exclusive_tax = exclusive_tax
        self.__deposit = deposit
        self.__items = items
        self.__errors = []

    @property
    def errors(self):
        return self.__errors

    def validate(self):
        # todo: decorator化
        isValid = True
        if self.__sales_date is None:
            isValid = False
            self.__set_error('sales_date', '売上日は必須です')
        if self.__total_price is None:
            isValid = False
            self.__set_error('total_price', '合計金額は必須です')
        elif self.__total_price <= 0:
            isValid = False
            self.__set_error('total_price', '1円未満の合計金額は登録できません')
        if self.__total_price < self.__discount_price:
            isValid = False
            self.__set_error('discount_price', '合計金額以上の値引額が設定されています')
        if self.__discount_rate >= 100:
            isValid = False
            self.__set_error('discount_rate', '不正な値引率の値です')
        if self.__deposit is None:
            isValid = False
            self.__set_error('deposit', '預かり金は必須です')
        elif self.__total_price > self.__deposit:
            isValid = False
            self.__set_error('deposit', '預かり金が合計金額より少ないです')
        if self.__items is None or len(self.__items) < 1:
            isValid = False
            self.__set_error('items', '明細データがセットされていません')
        return isValid

    def save(self):
        if not self.validate():
            return False
        return True

    def __set_error(self, field, message):
        self.__errors.append({'name': field, 'message': message})
