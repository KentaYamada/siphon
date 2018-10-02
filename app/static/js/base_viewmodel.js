'use strict';


class BaseViewModel {
    constructor() {
        // flash message properties
        this.canShowFlash = ko.observable(false);
        this.requestResult = ko.observable(false);
        this.message = ko.observable('');
        this.flashMessageClass = ko.computed(function() {
            return this.requestResult() ? 'alert-success' : 'alert-danger';
        }, this);
    }

    showSuccessMessage(message) {
        this.canShowFlash(true);
        this.message(message);
        this.requestResult(true);
    }

    showErrorMessage(message) {
        this.canShowFlash(true);
        this.message(message);
        this.requestResult(false);
    }
}
