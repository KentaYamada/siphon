'use strict';


class FlashMessageViewModel {
    constructor() {
        this.message = ko.observable('');
        this.isSuccess = ko.observable(false);
        this.messageStyle = ko.computed(function() {
            return this.isSuccess ? 'alert-success' : 'alert-danger';
        }, this);

        // bind this
        this.onShowSuccessMessage = this.onShowSuccessMessage.bind(this);
        this.onShowFailMessage = this.onShowFailMessage.bind(this);
    }

    onShowSuccessMessage(message) {
        this.message(message);
        this.isSuccess(true);
    }

    onShowFailMessage(message) {
        this.message(message);
        this.isSuccess(false);
    }
}
