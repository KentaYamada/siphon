'use strict';


class Sales {
    constructor() {
        this.items = ko.observableArray([]);
        this.discount_price = ko.observable(0);
        this.discount_rate = ko.observable(0);
        this.deposit = ko.observable(0);

        // computed attributes
        this.total_price = ko.computed(function() {
            var total = 0;
            ko.utils.arrayForEach(this.items(), function(item) {
                total += item.subtotal();
            });

            if (this.discount_price() > 0) {
                total -= this.discount_price();
            }

            if (this.discount_rate() > 0) {
            }

            return total;
        }, this);

        this.change = ko.computed(function() {
            var change = this.deposit() - this.total_price();
            return change < 0 ? 0 : change;
        }, this);
    }

    /**
     * increase item
     * @param {Item} selected item
     */
    increaseItem(selected_item) {
        var item = ko.utils.arrayFirst(this.items(), function(item) {
            return selected_item.name === item.item_name();
        });

        if (item === null) {
            this.items.push(new SalesItem(
                selected_item.name,
                selected_item.unit_price,
                1
            ));
        } else {
            item.quantity(item.quantity() + 1);
        }
    }

    /**
     * decrease or remova item
     * @param {SalesItem} selected item
     */
    decreaseItem(item) {
        if ((item.quantity() - 1) < 1) {
            this.items.remove(item);
        } else {
            item.quantity(item.quantity() -1);
        }
    }

    /**
     * reset all values
     */
    reset() {
        this.items.removeAll();
        this.deposit(0);
        this.discount_price(0);
        this.discount_rate(0);
    }

    /**
     * save data
     */
    save() {
        console.log(ko.toJSON(this));
    }
}

