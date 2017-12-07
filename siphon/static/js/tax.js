"use strict";


var Tax = function(rate, tax_type) {
    var self = this;
    self.END_POINT = "/api/tax";
    self.rate = ko.observable(rate);
    self.tax_type = ko.observable(tax_type);

    self.edit = function() {
        requestApi(self.END_POINT, 'POST', ko.toJSON(self.tax())).done(function(data) {
            console.log(data);
        });
    }

    self.find = function(model) {
        requestApi(self.END_POINT, 'GET').done(function(data) {
            model(new Tax(data.tax.rate, data.tax.tax_type));
        });
    }

}


var TaxViewModel = function() {
    var self = this;
    self.tax = ko.observable();
    var model = new Tax();
    mode.find(self.tax);

    self.onSave = function() {
        self.tax().edit();
    }
}

ko.applyBindings(new TaxViewModel());
