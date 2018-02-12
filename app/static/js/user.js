"use strict";

var User = function(id, name, email, password) {
    var self = this;
    self.END_POINT = "/api/users"
    self.id = ko.observable(id);
    self.name = ko.observable(name);
    self.email = ko.observable(email);
    self.password = ko.observable(password);

    self.add = function() {
        requestApi(self.END_POINT, "POST", ko.toJSON(self))
            .done(function(data) {
                console.log(data);
            })
            .fail(function() {
                console.error("Failed request");
            });
    }

    self.edit = function() {
        var url = self.END_POINT + "/" + self.id();
        requestApi(url, "PUT", ko.toJSON(self))
            .done(function(data) {
                console.log(data);
            })
            .fail(function() {
                console.error("Failed request");
            });
    }

    self.remove = function() {
        var url = self.END_POINT + "/" + self.id();
        requestApi(url, "DELETE")
            .done(function(data) {
                console.log(data);
            })
            .fail(function() {
                console.error("Failed request");
            });
    }

    self.findBy = function() {
        requestApi(self.END_POINT, "GET")
            .done(function(data) {
            })
            .fail(function() {
            });
    }

    self.authoricate = function(userId, password) {
        var args = {"name": userId, "password": password};
        requestApi(self.END_POINT, "GET", $.toJSON(args))
            .done(function(data) {
            })
            .fail(function() {
            });
    }
}


var AuthoricationViewModel = function() {
}


ko.applyBindings(new AuthoricationViewModel());
