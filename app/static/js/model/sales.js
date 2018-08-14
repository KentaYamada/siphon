'use strict';


class Sales {
    constructor() {
        this.items = ko.observableArray([]);
        this.discount_price = ko.observable(0);
        this.discount_rate = ko.observable(0);
        this.deposit = ko.observable(0);

        // computed attributes
        this.total_price = ko.computed(() => {
            let total = 0;
            ko.utils.arrayForEach(this.items(), (item) => {
                total += item.subtotal();
            });

            if (this.discount_price() > 0) {
                total -= this.discount_price();
            }

            if (this.discount_rate() > 0) {
            }

            return total;
        }, this);

        this.change = ko.computed(() => {
            return this.total_price() - this.deposit();
        }, this);
    }

    /**
     * increase item
     * @param {Item} selected item
     */
    increaseItem(item) {
        const item = ko.utils.arrayFirst(this.items(), (item) => {
            return item.item_name === item_name;
        });

        if (item === null) {
            this.items.push(new SalesItem(
            ));
        } else {
            this.items.quantity(this.quantity() + 1);
        }
    }

    /**
     * decrease or remova item
     * @param {SalesItem} selected item
     */
    decreaseItem(item) {
        if (--this.items().length < 1) {
            this.items.remove(item);
        } else {
            item.quantity(quantity() -1);
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
        console.log(ko.toJSON(this);
    }
}

