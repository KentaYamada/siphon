import Vue from 'vue';
import _ from 'lodash';
import { AxiosResponse } from 'axios';
import { User } from '@/entity/user';
import UserService from '@/api/user.service';


export default Vue.extend({
    props: {
        user: {
            required: true,
            //type: User
        }
    },
    data() {
        return {
            errors: {}
        };
    },
    methods: {
        /**
         * 保存イベント
         */
        handleSave(): void {
            UserService.saveUser(this.user)
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
