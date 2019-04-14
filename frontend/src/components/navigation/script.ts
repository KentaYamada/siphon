import Vue from 'vue';
import { getMenus } from '@/entity/menu';

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
        isLoggedIn(): boolean {
            return true;
        }
    },
    methods: {
        toggleNav(): void {
            this.showNav = !this.showNav;
        },
        handleCloseNav(): void {
            this.showNav = false;
        }
    }
});

