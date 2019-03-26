import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import { AxiosResponse } from 'axios';


export default Vue.extend({
    data() {
        return {
            isError: false,
            errors: {}
        };
    },
    computed: {
        ...mapGetters('auth', [
            'getAuth'
        ])
    },
    methods: {
        ...mapActions('auth', [
            'login'
        ]),
        /**
         * ログインボタンクリックイベント
         */
        handleLogin(): void {
            // todo: 認証情報の保持とかとか
            this.login()
                .then((response: AxiosResponse) => {

                })
                .catch((error: any) => {
                    this.isError = true;
                });
        },
    },
});

