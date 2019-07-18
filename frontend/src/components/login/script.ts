import Vue from 'vue';
import { mapActions, mapGetters } from 'vuex';
import { ToastConfig } from 'buefy/types/components';


export default Vue.extend({
    data() {
        return {
            isError: false
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
            this.login()
                .then(() => {
                    this.onLoginSuccess();
                })
                .catch(() => {
                    this.onLoginFailed();
                });
        },
        /**
         * ログイン成功した時のcallback
         */
        onLoginSuccess(): void {
            this.isError = false;
            this.$router.push('/');
        },
        /**
         * ログイン失敗した時のcallback
         */
        onLoginFailed(): void {
            this.isError = true;
            const option = {
                message: 'ログインに失敗しました',
                type: 'is-danger'
            } as ToastConfig;
            this.$toast.open(option);
        }
    },
});

