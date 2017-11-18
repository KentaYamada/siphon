"use strict";


var Category = function(id=null, name='', products=[]) {
    var self = this;
    self.id = ko.observable(id);
    self.name = ko.observable(name);
    self.products = ko.observableArray();
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
        self.categories(data.categories);
    });

    self.onAdd = function() {
        requestApi('/api/categories', 'POST', ko.toJSON(self.category))
        .done(function(data) {
            console.log(data);
        });
    }

    self.onEdit = function() {
        requestApi('/api/categories', 'PUT', ko.toJSON(self.category))
        .done(function(data) {
            console.log(data);
        });
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
