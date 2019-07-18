import Vue from 'vue';
import { getMenus } from '@/entity/menu';
import { mapGetters, mapActions } from 'vuex';
import { ToastConfig } from 'buefy/types/components';


/**
 * ナビゲーションメニュー
 */
export default Vue.extend({
    template: '<navigation/>',
    data() {
        const menu = getMenus();

        return {
            menu,
            showNav: false
        };
    },
    computed: {
        ...mapGetters('auth', [
            'isLoggedIn'
        ])
    },
    methods: {
        ...mapActions('auth', [
            'logout'
        ]),
        toggleNav(): void {
            this.showNav = !this.showNav;
        },
        handleCloseNav(): void {
            this.showNav = false;
        },
        /**
         * @event logout button click event
         */
        handleLogout(): void {
            this.logout()
                .then(() => {
                    this.onLogoutSuccess();
                })
                .catch(() => {
                    this.onLogoutFailed();
                });
        },
        onLogoutSuccess(): void {
            const option = {
                message: 'ログアウトしました',
                type: 'is-success'
            } as ToastConfig;
            this.$toast.open(option);
            this.$router.push('/login');
        },
        onLogoutFailed(): void {

        }
    }
});

