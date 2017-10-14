"use strict";

//
// Call API.
// @params
//   url string: URL
//   method string: request method(GET, POST etc...)
//   data object: request parameter.
// @return 
//
function requestApi(url, method, data) {
    return jQuery.ajax({
        accepts: 'application/json',
        cache: false,
        contentType: 'application/json',
        data: ko.toJSON(data),
        dataType: 'json',
        type: method,
        url: url
    });
}
