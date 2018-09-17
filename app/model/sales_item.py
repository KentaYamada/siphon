class SalesItem():
    def __init__(self, id=None, sales_id=None,
                 sales_date=None, item_no=None, item_name='',
                 unit_price=None, quantity=None, subtotal=None):
        self.id = id
        self.sales_id = sales_id
        self.sales_date = sales_date
        self.item_no = item_no
        self.item_name = item_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.subtotal = subtotal
        self.__errors = []

    @property
    def errors(self):
        return self.__errors

    def validate(self):
        # ToDo: decorator化
        isValid = True
        if self.sales_id is None:
            isValid = False
            self.__set_error('sales_id', '売上IDは必須です')
        if self.sales_date is None:
            isValid = False
            self.__set_error('sales_date', '売上日は必須です')
        if self.item_no is None:
            isValid = False
            self.__set_error('item_no', '売上明細番号は必須です')
        if not self.item_name:
            isValid = False
            self.__set_error('item_name', '商品名は必須です')
        if self.unit_price is None:
            isValid = False
            self.__set_error('unit_price', '単価は必須です')
        elif self.unit_price <= 0:
            isValid = False
            self.__set_error('unit_price', '1円未満の単価は登録できません')
        if self.quantity is None:
            isValid = False
            self.__set_error('quantity', '数量は必須です')
        elif self.quantity <= 0:
            isValid = False
            self.__set_error('quantity', '1未満の数量は登録できません')
        if self.subtotal is None:
            isValid = False
            self.__set_error('subtotal', '小計は必須です')
        elif self.subtotal <= 0:
            isValid = False
            self.__set_error('subtotal', '1円未満の小計は登録できません')
        return isValid

    def save(self):
        if not self.validate():
            return False
        return True

    def delete(self):
        if self.id is None:
            return False
        return True

    @classmethod
    def find_monthly_sales_items_by(cls, sales_month):
        rows = []
        for i in range(1, 11):
            rows.append({
                'id': i,
                'sales_id': 1,
                'sales_date': 'YYYY-mm-dd hh:MM:ss',
                'item_no': i,
                'item_name': 'Item{0}'.format(i),
                'unit_price': i * 100,
                'quantity': 1,
                'subtotal': i * 100})
        return rows

    def __set_error(self, field, message):
        self.__errors.append({'name': field, 'message': message})
