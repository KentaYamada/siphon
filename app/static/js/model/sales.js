'use strict';


class Sales {
    constructor() {
        this.items = ko.observableArray([]);
        this.total_price = ko.computed(() => {
            let total = 0;
            ko.utils.arrayForEach(this.items(), (item) => {
                total += item.subtotal();
            });
            return total;
        }, this);
    }
    /**
     * increase item
     * @param {string} item_name
     */
    increaseItem(item_name) {
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
}

