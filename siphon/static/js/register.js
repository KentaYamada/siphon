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

var RegisterViewModel = function() {
    var self = this;

    // Properties
    self.categories = ko.observableArray();
    self.products = ko.observableArray();
    self.sales = ko.observable();
    self.items = ko.observableArray();

    // set dummy
    var dummy = getDummyData();
    self.categories(dummy);
    self.products(self.categories()[0][0].products);

    // Actions.
}

ko.applyBindings(new RegisterViewModel());
