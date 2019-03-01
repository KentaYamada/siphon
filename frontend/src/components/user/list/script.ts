import Vue from 'vue';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';
import {
    User,
    UserSearchOption
} from '@/entity/user';
import UserEdit from '@/components/user/edit/UserEdit.vue';
import UserService from '@/api/user.service';
import { AxiosResponse } from 'axios';


export default Vue.extend({
    data() {
        return {
            users: []
        };
    },
    mounted() {
        this._fetch();
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
            this._fetch();
        },
        /**
         * ユーザー新規登録
         */
        handleNew(): void {
            const newUser: User = {
                id: null,
                name: '',
                nickname: '',
                email: '',
                password: ''
            };
            this._openEditModal(newUser);
        },
        /**
         * ユーザー編集
         */
        handleEdit(user: User): void {
            this._openEditModal(user);
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
         * ユーザー一覧取得
         */
        _fetch(): void {
            const option: UserSearchOption = {
                q: ''
            };
            UserService.fetchUsers(option)
                .then((response: AxiosResponse<any>) => {
                    this.users = response.data.users;
                })
                .catch((error: any) => {

                });
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
                        this._fetch();
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
            UserService.deleteUser(user.id)
                .then((response: AxiosResponse<any>) => {
                    this.$toast.open({
                        message: '削除しました',
                        type: 'is-success'
                    });
                    this._fetch();
                })
                .catch((error: any) => {

                });
        }
    }
});
