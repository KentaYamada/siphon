import Vue from 'vue';


export default Vue.extend({
    template: '<navigation/>',
    data() {
        const menu = [
            {
                title: '売上',
                submenu: [
                    {title: '売上登録', url: '/cashier'},
                    // {title: '本日の売上', url: '/sales/daily'},
                ]
            },
            {
                title: '設定',
                submenu: [
                    {title: '商品カテゴリ', url: '/categories'},
                    {title: '商品', url: '/items'},
                    {title: 'ユーザー', url: '/users'}
                ]
            }
        ];

        return { menu };
    },
    computed: {
        isLoggedIn(): boolean {
            return true;
        }
    }
});

