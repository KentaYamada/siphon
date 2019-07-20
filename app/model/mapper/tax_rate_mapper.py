from datetime import datetime
from app.model.tax_rate import TaxRate
from app.model.mapper.base_mapper import BaseMapper


class TaxRateMapper(BaseMapper):
    def save(self, tax_rate):
        if tax_rate is None or not isinstance(tax_rate, TaxRate):
            raise ValueError()
        data = (
            tax_rate.rate,
            tax_rate.reduced_rate,
            tax_rate.start_date,
            tax_rate.tax_type
        )
        try:
            self._db.execute_proc('save_tax_rate', data)
            self._db.commit()
            saved = True
        except Exception as e:
            # todo: logging
            self._db.rollback()
            saved = False
        return saved

    def find_current_tax_rate(self):
        data = (datetime.now().date(),)
        try:
            row = self._db.find_one_proc('find_current_tax_rate', data)
            self._db.commit()
        except Exception as e:
            # todo: logger
            self._db.rollback()
            row = None
        fields = ['rate', 'reduced_rate', 'start_date', 'tax_type']
        if row is not None:
            row['start_date'] = row['start_date'].strftime('%Y/%m/%d')
            row = self.format_row(row, fields)
        return row
