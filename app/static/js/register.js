"use strict";


class Sales extends ModelBase {
    constructor() {
        super();
        this.deposit = ko.observable(0);
        this.discount = ko.observable(0);
        this.mode = ko.observable('price');
        this.items = ko.observableArray();

        this.total = ko.computed(() => {
            let total = 0;
            ko.utils.arrayForeach(this.items(), (item) => {
                total += item.subtotal();
            });

            if (this.mode() === 'price') {
                total -= this.discount();
            }

            if (this.mode() === 'rate') {
                total *= (1 - (this.discount() / 100));
            }

            return total;
        });

        this.change = ko.computed(() => {
            return this.deposit() > 0 ? this.deposit() - this.total() : 0;
        });
    }

    //
    // Add item or Update quantity.
    //
    addItem(product) {
        let item = ko.utils.arrayFirst(this.items(), (data) => {
            return data.product_name == product.name;
        });

        if(item === null) {
            this.items.push(new SalesItem(product.name, product.price, 1));
        } else {
            item.quantity(item.quantity() + 1);
        }
    }

    //
    // Reduce quantity or remove item.
    //
    reduceItem(item) {
        item.quantity(item.quantity() -1);

        if(item.quantity() < 1) {
            this.items.remove(item);
        }
    }

    //
    // Reset sales data.
    //
    resetAll() {
        this.deposit(0);
        this.discount(0);
        this.mode('price');
        this.items.removeAll();
    }
}

class SalesItem extends ModelBase {
    constructor(product_name, price, quantity) {
        this.product_name = product_name;
        this.price = price;
        this.quantity = ko.observable(quantity);
        this.subtotal = ko.computed(function() {
            return this.price * this.quantity();
        });
    }
}


var Sales = function() {
    var self = this;
    self.END_POINT = "/api/sales";
    self.deposit = ko.observable(0);
    self.discount = ko.observable(0);
    self.mode = ko.observable('price');
    self.items = ko.observableArray();

    self.total = ko.computed(function() {
        var val = 0;
        ko.utils.arrayForEach(self.items(), function(item) {
            val += item.subtotal();
        });

        if(self.mode() == 'price') {
            val -= self.discount();
        }

        if(self.mode() == 'rate') {
            val *= (1 - (self.discount() / 100));
        }

        return val;
    }, self);

    self.change = ko.computed(function() {
        return self.deposit() > 0 ? self.deposit() - self.total() : 0;
    }, self);


    //
    // Add item or Update quantity.
    //
    self.addItem = function(product) {
        var item = ko.utils.arrayFirst(self.items(), function(data) {
            return data.product_name == product.name;
        });

        if(item == null) {
            self.items.push(new SalesItem(product.name, product.price, 1));
        } else {
            item.quantity(item.quantity() + 1);
        }
    }

    //
    // Reduce quantity or remove item.
    // @params
    //   item object: current item
    //
    self.reduceItem = function(item) {
        item.quantity(item.quantity() -1);
        if(item.quantity() < 1) {
            self.items.remove(item);
        }
    }

    //
    // Reset sales data.
    //
    self.resetAll = function() {
        self.deposit(0);
        self.discount(0);
        self.mode('price');
        self.items.removeAll();
    }

    self.save = function() {
        requestApi(self.END_POINT, 'POST', ko.toJSON(self))
        .done(function(data) {
            console.log(data);
        });
    }
}

var SalesItem = function(product_name, price, quantity) {
    var self = this;
    self.product_name = product_name;
    self.price = price;
    self.quantity = ko.observable(quantity);
    self.subtotal = ko.computed(function() {
        return self.price * self.quantity();
    }, self);
}


var RegisterViewModel = function() {
    var self = this;
    self.categories = ko.observableArray([]);
    self.products = ko.observableArray();
    self.sales = ko.observable(new Sales());
    self.items = ko.observableArray(self.sales().items());

    requestApi('/api/sales', 'GET').done(function(data) {
        self.categories(data.categories);
        self.products(self.categories()[0][0].products);
    });

    //
    // Add item event.
    // @params
    //   product object: clicked product
    //
    self.onAdd = function(product) {
        self.sales().addItem(product);
    }

    //
    // Reduce item event.
    // @params
    //   item object: sales item
    //
    self.onReduce = function(item) {
        self.sales().reduceItem(item);
    }

    //
    // Reset all sales data event.
    //
    self.onResetAll = function() {
        self.sales().resetAll();
    }

    self.onSave = function() {
        self.sales().save();
    }

    //
    // Switch products event.
    // @params
    //   category object: clicked category
    //
    self.onSwitchProducts = function(category) {
        self.products(category.products);
    }

    //
    // Switch discount price mode event.
    //
    self.onSwitchDiscountPrice = function() {
        if(self.sales().mode() == 'rate') {
            self.sales().mode('price');
        }
    }

    //
    // Switch discount rate mode event.
    //
    self.onSwitchDiscountRate = function() {
        if(self.sales().mode() == 'price') {
            self.sales().mode('rate');
        }
    }
}

ko.applyBindings(new RegisterViewModel());
