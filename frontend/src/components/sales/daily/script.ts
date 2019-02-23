import Vue from 'vue';


export default Vue.extend({
    data() {
        let dailySales = [];
        let searchCondition = {
            time_from: null,
            time_to: null,
            q: 'Siphon'
        };

        for (let i = 0; i < 10; i++) {
            let items = [];

            for (let j = 1; j < 10; j++) {
                items.push({
                    item_name: 'Item',
                    price: 500,
                    amount: j,
                    subtotal: j * 500
                });
            }

            dailySales.push({items: items});
        }

        return {
            dailySales,
            searchCondition
        };
    },
    methods: {
        /**
         * 売上検索
         */
        handleSearch(): void {
        },
        /**
         * 検索条件クリア
         */
        handleClearConditions(): void {
            this.searchCondition.time_from = null;
            this.searchCondition.time_to = null;
            this.searchCondition.q = '';
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
                    // todo: call cancel api
                    this.cancelSalesSuccess();
                    this.cancelSalesFailed();
                }
            });
        },
        /**
         * 売上取消後のコールバック
         */
        cancelSalesSuccess(): void {
            console.log('success');
        },
        /**
         * 売上取消失敗時のエラーハンドラ
         */
        cancelSalesFailed(): void {
            console.log('failed');
        }
    }
});

