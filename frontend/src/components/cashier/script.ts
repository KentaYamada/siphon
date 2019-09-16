import Vue from 'vue';
import {
    mapActions,
    mapGetters,
    mapMutations,
    mapState,
} from 'vuex';
import _ from 'lodash';
import { DISCOUNT_TYPES } from '@/entity/sales';
import { TAX_OPTIONS } from '@/entity/tax_rate';
import { SalesItem, TargetItem } from '@/entity/sales_item';
import { Item } from '@/entity/item';
import { AxiosError } from 'axios';


const defaultData = (): any => {
    return {
        errors: {},
        saving: false,
        isFocusedDposit: false,
        isFocusedDiscount: false,
        discountMode: DISCOUNT_TYPES.PRICE,
        taxOption: TAX_OPTIONS.NORMAL,
    };
}


export default Vue.extend({
    data() {
        return _.extend({}, defaultData());
    },
    mounted() {
        this.initialize();
        this.fetchSelectionItems();
    },
    computed: {
        ...mapState('cashier', [
            'sales',
            'categories',
        ]),
        ...mapGetters('cashier', [
            'grandTotalPrice',
            'charge',
            'normalTaxSalesItems',
            'reducedTaxSalesItems',
            'hasSalesItems',
            'hasNormalTaxSalesItems',
            'hasReducedTaxSalesItems',
            'currentItems',
            'hasItems'
        ]),
        grand_total_price(): number {
            return this.grandTotalPrice(this.discountMode);
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
        },
        isDiscountPrice(): boolean {
            return this.discountMode === DISCOUNT_TYPES.PRICE;
        },
        isDiscountRate(): boolean {
            return this.discountMode === DISCOUNT_TYPES.RATE;
        },
        isNormalTax(): boolean {
            return this.taxOption === TAX_OPTIONS.NORMAL;
        },
        isReducedTax(): boolean {
            return this.taxOption == TAX_OPTIONS.REDUCED;
        },
    },
    methods: {
        ...mapMutations('cashier', [
            'initialize',
            'addSalesItem',
            'deleteSalesItem',
            'increaseSalesItem',
            'decreaseSalesItem',
            'setDeposit',
            'setDiscountPrice',
            'setDiscountRate',
            'setItems',
            'resetDiscountPrice',
            'resetDiscountRate',
        ]),
        ...mapActions('cashier', [
            'fetchSelectionItems',
            'save',
        ]),
        /**
         * 明細 or 数量追加
         * @event
         * @param item 
         */
        handleAddSalesItem(item: Item): void {
            const data = {
                item: item,
                tax_option: this.taxOption,
            } as TargetItem;

            this.addSalesItem(data);
        },
        /**
         * 明細データ削除
         * @event
         * @param salesItem 
         * @param index 
         */
        handleDeleteSalesItem(salesItem: SalesItem): void {
            const confirmOption = {
                title: '明細データ削除',
                message: `『${salesItem.name}』を削除します。よろしいですか？`,
                confirmText: '削除',
                cancelText: 'キャンセル',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    const data = {
                        item: salesItem,
                        tax_option: this.taxOption,
                    } as TargetItem;

                    this.deleteSalesItem(data);
                    this.$toast.open({
                        message: '削除しました。',
                        type: 'is-success'
                    });
                }
            };
            this.$dialog.confirm(confirmOption);
        },
        /**
         * 明細数量を増やす
         * @event
         * @param index 
         */
        handleIncreaseSalesItem(salesItem: SalesItem): void {
            const data = {
                item: salesItem,
                tax_option: this.taxOption
            } as TargetItem;

            this.increaseSalesItem(data);
        },
        /**
         * 明細数量を減らす
         * @event
         * @param itemName 
         */
        handleDecreaseSalesItem(salesItem: SalesItem): void {
            const data = {
                item: salesItem,
                tax_option: this.taxOption
            } as TargetItem;

            this.decreaseSalesItem(data);
        },
        /**
         * フォーカスしてるinputの値クリア
         * @event
         */
        handleClearInput(): void {
            if (this.isFocusedDposit) {
                this.setDeposit(0);
            }
        },
        /**
         * 商品切替イベント
         * @event
         */
        handleSwitchItems(categoryId: number): void {
            this.setItems(categoryId);
        },
        /**
         * 通常税率モードへ切替
         * @event
         */
        handleSwitchNormalTax(): void {
            this.taxOption = TAX_OPTIONS.NORMAL;
        },
        /**
         * 軽減税率モードへ切替
         * @event
         */
        handleSwitchReducedTax(): void {
            this.taxOption = TAX_OPTIONS.REDUCED;
        },
        /**
         * 値引額モードへ切替
         * @event
         */
        handleSwitchDiscountPrice(): void {
            this.resetDiscountRate();
            this.discountMode = DISCOUNT_TYPES.PRICE;
        },
        /**
         * 値引率モードへ切替
         * @event
         */
        handleSwitchDiscountRate(): void {
            this.resetDiscountPrice();
            this.discountMode = DISCOUNT_TYPES.RATE;
        },
        /**
         * 数値ボタンクリック
         * @event
         * @param value 
         */
        handleClickNumpad(value: number): void {

        },
        /**
         * 売上登録
         * @event
         */
        handleSave(): void {
            this.save()
                .then(() => {
                    this._saveSuccess();
                })
                .catch((error: AxiosError) => {
                    this._saveFailure(error.response);
                })
                .finally(() => {

                });
        },
        /**
         * 登録成功時のcallback
         */
        _saveSuccess(): void {
            const option = {
                message: '売上登録しました',
                type: 'is-success',
            };
            this.$toast.open(option);

            this.initialize();
            _.assign(this.$data, this.$options.data);
        },
        /**
         * 登録失敗時のcallback
         * @param error 
         */
        _saveFailure(error: any) {
        },
    }
});
