import Vue from 'vue';
import User from '@/entity/user';


export default Vue.extend({
    data() {
        return {
            errors: {
                // name: 'ユーザー名は必須です',
                // password: 'パスワードは半角英数字を入力してください'
            }
        };
    },
    methods: {
        handleSave() {
        }
    }
});

