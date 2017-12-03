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
