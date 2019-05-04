import Vue from 'vue';
import { mapActions } from 'vuex';
import { ToastConfig } from 'buefy/types/components';
import { DailySales } from '@/entity/daily_sales';
import { DISCOUNT_TYPES } from '@/entity/sales';

export default Vue.extend({
    data() {
        return {
            isOpen: true
        }
    },
    template: '<daily-sales-item/>',
    props: {
        dailySales: {
            required: true
        }
    },
    computed: {
        discountUnit(): string {
            let unit_text = '';

            switch(this.dailySales.discount_mode) {
                case DISCOUNT_TYPES.PRICE:
                    unit_text = '(円)';
                break;
                case DISCOUNT_TYPES.RATE:
                    unit_text = '(％)';
                break;
                default:
                    // Do nothing
                break;
            }
            return unit_text;
        }
    },
    methods: {
        ...mapActions('daily_sales', [
            'cancelSales'
        ]),
        /**
         * 売上取消
         */
        handleCancel(): void {
            const message = `
            <div>売上を取り消します。よろしいですか？</div>
            <small>注: 取り消したデータを差し戻すことはできません</small>`;

            this.$dialog.confirm({
                title: '売上取消',
                message: message,
                confirmText: '取消',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    this._cancel((<DailySales>this.dailySales).id);
                }
            });
        },
        /**
         * 売上取り消し実行
         * @param salesId 
         */
        _cancel(salesId: number): void {
            this.cancelSales(salesId)
                .then(() => {
                    const option: ToastConfig = {
                        message: '売上取り消しました',
                        type: 'is-success'
                    };

                    this.$toast.open(option);
                })
                .catch((error: any) => {
                    const option: ToastConfig = {
                        message: '売上取り消しに失敗しました',
                        type: 'is-danger'
                    };
                    this.$toast.open(option);
                });
        }
    },
    filters: {
        concatDateTime(date: string, time: string): string {
            return `${date} ${time}`;
        },
        formatDiscount (value: number, mode: number): number {
            if (mode === DISCOUNT_TYPES.PRICE) {
                value *= -1;
            }

            return value;
        }
    }
});