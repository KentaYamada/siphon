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

        var year = sales_month.split("/")[0];
        var month = sales_month.split("/")[1];
        var url = self.END_POINT + "/" + year + "/" + month;

        requestApi(url , "GET")
            .done(function(res) {
                $.each(res.data, function(i, row) {
                    list.push(new MonthlySales(row.sales_date, row.amount);
                });
            })
            .fail(function() {
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


var days = [
    [
        new MonthlySales(1, 1000),
        new MonthlySales(2, 2000),
        new MonthlySales(3, 3000),
        new MonthlySales(4, 4000),
        new MonthlySales(5, 5000),
        new MonthlySales(6, 6000),
        new MonthlySales(7, 7000),
    ],
    [
        new MonthlySales(8, 1000),
        new MonthlySales(9, 2000),
        new MonthlySales(10, 3000),
        new MonthlySales(11, 4000),
        new MonthlySales(12, 5000),
        new MonthlySales(13, 6000),
        new MonthlySales(14, 7000),
    ],
    [
        new MonthlySales(15, 1000),
        new MonthlySales(16, 2000),
        new MonthlySales(17, 3000),
        new MonthlySales(18, 4000),
        new MonthlySales(19, 5000),
        new MonthlySales(20, 6000),
        new MonthlySales(21, 7000),
    ],
    [
        new MonthlySales(22, 1000),
        new MonthlySales(23, 2000),
        new MonthlySales(24, 3000),
        new MonthlySales(25, 4000),
        new MonthlySales(26, 5000),
        new MonthlySales(27, 6000),
        new MonthlySales(28, 7000),
    ],
    [
        new MonthlySales(29, 1000),
        new MonthlySales(30, 2000),
        new MonthlySales(31, 3000),
        new MonthlySales(0, 0),
        new MonthlySales(0, 0),
        new MonthlySales(0, 0),
        new MonthlySales(0, 0),
    ]

];

ko.applyBindings(new MonthlySalesViewModel());
