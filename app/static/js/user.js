'user strict';


class UserViewModel {
    constructor() {
        this.modalId = ko.observable('user_edit_modal');
        this.users = ko.observableArray([
            { username: '山田 太郎', nickname: 'ドカベン'},
            { username: '里中 智', nickname: '小さな巨人'}
        ]);
        this.user = ko.observable({
            username: '',
            nickname: '',
            email: '',
            password:'',
            confirm_password:''
        });

        // bind this
        this.onDelete = this.onDelete.bind(this);
        this.onShowEditDialog = this.onShowEditDialog.bind(this);
    }

    onDelete() {
        let modalId = 'delete_user_alert';
        this.modalId(modalId);
        $(`#${this.modalId()}`).modal();
    }

    onShowAddDialog() {
    }

    /**
     * 編集モードで設定画面表示
     * @param user 選択したユーザー
     */
    onShowEditDialog(user) {
        $(`#${this.modalId()}`).modal();
    }
}


ko.applyBindings(new UserViewModel());
