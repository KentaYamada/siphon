'use strict';


class SalesItem {
    constructor(item_name, unit_price, quantity) {
        this.item_name = ko.observable(item_name);
        this.unit_price = ko.observable(unit_price);
        this.quantity = ko.observable(quantity);
        this.subtotal = ko.computed(() => {
            return this.unit_price() * this.quantity();
        }, this);
    }
}

