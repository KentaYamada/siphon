"use strict";


var Tax = function(rate=1, tax_type='out') {
    var self = this;
    self.rate = ko.observable(rate);
    self.tax_type = ko.observable(tax_type);
}


var TaxViewModel = function() {
    var self = this;
    self.tax = ko.observable();
    requestApi('/api/tax', 'GET').done(function(data) {
        self.tax(new Tax(data.tax.rate, data.tax.tax_type));
    });

    self.onSave = function() {
        requestApi('/api/tax', 'POST', ko.toJSON(self.tax())).done(function(data) {
            console.log('succeed.');
        });
    }
}

ko.applyBindings(new TaxViewModel());
