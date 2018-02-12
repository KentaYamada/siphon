"use strict";


var MonthlySales = function(sales_date, amount) {
    var self = this;
    self.END_POINT = "/api/sales/monthly";
    self.sales_date = ko.observable(sales_date);
    self.amount = ko.observable(amount);

    self.findBy = function(list, sales_month) {
        if(list === null || list === "undefiend") {
            console.error("Invalid argument: list");
        }

        var year = 2017
        var month = 10;
        var url = self.END_POINT + "/" + year + "/" + month;

        requestApi(url , "GET")
            .done(function(res) {
                $.each(res.data, function(i, week) {
                    var row = $.map(week, function(i, day) {
                        return new MonthlySales(day.sales_date, day.amount);
                    });
                    list.push(row);
                });
            })
            .fail(function() {
                console.error('Failed get monthly sales.');
            });
    }
}


var MonthlySalesViewModel = function() {
    var self = this;
    self.monthlySales = ko.observableArray([]);
    self.month = ko.observable(new Date());

    self.onGetMonthlySales = function() {
        self.monthlySales.removeAll();
        var model = new MonthlySales();
        model.findBy(self.monthlySales, self.month());
    }

    self.onGetMonthlySales();
}


ko.applyBindings(new MonthlySalesViewModel());
