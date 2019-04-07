import Vue from 'vue';
import { mapActions } from 'vuex';
import { ToastConfig } from 'buefy/types/components';
import { DailySales } from '@/entity/daily_sales';


export default Vue.extend({
    data() {
        return {
            isOpen: false,
        };
    },
    template: '<daily-sales-item/>',
    props: {
        dailySales: {
            required: true
        }
    },
    methods: {
        ...mapActions('daily_sales', [
            'cancel'
        ]),
        handleClickHeader(): void {
            this.isOpen = !this.isOpen;
        },
        /**
         * 売上取消
         */
        handleCancel(): void {
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
                    this._cancel((<DailySales>this.dailySales).sales_id);
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
