import Vue from 'vue';
import { getMenus } from '@/entity/menu';
import { mapGetters } from 'vuex';

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
            console.log('logout event run')
        }
    }
});

