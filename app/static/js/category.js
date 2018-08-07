'use strict';


class CategoryViewModel {
    constructor() {
        this.modalId = ko.observable('category_edit_modal');
        this.category = ko.observable({
            id: null, name: ''
        });
        this.categories = ko.observableArray([
            { id: 1, name: 'Morning' },
            { id: 2, name: 'Lunch' },
            { id: 3, name: 'Dinner' }
        ]);

        // bind this
        this.onShowEditDialog = this.onShowEditDialog.bind(this);
    }

    onShowEditDialog() {
        $(`#${this.modalId()}`).modal();
    }
}

ko.applyBindings(new CategoryViewModel());
