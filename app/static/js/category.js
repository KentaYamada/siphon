'use strict';


class CategoryViewModel {
    constructor() {
        this.category = ko.observable();
        this.categories = ko.observableArray();

        this.noitem = ko.computed(function() {
            return this.categories().length < 1;
        }, this);

        // bind this
        this.onClickAdd = this.onClickAdd.bind(this);
        this.onClickEdit = this.onClickEdit.bind(this);
        this.onClickDelete = this.onClickDelete.bind(this);
        this.onModalClickSave = this.onModalClickSave.bind(this);
        this.onModalClickDelete = this.onModalClickDelete.bind(this);

        this._fetchCategories();
    }

    onClickAdd() {
        this.category(new Category(null, ''));
        $('#category_edit_modal').modal();
    }

    onClickEdit(category) {
        this.category(category);
        $('#category_edit_modal').modal();
    }

    onClickDelete(category) {
        this.category(category);
        $('#category_delete_modal').modal();
    }

    onModalClickSave() {
        console.log(ko.toJSON(this.category()));
        // this.category().save()
        //     .done(function(data) {
        //     })
        //     .fail(function() {
        //     });
    }

    onModalClickDelete() {
        console.log(ko.toJSON(this.category()));
        // this.category().delete()
        //     .done(function(data) {
        //     })
        //     .fail(function() {
        //     });
    }

    _fetchCategories() {
        var self = this;
        Category.findAll()
                .done(function(data) {
                    self._fetchCategoriesSuccess(data);
                });
    }

    _fetchCategoriesSuccess(data) {
        var rows = [];
        ko.utils.arrayForEach(data.categories, function(category) {
            rows.push(new Category(category.id, category.name));
        });
        this.categories(rows);
    }
}

$(function() {
    ko.applyBindings(new CategoryViewModel());
});
