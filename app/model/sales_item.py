from app.model.base import BaseModel


class SalesItem(BaseModel):
    def __init__(self, id=None, sales_id=None,
                 item_no=None, item_name=None, unit_price=None,
                 quantity=None, subtotal=None, **kwargs):
        super().__init__()
        self.id = id
        self.sales_id = sales_id
        self.item_no = item_no
        self.item_name = item_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.subtotal = subtotal

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
    def sales_id(self):
        return self.__sales_id

    @sales_id.setter
    def sales_id(self, value):
        super()._clear_validation_error('sales_id')
        if value is None:
            super()._add_validation_error('sales_id', '売上IDは必須です')
        elif not isinstance(value, int):
            super()._add_validation_error('sales_id', '売上IDには整数をセットしてください')
        elif value <= 0:
            super()._add_validation_error('sales_id', '無効な売上IDです')
        else:
            self.__sales_id = value

    @property
    def item_no(self):
        return self.__item_no

    @item_no.setter
    def item_no(self, value):
        super()._clear_validation_error('item_no')
        if value is None:
            super()._add_validation_error('item_no', '明細Noは必須です')
        elif not isinstance(value, int):
            super()._add_validation_error('item_no', '明細Noには整数をセットしてください')
        elif value <= 0:
            super()._add_validation_error('item_no', '無効な明細Noです')
        else:
            self.__item_no = value

    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, value):
        super()._clear_validation_error('item_name')
        if not value:
            super()._add_validation_error('item_name', '商品名は必須です')
        else:
            self.__item_name = value

    @property
    def unit_price(self):
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, value):
        super()._clear_validation_error('unit_price')
        if value is None:
            super()._add_validation_error('unit_price', '単価は必須です')
        elif not isinstance(value, int):
            super()._add_validation_error('unit_price', '単価には整数をセットしてください')
        elif value <= 0:
            super()._add_validation_error('unit_price', '無効な単価です')
        else:
            self.__unit_price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        super()._clear_validation_error('quantity')
        if value is None:
            super()._add_validation_error('quantity', '数量は必須です')
        elif not isinstance(value, int):
            super()._add_validation_error('quantity', '数量には整数をセットしてください')
        elif value <= 0:
            super()._add_validation_error('quantity', '無効な数量です')
        else:
            self.__quantity = value

    @property
    def subtotal(self):
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, value):
        super()._clear_validation_error('subtotal')
        if value is None:
            super()._add_validation_error('subtotal', '小計は必須です')
        elif not isinstance(value, int):
            super()._add_validation_error('subtotal', '小計には整数をセットしてください')
        elif value <= 0:
            super()._add_validation_error('subtotal', '無効な小計です')
        else:
            self.__subtotal = value

    def is_valid(self):
        if not super().is_valid():
            return False
        if (self.unit_price * self.quantity) != self.subtotal:
            super()._add_validation_error('subtotal', '小計の計算値がマッチしません')
            return False
        return True


class PopularSalesItemSearchOption:
    def __init__(self, start_date, end_date, **kwargs):
        self.start_date = start_date
        self.end_date = end_date
