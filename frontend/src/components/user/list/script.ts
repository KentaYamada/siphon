import Vue from 'vue';
import User from '@/entity/user';
import UserEdit from '@/components/user/edit/UserEdit.vue';

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
        handleNew(): void {
            this.$modal.open({
                parent: this,
                component: UserEdit,
                hasModalCard: true,
                props: {
                    user: {}
                }
            });
        },
        handleEdit(user: User): void {
            this.$modal.open({
                parent: this,
                component: UserEdit,
                hasModalCard: true,
                props: {
                    user: user
                }
            });
        },
        handleDelete(user: User): void {
            this.$dialog.confirm({
                title: 'ユーザー削除',
                message: `<div>${user.name}を削除しますか？<div><small>Note:削除したデータを元に戻すことはできません</small>`,
                confirmText: '削除',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger'
            });
        }
    }
});
