"use strict";

//
// Array to 2 dimention array.
//
function toDimentionArray(arr, row, col) {
    var res = [];
    var offset = 0;

    for(var i = 0; i < row; i++) {
        res.push(arr.slice(offset, col+offset));
        offset += col;
    }

    return res;
}

//
// Generate Category and Product dummy data.
//
function getDummyData() {
    var categories = [];
    var productID = 1;

    for(var i = 1; i <= 10; i++) {
        var category = {
            "id": i,
            "name": "Category" + i,
            "products": []
        };

        for(var j = 1; j <= 30; j++) {
            category.products.push({
                "id": productID,
                "name": "Product" + productID,
                "price": j * 100
            });
            productID++;
        }

        category.products = toDimentionArray(category.products, 10, 3);
        categories.push(category);
    }

    categories = toDimentionArray(categories, 2, 5);
    return categories;
}


var Sales = function() {
    var self = this;
    self.deposit = ko.observable(0);
    self.discount = ko.observable(0);
    //self.mode = ko.observable('price');
    self.mode = 'rate';
    self.items = ko.observableArray();

    self.total = ko.computed(function() {
        var val = 0;
        ko.utils.arrayForEach(self.items(), function(item) {
            val += item.subtotal();
        });

        if(self.mode == 'price') {
            val -= self.discount();
        }

        if(self.mode == 'rate') {
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
        self.mode = 'price';
        self.items.removeAll();
    }

    self.save = function() {
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

    // Properties
    self.categories = ko.observableArray();
    self.products = ko.observableArray();
    self.sales = ko.observable(new Sales());
    self.items = ko.observableArray(self.sales().items());

    // set dummy
    var dummy = getDummyData();
    self.categories(dummy);
    self.products(self.categories()[0][0].products);

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
    // Switch discount mode event.
    //
    self.onSwitchDiscount = function() {
        if(self.sales.mode == 'price') {
            self.sales.mode = 'rate';
        }

        if(self.sales.mode == 'rate') {
            self.sales.mode = 'price';
        }
    }
}

ko.applyBindings(new RegisterViewModel());
