import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import { ToastConfig } from 'buefy/types/components';
import { DailySalesSearchOption } from '@/entity/daily_sales';

/**
 * 日次売上一覧
 */
export default Vue.extend({
    data() {
        const option: DailySalesSearchOption = {
            time_from: '',
            time_to: '',
            q: ''
        };

        return {
            option
        };
    },
    mounted() {
        this.fetchDailySales(this.option);
    },
    computed: {
        ...mapGetters('daily_sales', [
            'getDailySales',
            'hasItems'
        ])
    },
    methods: {
        ...mapActions('daily_sales', [
            'fetchDailySales',
            'cancel'
        ]),
        /**
         * 売上検索
         */
        handleSearch(): void {
            this.fetchDailySales(this.option);
        },
        /**
         * 検索条件クリア
         */
        handleClearConditions(): void {
            this.option.time_from = '';
            this.option.time_to = '';
            this.option.q = '';
        },
        /**
         * 売上取消
         * @param {int} salesId
         */
        handleCancelSales(salesId: number): void {
            const message = `
                <div>売上を取り消します。よろしいですか？</div>
                <small>Note: 取り消したデータを差し戻すことはできません</small>
            `;

            // todo: callback
            this.$dialog.confirm({
                title: '売上取消',
                message: message,
                confirmText: '取消',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    this._cancel(salesId);
                }
            });
        },
        /**
         * 売上取り消し実行
         * @param salesId 
         */
        _cancel(salesId: number): void {
            this.cancel(salesId)
                .then(() => {
                    const option: ToastConfig = {
                        message: '売上取り消しました',
                        type: 'is-success'
                    };

                    this.$toast.open(option);
                    this.getDailySales(this.option);
                })
                .catch((error: any) => {
                    const option: ToastConfig = {
                        message: '売上取り消しに失敗しました',
                        type: 'is-danger'
                    };
                    this.$toast.open(option);
                });
        }
    }
});

