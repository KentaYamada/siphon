'use strict';


class EditCategoryViewModel {
    constructor() {
        this.category = ko.observable();
        this.errors = ko.observable();

        // bind this
        this.onShow = this.onShow.bind(this);
        this.onSave = this.onSave.bind(this);
    }

    onShow(category) {
        this.category(category);
        $('#category-edit-modal').modal('show');
    }

    onSave() {
        this.category().save()
            .done(function(res) {
                console.log(res)
            })
            .fail(function(xhr) {
                console.log(xhr);
            });
    }
}


class RemoveCategoryViewModel {
    constructor() {
        this.category = ko.observable();
        this.confirmMessage = ko.computed(function() {
            var message = '';
            if (this.category() !== undefined) {
                message = '「' + this.category().name() + '」を削除しますか？';
            }
            return message;
        }, this);
    }

    onShow(category) {
        this.category(category);
        $('#category-remove-modal').modal('show');
    }

    onRemove() {
        this.category().remove()
            .done(function(res) {
                console.log(res)
            });
    }
}


class CategoryViewModel {
    constructor() {
        this.category = ko.observable(new Category(null, ''));
        this.categories = ko.observableArray();
        this.editModal = new EditCategoryViewModel();
        this.removeModal = new RemoveCategoryViewModel();

        // bind this
        this.onShowAddDialog = this.onShowAddDialog.bind(this);
        this.onShowEditDialog = this.onShowEditDialog.bind(this);
        this.onBeforeRemoveDialog = this.onBeforeRemoveDialog.bind(this);

        this._fetchCategories();
    }

    onShowAddDialog() {
        this.editModal.onShow(new Category(null, ''));
    }

    onShowEditDialog(category) {
        this.editModal.onShow(category);
    }

    onBeforeRemoveDialog(category) {
        this.removeModal.onShow(category);
    }

    _fetchCategories() {
        var self = this;
        Category.findAll()
            .done(function(res) {
                console.log(res);
                if (res.categories) {
                    var rows = [];

                    ko.utils.arrayForEach(res.categories, function(category) {
                        rows.push(new Category(category.id, category.name));
                    });

                    self.categories.removeAll();
                    self.categories(rows);
                }
            })
            .fail(function() {
            });
    }
}

$(function() {
    var mainViewModel = new CategoryViewModel();

    ko.applyBindings(
        mainViewModel,
        document.getElementById('category-list')
    );
    ko.applyBindings(
        mainViewModel.editModal,
        document.getElementById('category-edit-modal')
    );
    ko.applyBindings(
        mainViewModel.removeModal,
        document.getElementById('category-remove-modal')
    );
});
