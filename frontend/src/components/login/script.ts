import Vue from 'vue';
import Authrication from '@/entity/auth';


export default Vue.extend({
    data() {
        return {
            user: new Authrication('', ''),
            error: false
        };
    },
    computed: {
        isError(): boolean {
            return this.error;
        }
    },
    methods: {
        /**
         * ログインボタンクリックイベント
         */
        handleLogin(): void {
            this.isError = this.user.email !== 'test' ||
                this.user.password !== 'test';
        },
    },
});

