'use strict';


class ItemViewModel {
    constructor() {
        this.modalId = ko.observable('item_edit_modal');
        this.item = ko.observable();
        this.items = ko.observableArray([
            { id: 1, name: 'Gamoyon curry', unit_price: 600 },
            { id: 2, name: 'Siphon coffee', unit_price: 450 }
        ]);
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

ko.applyBindings(new ItemViewModel());
