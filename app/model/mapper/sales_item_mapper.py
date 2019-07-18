from app.model.mapper.base_mapper import BaseMapper
from app.model.sales_item import PopularSalesItemSearchOption


class SalesItemMapper(BaseMapper):
    def __init__(self):
        super().__init__()

    def find_daily_sales_items(self, sales_ids):
        if sales_ids is None:
            raise ValueError('sales_ids cannot empty.')
        if not isinstance(sales_ids, list):
            raise ValueError('invalid type: sales_ids')
        data = (sales_ids,)
        rows = []
        try:
            rows = self._db.find_proc('find_daily_sales_items', data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
        fields = [
            'sales_id',
            'item_no',
            'item_name',
            'unit_price',
            'quantity',
            'subtotal'
        ]
        sales_items = self.format_rows(rows, fields)
        return sales_items

    def find_popular_items(self, option):
        if option is None or not isinstance(option, PopularSalesItemSearchOption):
            raise ValueError('Invalid argument')
        data = (
            option.start_date,
            option.end_date
        )
        rows = []
        try:
            rows = self._db.find_proc('find_popular_sales_items', data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
        fields = ['rank_no', 'item_name', 'quantity']
        sales_items = self.format_rows(rows, fields)
        return list(filter(lambda x: x['quantity'] > 0, sales_items))
