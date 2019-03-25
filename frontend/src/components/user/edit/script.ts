import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import _ from 'lodash';
import { AxiosResponse } from 'axios';


/**
 * ユーザー情報編集
 */
export default Vue.extend({
    data() {
        return {
            user: {},
            errors: {}
        };
    },
    mounted() {
        this.user = this.findOrCreate(this.id);
    },
    props: {
        id: {
            type: Number
        }
    },
    computed: {
        ...mapGetters('user', [
            'findOrCreate'
        ])
    },  
    methods: {
        ...mapActions('user', [
            'save'
        ]),
        /**
         * 保存イベント
         */
        handleSave(): void {
            this.save(this.user)
                .then((response: AxiosResponse<any>) => {
                    this.$emit('close');
                    this.$emit('save-success', response.data.message);
                })
                .catch((error: any) => {
                    const response = error.response;

                    // todo: 500 errorはglobalでハンドリング
                    let message = '';
                    if (response.status === 500) {
                        message = `
                            <p>アプリケーションエラーが発生しました</p>
                            <p>エラー内容をシステム管理者へ通知します</p>`;
                    } else {
                        message = response.data.message;
                    }
                    this.$toast.open({
                        message: message,
                        type: 'is-danger'
                    });

                    if (!_.isEmpty(response.data.errors)) {
                        this.errors =  _.extend({}, response.data.errors);
                    }
                });
        }
    }
});
