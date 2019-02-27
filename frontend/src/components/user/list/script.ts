import Vue from 'vue';
import User from '@/entity/user';
import UserEdit from '@/components/user/edit/UserEdit.vue';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';


export default Vue.extend({
    data() {
        const users = User.getDummyUsers();

        return {
            users
        };
    },
    computed: {
        hasItems(): boolean {
            return this.users.length > 0;
        }
    },
    methods: {
        /**
         * ユーザー検索
         */
        handleSearch(): void {

        },
        /**
         * ユーザー新規登録
         */
        handleNew(): void {
            this._openEditModal(new User(0, '', '', '', ''));
        },
        handleEdit(user: User): void {
            this._openEditModal(user);
        },
        /**
         * 商品削除
         * @param {User} user
         */
        handleDelete(user: User): void {
            const message = `
                <div>${user.name}を削除しますか？<div>
                <small>Note:削除したデータを元に戻すことはできません</small>`;
            const option: DialogConfig = {
                title: 'ユーザー削除',
                message: message,
                confirmText: '削除',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    // todo: call delete api
                    this.deleteSuccess();
                    this.deleteFailed();
                }
            };
            this.$dialog.confirm(option);
        },
        deleteSuccess(): void {
            console.log('success');
        },
        deleteFailed(): void {
            console.log('failed');
        },
        /**
         * 編集モーダル表示
         * @param {User} user
         */
        _openEditModal(user: User): void {
            const option: ModalConfig = {
                parent: this,
                component: UserEdit,
                hasModalCard: true,
                props: {
                    user: user
                },
                events: {
                    'save-success': () => {
                        const option: ToastConfig = {
                            message: '保存しました',
                            type:'is-success'
                        };
                        this.$toast.open(option);
                    }
                }
            };
            this.$modal.open(option);
        }
    }
});
