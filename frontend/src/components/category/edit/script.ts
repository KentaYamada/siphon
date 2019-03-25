import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import _ from 'lodash';
import { AxiosResponse } from 'axios';

export default Vue.extend({
    data() {
        return {
            category: {},
            errors: {}
        };
    },
    mounted() {
        this.category = this.findOrCreate(this.id);
    },
    props: {
        id: {
            type: Number
        }
    },
    computed: {
        ...mapGetters('category', [
            'findOrCreate'
        ])
    },    
    methods: {
        ...mapActions('category', [
            'save'
        ]),
        /**
         * 保存イベント
         */
        handleSave(): void {
            this.save(this.category)
                .then((response: AxiosResponse) => {
                    this.$emit('close');
                    this.$emit('save-success', response.data.message);
                })
                .catch((error: any) => {
                    const response = error.response;
                    let message = '';

                    if (!_.isUndefined(response)) {
                        message = response.data.message;

                        if (!_.isEmpty(response.data.errors)) {
                            this.errors =  _.extend({}, response.data.errors);
                        }
                    } else {
                        message = 'システムエラー発生';
                    }

                    this.$toast.open({
                        message: message,
                        type: 'is-danger'
                    });
                });
        }
    }
});
