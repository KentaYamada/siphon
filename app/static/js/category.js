'use strict';


class CategoryViewModel {
    constructor() {
        this.modalId = ko.observable('category_edit_modal');
        this.category = ko.observable(new Category(null, ''));
        this.categories = ko.observableArray();
        this.initCategories();

        // bind this
        this.onShowEditDialog = this.onShowEditDialog.bind(this);
    }

    // test data
    initCategories() {
        let data = [];
        for (let i = 1; i <= 10; i++) {
            data.push(new Category(i, `test${i}`));
        }
        this.categories(data);
    }

    onShowEditDialog() {
        $(`#${this.modalId()}`).modal();
    }
}

ko.applyBindings(new CategoryViewModel());
