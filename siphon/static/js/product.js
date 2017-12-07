"use strict";


var Product = function(id, category_id, name, price) {
    var self = this;
    self.END_POINT = "/api/products";
    self.id = ko.observable(id);
    self.category_id = ko.observable(category_id);
    self.name = ko.observable(name);
    self.price = ko.observable(price);

    self.add = function() {
        requestApi(self.END_POINT, 'POST', ko.toJSON(self)).done(function(data) {
        });
    }

    self.edit = function() {
        var url = self.END_POINT + "/"  + self.id();
        requestApi(url, 'PUT', ko.toJSON(self)).done(function(data) {
        });
    }

    self.remove = function() {
        var url = self.END_POINT + "/"  + self.id();
        requestApi(url, 'DELETE', ko.toJSON(self)).done(function(data) {
        });
    }

    self.findBy = function(list, categoryId) {
        var url = self.END_POINT + "/" + categoryId;
        requestApi(self.END_POINT, 'GET').done(function(data) {
            $.each(data.products, function(i, row) {
                list.push(new Product(row.id, row.category_id,
                                      row.name, row.price));
            });
        });
    }
}


var ProductViewModel = function() {
    var self = this;
    self.product = ko.observable(new Product());
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


    self.onAdd = function() {
        self.product().add();
    }

    self.onChangeCategory = function() {
        // ToDo: implement get category.
        requestApi("/api/products/", ko.toJSON(self.selectedCatgory()))
        .done(function(data) {
            self.categories(data.categories);
        });
        console.log(ko.toJSON(self.selectedCatgory()));
    }

    self.onEdit = function() {
        self.product().edit();
    }

    self.onRemove = function() {
        self.product().remove();
    }

    self.onShowAddForm = function() {
        self.product(new Product());
        jQuery('#entryForm').modal('show');
    }

    self.onShowEditForm = function(product) {
        self.product(product);
        jQuery('#entryForm').modal('show');
    }

    self.onShowRemoveAlert = function(product) {
        self.product(product);
        jQuery('#removeAlert').modal('show');
    }
}

ko.applyBindings(new ProductViewModel());
