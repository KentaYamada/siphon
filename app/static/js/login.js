'use strict';


class LoginViewModel {
    constructor() {

    }

    onAuthoricate() {
        requestApi('/api/users/authoricate', 'POST', { username: 'hoge', password: 'fuga' })
            .done(function(data) {
                console.log(data);
                if (data.authoricate) {
                    window.location.href = data.redirect_url;
                }
            });

    }
}


$(function() {
    ko.applyBindings(new LoginViewModel());
});
