'use strict';


class CashierViewModel {
    constructor() {
        this.sales = new Sales();
        this.items = ko.observableArray([]);
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
    onDecraeseItem(sales_item) {
        this.salse.decreaseItem(sales_item);
    }

    /**
     * switch discount price mode event
     */
    onSwitchDiscountPrice() {
        this.sales.discount_rate(0);
        this.sales.discount_price(0);
    }

    /**
     * switch discount rate mode event
     */
    onSwitchDiscountRate() {
        this.sales.discount_rate(0);
        this.sales.discount_price(0);
    }

    /**
     * +1000 button click event
     */
    onAddThousand() {
        this.sales.deposit(this.sales.deposit() + 1000);
    }

    /**
     * +10000 button click event
     */
    onAddTenThousand() {
        this.sales.deposit(this.sales.deposit() + 10000);
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
     *
     */
    _initItemSelectionPanel() {
    }
}


$(() => {
    ko.applyBindings(new CashierViewModel());
});
