import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import _ from 'lodash';
import { AxiosResponse } from 'axios';

export default Vue.extend({
    props: {
        id: {
            type: Number
        }
    },
    data() {
        return {
            item: {},
            errors: {}
        };
    },
    mounted() {
        this.item = this.findOrCreate(this.id);
        this.fetchCategories();
    },
    computed: {
        ...mapGetters('category', [
            'getCategories'
        ]),
        ...mapGetters('item', [
            'findOrCreate',
        ])
    },
    methods: {
        ...mapActions('category', [
            'fetchCategories'
        ]),
        ...mapActions('item', [
            'save',
        ]),
        /**
         * 保存イベント
         */
        handleSave(): void { 
            this.save(this.item)
                .then((response: AxiosResponse<any>) => {
                    this.$emit('close');
                    this.$emit('save-success', response.data.message);
                })
                .catch((error: any) => {
                    const response = error.response;

                    if (!_.isEmpty(response.data.errors)) {
                        this.errors = _.extend({}, response.data.errors);
                    }
                    const message = `<p>${response.data.message}</p>`;
                    this.$toast.open({
                        message: message,
                        type: 'is-danger'
                    });
                });
        }
    }
});
