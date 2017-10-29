"use strict";

var User = function() {
    var self = this;
    self.username = ko.observable();
    self.password = ko.observable();
}

var LoginViewModel = function() {
    var self = this;
    self.loginUser = ko.observable(new User());
    self.validate = ko.computed(function() {
    });

    self.login = function() {
        // Todo: request api
    }
}

ko.applyBindings(new LoginViewModel());
