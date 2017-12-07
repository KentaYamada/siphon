"use strict";


var Category = function(id, name, products) {
    var self = this;
    self.END_POINT = "/api/categories";
    self.id = ko.observable(id);
    self.name = ko.observable(name);
    self.products = ko.observableArray();

    self.add = function() {
        requestApi(self.END_POINT, "POST", ko.toJSON(self))
            .done(function(data) {
                console.log(data);
            })
            .fail(function() {
            });
    }

    self.edit = function() {
        var url = self.END_POINT + '/' + self.id();
        requestApi(url, "PUT", ko.toJSON(self))
            .done(function(data) {
                console.log(data);
            })
            .fail(function() {
            });
    }

    self.remove = function() {
        var url = self.END_POINT + '/' + self.id();
        requestApi(url, "DELETE")
            .done(function(data) {
                console.log(data);
            })
            .fail(function() {
                console.error("Failed api request.");
            });
    }

    self.findAll = function(list) {
        requestApi(self.END_POINT, 'GET').done(function(data) {
            $.each(data.categories, function(i, row) {
                list.push(new Category(row.id, row.name));
            });
        });
    }
}


var CategoryViewModel = function() {
    var self = this;
    self.category = ko.observable(new Category());
    self.categories = ko.observableArray([]);
    self.category().findAll(self.categories);

    self.onAdd = function() {
        self.category().add();
    }

    self.onEdit = function() {
        self.category().edit();
    }

    self.onRemove = function() {
        self.category().remove();
    }

    self.onShowAddForm = function() {
        self.category(new Category());
        jQuery('#entryForm').modal('show');
    }

    self.onShowEditForm = function(category) {
        self.category(category);
        jQuery('#entryForm').modal('show');
    }

    self.onShowRemoveAlert = function(category) {
        self.category(category);
        jQuery('#removeAlert').modal('show');
    }
}

ko.applyBindings(new CategoryViewModel());
