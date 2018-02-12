"use strict";


class Category extends ModelBase {
    constructor(id, name) {
        super();
        this.endpoint = '/api/categories';
        this.id(id);
        this.name = ko.observable(name);
    }

    // Todo: static methodにする
    findAll(list) {
        super.find(null, (res) => {
            $.each(res.categories, (i, category) => {
                list.push(new Category(category.id, category.name));
            });
        });
    }
}


/*class CategoryViewModel extends ViewModelBase {
    constructor() {
        super();
        this.title = '商品カテゴリ設定';
        this.model(new Category());
    }

    onShowAddForm() {
        this.model(new Category());
        super.onShowAddForm();
    }
}*/

var CategoryViewModel = function() {
    var self = this;
    self.TITLE = '商品カテゴリ登録';
    self.model = ko.observable(new Category());
    self.categories = ko.observableArray([]);
    self.model().findAll(self.categories);

    self.onAdd = function() {
        self.model().add();
    }

    self.onEdit = function() {
        self.model().edit();
    }

    self.onRemove = function() {
        self.model().remove();
    }

    self.onShowAddForm = function() {
        self.model(new Category());
        jQuery('#entryForm').modal('show');
    }

    self.onShowEditForm = function(category) {
        self.model(category);
        jQuery('#entryForm').modal('show');
    }

    self.onShowRemoveAlert = function(category) {
        self.model(category);
        jQuery('#removeAlert').modal('show');
    }
}

ko.applyBindings(new CategoryViewModel());
