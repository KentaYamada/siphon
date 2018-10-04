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
        var self = this;

        this.errors(null);
        this.category().save()
            .done(function(res) {
                $('#category-edit-modal').modal('hide');
                $('#category-list').trigger('onRequestSuccess', [res.message]);
            })
            .fail(function(xhr) {
                if (xhr.status === 400) {
                    self.errors(xhr.responseJSON.errors);
                }
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
                $('#category-list').trigger('onRequestSuccess', ['削除しました']);
                $('#category-remove-modal').modal('hide');
            });
    }
}


class CategoryViewModel {
    constructor() {
        this.category = ko.observable(new Category(null, ''));
        this.categories = ko.observableArray();
        this.flashMessage = new FlashMessageViewModel();
        this.editModal = new EditCategoryViewModel();
        this.removeModal = new RemoveCategoryViewModel();

        // bind this
        this.onShowAddDialog = this.onShowAddDialog.bind(this);
        this.onShowEditDialog = this.onShowEditDialog.bind(this);
        this.onBeforeRemoveDialog = this.onBeforeRemoveDialog.bind(this);
        this.onRequestSuccess = this.onRequestSuccess.bind(this);
        this.onRequestFailure = this.onRequestFailure.bind(this);

        // listen to events
        $('#category-list').on('onRequestSuccess', this.onRequestSuccess);
        $('#category-list').on('onRequestFailure', this.onRequestFailure);

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

    onRequestSuccess(e, message) {
        this.flashMessage.onShowSuccessMessage(message);
        this._fetchCategories();
    }

    onRequestFailure(e, message) {
        this.flashMessage.onShowFailMessage(message);
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
        mainViewModel.flashMessage,
        document.getElementById('flash-message-area')
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
