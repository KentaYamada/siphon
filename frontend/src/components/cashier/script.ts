import Vue from 'vue';
import _ from 'lodash';
import Sales from '@/entity/sales';
import SalesItem from '@/entity/sales_item';
import Category from '@/entity/category';
import Item from '@/entity/item';

/**
 * 値引種別
 */
enum DISCOUNT_TYPES {
    // 値引額
    PRICE,
    // 値引率
    RATE
};

export default Vue.extend({
    data(): any {
        const sales = new Sales();
        const categories = Category.getDummyCashierPanel();
        const items = categories[0].items;
        const discountMode = DISCOUNT_TYPES.PRICE;
        const saving = false;
        const charge = 0;

        return {
            sales,
            sales_items: sales.items,
            items,
            saving,
            charge,
            discountMode,
            errors: {}
        };
    },
    watch: {
        'sales.total_price': function(val: number) {
            this.charge = this.sales.deposit - val;
        },
        'sales.deposit': function(val: number) {
            this.charge = val - this.sales.total_price;
        }
    },
    methods: {
        /**
         * 明細データ作成 or 数量追加
         * @param {Item} item
         */
        handleIncreaseItem(item: Item): void {
            this.sales.increaseItem(item);
        },
        /**
         * 明細データ削除 or 数量を減らす
         *
         */
        handleDecreaseItem(itemName: string): void {
            this.sales.decreaseItem(itemName);
        },
        /**
         * 明細データ削除
         */
        handleDeleteItem(salesItem: SalesItem, index: number): void {
            this.$dialog.confirm({
                title: '明細データ削除',
                message: `${salesItem.item_name}を削除します。よろしいですか？`,
                confirmText: '削除',
                cancelText: 'キャンセル',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    this.sales.deleteItem(salesItem, index);
                    this.$toast.open({
                        message: '削除しました。',
                        type: 'is-success'
                    });
                }
            });
        },
        /**
         * 入力中の売上データリセットイベント
         */
        handleClearSales(): void {
            this.$dialog.confirm({
                title: '売上データクリア',
                message: '入力中の売上データをクリアします。よろしいですか？',
                confirmText: 'クリア',
                cancelText: 'キャンセル',
                hasIcon: true,
                type: 'is-warning',
                onConfirm: () => {
                    this.sales = new Sales();
                    this.sales_items.splice(0, this.sales_items.length);
                    this.$toast.open({
                        message: 'クリアしました',
                        type: 'is-success'
                    });
                }
            });
        },
        /**
         * 値引額切替イベント
         */
        handleChangeDiscountPrice(): void {
            this.sales.discount_rate = 0;
            this.discountMode = DISCOUNT_TYPES.PRICE;
        },
        /**
         * 値引率切替イベント
         */
        handleChangeDiscountRate(): void {
            this.sales.discount_price = 0;
            this.discountMode = DISCOUNT_TYPES.RATE;
        },
        /**
         * 決済ボタンクリックイベント
         */
        handleSave(): void {
            this.saving = true;
            setTimeout(() => {
                this.saving = false;
                // todo: call save api
                const saved = true;
                const message = saved ? '売上登録しました' : '売上登録に失敗しました';
                const toastType = saved ? 'is-success' : 'is-danger';

                this.$toast.open({
                    message: message,
                    type: toastType
                });
            }, 4000);
        },
        /**
         * 明細データ削除確認画面表示
         * @param {string} item_name
         * @param {number} index
         */
        _showDeleteConfirm(item_name: string, index: number): void {
            this.$dialog.confirm({
                title: '明細データ削除',
                message: `${item_name}を削除します。よろしいですか？`,
                confirmText: '削除',
                cancelText: 'キャンセル',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    this.sales.deleteItem(index);
                    this.$toast.open({
                        message: '削除しました。',
                        type: 'is-success'
                    });
                }
            });
        }
    },
    computed: {
        hasItems(): boolean {
            return this.sales.items.length > 0;
        },
        discountUnit(): string {
            let unit = '';            

            switch (this.discountMode) {
                case DISCOUNT_TYPES.PRICE:
                    unit = '円';
                    break;
                case DISCOUNT_TYPES.RATE:
                    unit = '％';
                    break;
                default:
                    // do nothing
                    break;
            };

            return unit;
        }
    },
    filters: {
        numberWithDelimiter(value: number): string {
            return value ? value.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1,') : '0';
        }
    }
});

