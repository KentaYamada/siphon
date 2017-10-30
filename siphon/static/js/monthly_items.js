"use strict";


var MonthlyItemsViewModel = function() {
    var self = this;
    self.month = ko.observable('2017-10');
    self.items = ko.observableArray([
        {item: 'Siphon Coffee', quantity: 250},
        {item: 'Gamoyon Curry', quantity: 300},
    ]);

    self.onFind = function() {
        // Todo: request api
        console.log(self.month());
    }
}

ko.applyBindings(new MonthlyItemsViewModel());
