"use strict";


var Product = function(id, category_id, price) {
    var self = this;
    self.id = ko.observable(id);
    self.category_id = ko.observable(category_id);
    self.name = ko.observable(name);
    self.price = ko.observable(price);
}


var ProductViewModel = function() {
    var self = this;
    self.product = ko.observable();
    self.products = ko.observableArray([
        {"id": 1, "category_id": 1, "name": "A", "price": 100},
        {"id": 2, "category_id": 2, "name": "B", "price": 200},
    ]);
    self.categories = ko.observableArray([
        {"id": 1, "name": "Morning"},
        {"id": 2, "name": "Lunch"},
        {"id": 3, "name": "Dinner"}
    ]);
    self.selectedCatgory = ko.observable();
    self.mode = ko.observable('add');

    // ToDo: mode分割したほうがいい？
    self.isAdd = ko.computed(function() {
        return self.mode() == 'add' ? true : false;
    }, self);

    self.onAdd = function() {
        console.log(ko.toJSON(self.product()));
    }

    self.onChangeCategory = function() {
        // ToDo: implement get category.
        console.log(ko.toJSON(self.selectedCatgory()));
    }

    self.onEdit = function() {
        console.log(ko.toJSON(self.product()));
    }

    self.onRemove = function() {
    }

    self.onShowAddForm = function() {
        self.product(new Product());
        self.mode('add');
        jQuery('#entryForm').modal('show');
    }

    self.onShowEditForm = function(product) {
        self.product(product);
        self.mode('edit');
        jQuery('#entryForm').modal('show');
    }

    self.onShowRemoveAlert = function(product) {
        self.product(product);
        jQuery('#removeAlert').modal('show');
    }
}

ko.applyBindings(new ProductViewModel());
