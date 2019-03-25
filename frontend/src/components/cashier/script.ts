import Vue from 'vue';
import {
    mapActions,
    mapGetters,
    mapMutations
} from 'vuex';
import _ from 'lodash';
import { AxiosResponse } from 'axios';
import { DISCOUNT_TYPES } from '@/entity/sales';
import SalesItem  from '@/entity/sales_item';
import { getDummyCashierPanel } from '@/entity/category';
import { Item } from '@/entity/item';

/**
 * 初期データ取得
 */
const defaultData = (): any => {
    const categories = getDummyCashierPanel();

    return {
        categories: [],
        errors: {},
        items: categories[0].items,
        saving: false,
        discountMode: DISCOUNT_TYPES.PRICE,
    };
};

export default Vue.extend({
    data() {
        let data = defaultData();
        return _.extend({},  data);
    },
    mounted() {
        this.fetchCategories();
    },
    computed: {
        ...mapGetters('cashier', [
            'getSales',
            'hasItems',
            'getCharge'
        ]),
        ...mapGetters('category', [
            'getCategories'
        ]),
        /**
         * 値引単位
         */
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
        },
        isDiscountPrice(): boolean {
            return this.discountMode === DISCOUNT_TYPES.PRICE;
        },
        isDiscountRate(): boolean {
            return this.discountMode === DISCOUNT_TYPES.RATE;
        }
    },
    methods: {
        ...mapMutations('cashier', [
            'initialize',
            'addItem',
            'reduceItem',
            'deleteItem',
            'calcTotalPrice',
            'resetDiscountPrice',
            'resetDiscountRate'
        ]),
        ...mapActions('cashier', [
            'save',
        ]),
        ...mapActions('category', [
            'fetchCategories',
        ]),
        /**
         * 明細データ作成 or 数量追加
         * @param {Item} item
         */
        handleIncreaseItem(item: Item): void {
            this.addItem(item);
            this.calcTotalPrice(this.discountMode);
        },
        /**
         * 明細データ削除 or 数量を減らす
         *
         */
        handleDecreaseItem(itemName: string): void {
            this.reduceItem(itemName);
            this.calcTotalPrice(this.discountMode);
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
                    this.deleteItem(index);
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
                    this.initialize();
                    _.assign(this.$data, defaultData());

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
            this.resetDiscountRate();
            this.discountMode = DISCOUNT_TYPES.PRICE;
        },
        /**
         * 値引率切替イベント
         */
        handleChangeDiscountRate(): void {
            this.resetDiscountPrice();
            this.discountMode = DISCOUNT_TYPES.RATE;
        },
        /**
         * 決済ボタンクリックイベント
         */
        handleSave(): void {
            this.saving = true;

            this.save(this.sales)
                .then((response: AxiosResponse<any>) => {
                    this.$toast.open({
                        message: '売上登録しました',
                        type: 'is-success'
                    });

                    this.initialize();
                    _.assign(this.$data, this.$options.data);
                })
                .catch((error: any) => {
                    const response = error.response;
                    let message = '';

                    if (!_.isEmpty(response.data.message)) {
                        message = response.data.message;
                    }

                    if (!_.isEmpty(response.data.errors)) {
                        this.errors = _.extend({}, response.data.errors);
                    }

                    this.$toast.open({
                        message: message,
                        type: 'is-danger'
                    });
                })
                .finally(() => {
                    this.saving = false;
                });
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
    filters: {
        numberWithDelimiter(value: number): string {
            return value ? value.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1,') : '0';
        }
    }
});
