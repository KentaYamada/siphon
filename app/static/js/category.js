'use strict';


class CategpryEditViewModel {
    constructor(category) {
        this.category = category;
    }

    /**
     * save button click event
     */
    onSave() {
        this.category.save()
            .done(function(data) {
            })
            .fail(function() {
            });
    }
}

class CategoryViewModel {
    constructor() {
        this.modalId = ko.observable('category_edit_modal');
        this.category = ko.observable(new Category(null, ''));
        this.categories = ko.observableArray();

        this.noitem = ko.computed(function() {
            return this.categories().length < 1;
        }, this);

        // bind this
        this.onShowEditDialog = this.onShowEditDialog.bind(this);

        this._fetchCategories();
    }

    onShowEditDialog() {
        $(`#${this.modalId()}`).modal();
    }

    _fetchCategories() {
        var self = this;
        Category.findAll()
            .done(function(data) {
                self.categories(data.categories);
            });
    }
}

$(function() {
    ko.applyBindings(new CategoryViewModel());
});
