'use strict';


class Category {
    constructor(id, name) {
        this.id = ko.observable(id);
        this.name = ko.observable(name);
    }

    save() {
        var url = '/api/categories/';
        var method = 'POST';

        if (this.id() !== null) {
            url += this.id();
            method = 'PUT';
        }

        return requestApi(url, method, ko.toJSON(this));
    }

    remove() {
        var url = `/api/categories/${this.id()}`;
        return requestApi(url, 'DELETE', null);
    }

    static findAll() {
        return requestApi('/api/categories/', 'GET', null);
    }
}
