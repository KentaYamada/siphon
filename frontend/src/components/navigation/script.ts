import Vue from 'vue';


const getMenu = () => {
    return [
        {
            title: '売上',
            icon: 'fa-coins',
            submenu: [
                {title: '売上登録', icon: 'fa-cash-register', url: '/cashier', submenu: null},
                {title: '1日の売上', icon: 'fa-calendar-day', url: '', submenu: null}
            ]
        },
        {
            title: '設定',
            icon: 'fa-user-cog',
            submenu: [
                {title: '商品カテゴリ', icon: 'fa-tag', url: '/categories', submenu: null},
                {title: '商品', icon: 'fa-coffee', url: '/items', submenu: null},
                {title: 'ユーザー', icon: 'fa-users', url: '/users', submenu: null}
            ]
        }
    ];
};


export default Vue.extend({
    template: '<navigation/>',
    data() {
        const menu = getMenu();

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

