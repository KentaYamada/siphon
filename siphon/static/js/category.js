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
}


var CategoryViewModel = function() {
    var self = this;
    self.category = ko.observable(new Category());
    self.mode = ko.observable('add');
    self.isAdd = ko.computed(function() {
        return self.mode() == 'add' ? true : false;
    }, self);

    self.categories = ko.observableArray([]);
    requestApi('/api/categories', 'GET').done(function(data) {
        $.map(data.categories, function(row, i) {
            self.categories.push(new Category(row.id, row.name));
        });
        //self.categories(data.categories);
    });

    self.onAdd = function() {
        self.category().add();
    }

    self.onEdit = function() {
        self.category().edit();
        //requestApi('/api/categories', 'PUT', ko.toJSON(self.category))
        //.done(function(data) {
        //    console.log(data);
        //});
    }

    self.onRemove = function(category) {
        self.category(category);
        console.log(self.category());
        jQuery('#removeAlert').modal('show');
    }

    self.onShowAddForm = function() {
        self.category(new Category());
        self.mode('add');
        jQuery('#entryForm').modal('show');
    }

    self.onShowEditForm = function(category) {
        self.category(category);
        self.mode('edit');
        jQuery('#entryForm').modal('show');
    }

    self.onShowRemoveAlert = function(category) {
        self.category(category);
        console.log(self.category());
        jQuery('#removeAlert').modal('show');
    }
}

ko.applyBindings(new CategoryViewModel());
