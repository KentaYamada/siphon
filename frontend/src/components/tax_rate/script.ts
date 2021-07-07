import Vue from 'vue';
import {
    mapActions,
    mapState,
} from 'vuex';
import _ from 'lodash';
import { ToastConfig } from 'buefy/types/components';
import { AxiosResponse, AxiosError } from 'axios';


export default Vue.extend({
    data() {
        return {
            errors: {}
        };
    },
    mounted() {
        this.fetchTaxRate();
    },
    computed: {
        ...mapState('tax_rate', [
            'tax_rate'
        ]),
    },
    methods: {
        ...mapActions('tax_rate', [
            'fetchTaxRate',
            'save'
        ]),
        handleSave(): void {
            this.errors = {};
            this.save()
                .then((response: AxiosResponse<any>) => {
                    const message: string = response.data.message;
                    this._saveSuccess(message);
                })
                .catch((error: AxiosError) => {
                    this._saveFailure(error);
                });
        },
        _saveSuccess(message: string): void {
            const option: ToastConfig = {
                message: message,
                type: 'is-success'
            };
            this.$toast.open(option);
        },
        _saveFailure(error: any): void {
            const errors = error.response.data.errors;

            if (!_.isUndefined(errors)) {
                this.errors = errors;
            }

            const option: ToastConfig = {
                message: error.response.data.message,
                type: 'is-danger'
            }

            this.$toast.open(option);
        }
    }
});
