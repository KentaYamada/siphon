"use strict";



var DailySales = function(day, amount) {
    var self = this;
    self.day = ko.observable(day);
    self.amount = ko.observable(amount);

    self.find = function(month) {
    }
}


var MonthlySalesViewModel = function() {
    var self = this;
    self.calendar = ko.observableArray(days);
    self.month = ko.observable('2017-10');

    self.onFind = function() {
        // Todo: request api
        console.log(self.month());
    }
}

var days = [
    [
        new DailySales(1, 1000),
        new DailySales(2, 2000),
        new DailySales(3, 3000),
        new DailySales(4, 4000),
        new DailySales(5, 5000),
        new DailySales(6, 6000),
        new DailySales(7, 7000),
    ],
    [
        new DailySales(8, 1000),
        new DailySales(9, 2000),
        new DailySales(10, 3000),
        new DailySales(11, 4000),
        new DailySales(12, 5000),
        new DailySales(13, 6000),
        new DailySales(14, 7000),
    ],
    [
        new DailySales(15, 1000),
        new DailySales(16, 2000),
        new DailySales(17, 3000),
        new DailySales(18, 4000),
        new DailySales(19, 5000),
        new DailySales(20, 6000),
        new DailySales(21, 7000),
    ],
    [
        new DailySales(22, 1000),
        new DailySales(23, 2000),
        new DailySales(24, 3000),
        new DailySales(25, 4000),
        new DailySales(26, 5000),
        new DailySales(27, 6000),
        new DailySales(28, 7000),
    ],
    [
        new DailySales(29, 1000),
        new DailySales(30, 2000),
        new DailySales(31, 3000),
        new DailySales(0, 0),
        new DailySales(0, 0),
        new DailySales(0, 0),
        new DailySales(0, 0),
    ]

];

ko.applyBindings(new MonthlySalesViewModel());
