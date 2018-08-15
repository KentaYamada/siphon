'use strict';


class CashierViewModel {
    constructor() {
        this.sales = new Sales();
        this.categories = ko.observableArray([]);
        this.items = ko.observableArray([]);
        this.discount_label = ko.observable('値引額');

        // computed attributes
        this.can_cashing = ko.computed(function() {
            return this.sales.change() > 0;
        }, this);

        // bind this
        this.onAddItem = this.onAddItem.bind(this);
        this.onAddThousand = this.onAddThousand.bind(this);
        this.onAddTenThousand = this.onAddTenThousand.bind(this);
        this.onChangeItems = this.onChangeItems.bind(this);
        this.onDecreaseItem = this.onDecreaseItem.bind(this);
        this.onReset = this.onReset.bind(this);
        this.onResetDeposit = this.onResetDeposit.bind(this);
        this.onSave = this.onSave.bind(this);
        this.onSwitchDiscountPrice = this.onSwitchDiscountPrice.bind(this);
        this.onSwitchDiscountRate = this.onSwitchDiscountRate.bind(this);

        // fetch panel data
        this._fetchItems();
    }

    /**
     * change items panel event
     * @param {Category} selected category
     */
    onChangeItems(category) {
        this.items.removeAll();
        this.items(category.items);
    }

    /**
     * add sales item event
     * @param {Item} selected item
     */
    onAddItem(item) {
        this.sales.increaseItem(item);
    }

    /**
     * decrease or remove item event
     * @param {SalesItem} selected sales item
     */
    onDecreaseItem(sales_item) {
        this.sales.decreaseItem(sales_item);
    }

    /**
     * switch discount price mode event
     */
    onSwitchDiscountPrice() {
        this.sales.discount_rate(0);
        this.sales.discount_price(0);
        this.discount_label('値引額');
    }

    /**
     * switch discount rate mode event
     */
    onSwitchDiscountRate() {
        this.sales.discount_rate(0);
        this.sales.discount_price(0);
        this.discount_label('値引率');
    }

    /**
     * +1000 button click event
     */
    onAddThousand() {
        var deposit = Number(this.sales.deposit()) + 1000;
        this.sales.deposit(deposit);
    }

    /**
     * +10000 button click event
     */
    onAddTenThousand() {
        var deposit = Number(this.sales.deposit()) + 10000;
        this.sales.deposit(deposit);
    }

    /**
     * AC button click event
     */
    onReset() {
        this.sales.reset();
    }

    /**
     * reset deposit button click event
     */
    onResetDeposit() {
        this.sales.deposit(0);
    }

    /**
     * save button click event
     */
    onSave() {
        this.sales.save();
    }

    /**
     * Fetch item selection data
     */
    _fetchItems() {
        var self = this;
        requestApi('/api/cashier', 'GET')
            .done(function(data) {
                // console.log(data);
                if (data.categories && data.categories.length > 0) {
                    self.categories(data.categories);
                    self.items(data.categories[0][0].items);
                    console.log(self.items());
                }
            });
    }
}


$(function() {
    ko.applyBindings(new CashierViewModel());
});
