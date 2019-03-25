import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';
import UserEdit from '@/components/user/edit/UserEdit.vue';
import {
    User,
    UserSearchOption
} from '@/entity/user';


export default Vue.extend({
    data() {
        const option: UserSearchOption = {
            q: ''
        };

        return {
            option
        };
    },
    mounted() {
        this.fetchUsers();
    },
    computed: {
        ...mapGetters('user', [
            'getUsers',
            'hasItems'
        ])
    },
    methods: {
        ...mapActions('user', [
            'fetchUsers',
            'delete'
        ]),
        /**
         * ユーザー検索
         */
        handleSearch(): void {
            this.fetchUsers();
        },
        /**
         * ユーザー新規登録
         */
        handleNew(): void {
            this._openEditModal();
        },
        /**
         * ユーザー編集
         */
        handleEdit(user: User): void {
            this._openEditModal(user.id);
        },
        /**
         * ユーザー削除
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
                    this._onDelete(user);
                }
            };
            this.$dialog.confirm(option);
        },
        /**
         * 編集モーダル表示
         * @param {User} user
         */
        _openEditModal(id?: number | null): void {
            const option: ModalConfig = {
                parent: this,
                component: UserEdit,
                hasModalCard: true,
                props: {
                    id: id
                },
                events: {
                    'save-success': () => {
                        const option: ToastConfig = {
                            message: '保存しました',
                            type:'is-success'
                        };
                        this.$toast.open(option);
                        this.fetchUsers();
                    }
                }
            };
            this.$modal.open(option);
        },
        /**
         * 削除実行
         * @param {User} user 
         */
        _onDelete(user: User): void {
            this.delete(user.id)
                .then(() => {
                    this.$toast.open({
                        message: '削除しました',
                        type: 'is-success'
                    });
                    this.fetchUsers();
                })
                .catch((error: any) => {

                });
        }
    }
});
