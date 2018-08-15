'use strict';


class MonthlySalesViewModel {
    constructor() {
        this.monthly_sales = ko.observableArray([]);
        this.sales_month = ko.observable(moment().format('YYYY-MM'));
        this.noitem = ko.computed(function() {
            return this.monthly_sales().length < 1;
        }, this);

        // bind this
        this.onSearchMonthSales = this.onSearchMonthSales.bind(this);

        this._fetchMonthlySales();
    }

    /**
     * Search button click event
     */
    onSearchMonthSales() {
        this._fetchMonthlySales();
    }

    /**
     * Fetch monthly sales from server
     */
    _fetchMonthlySales() {
        var splitSalesMonth = this.sales_month().split('-');
        var year = splitSalesMonth[0];
        var month = splitSalesMonth[1];
        var url = `/api/sales/monthly/${year}/${month}`;
        var self = this;

        requestApi(url, 'GET')
            .done(function(data, textStatus) {
                if (data.monthly_sales) {
                    self.monthly_sales.removeAll();
                    self.monthly_sales(data.monthly_sales);
                }
            });
    }
}


$(function() {
    ko.applyBindings(new MonthlySalesViewModel());
});
