"use strict";


var Tax = function(rate=1, tax_type='out') {
    var self = this;
    self.rate = ko.observable(rate);
    self.tax_type = ko.observable(tax_type);
}


var TaxViewModel = function() {
    var self = this;
    self.tax = ko.observable(new Tax());

    self.onFind = function() {
    }

    self.onSave = function() {
        console.log(ko.toJSON(self.tax()));
    }
}

ko.applyBindings(new TaxViewModel());
