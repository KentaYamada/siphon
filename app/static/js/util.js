'use strict';


/**
 * Request api
 * @param {string} url
 * @param {string} method
 * @param {object} data
 * @return JQueryXHR
 */
function requestApi(url, method, data) {
    var option = {
        contentType: 'application/json',
        data: data,
        dataType: 'json',
        method: method,
        url: url
    };

    return $.ajax(option);
}
