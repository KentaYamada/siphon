"use strict";

//
// Request API using ajax.
// @params
//   url string: URL
//   method string: request method(GET, POST etc...)
//   data object: request parameter.
// @return
//
function requestApi(url, method, data) {
    var options = {
        accepts: 'application/json',
        cache: false,
        contentType: 'application/json',
        data: ko.toJSON(data),
        dataType: 'json',
        type: method,
        url: url
    };

    return $.ajax(options);
}

class ModelBase {
    constructor() {
        this.endpoint = '';
        this.id = ko.observable();
        this.urlWithId = ko.computed(() => {
            return this.endpoint + '/' + this.id();
        }, this);
    }


    add() {
        requestApi(this.endpoint, 'POST', ko.toJSON(this))
            .done((res) => {
                console.log(res);
            })
            .fail(() => {
                console.error('Failed add request.');
            });
    }

    edit() {
        if (!this.id()) {
            throw new Error('id should be set.');
        }

        let url = this.urlWithId();

        requestApi(url, 'PUT', ko.toJSON(this))
            .done((res) => {
                console.log(res);
            })
            .fail(() => {
                console.error('Failed add request.');
            });
    }

    remove() {
        if (!this.id()) {
            throw new Error('id cannot null.');
        }

        let url = this.endpoint + '/' + this.id();

        requestApi(url, 'DELETE')
            .done((res) => {
            })
            .fail(() => {
                console.erro('Failed add request.');
            });
    }

    // Todo: static methodにする
    find(condition, callback) {
        requestApi(this.endpoint, 'GET')
            .done((res) => {
                if (callback) {
                    callback(res);
                }
            });
    }
}

class ViewModelBase {
    constructor() {
        this.title = '';
        this.model = ko.observable();
        this.models = ko.observableArray([]);
    }

    /**
     * Add event handler.
     */
    onAdd() {
        this.model().add();
    }

    /**
     * Edit event handler.
     */
    onEdit() {
        this.model().edit();
    }

    /**
     * Remove event handler.
     */
    onRemove() {
        this.model().remove();
    }

    /**
     * Show create data dialog.
     */
    onShowAddForm() {
        $('#entryForm').modal('show');
    }

    /**
     * Show edit data dialog.
     * @param model Object: target data.
     */
    onShowEditForm(data) {
        this.model(data);
        $('#entryForm').modal('show');
    }

    /**
     * Show alert when before remove
     */
    onShowRemoveAlert(data) {
        this.model(data);
        jQuery('#removeAlert').modal('show');
    }
}
