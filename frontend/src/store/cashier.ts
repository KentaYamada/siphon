import _ from 'lodash';
import axios from 'axios';
import { Sales, DISCOUNT_TYPES } from '@/entity/sales';
import SalesItem from '@/entity/sales_item';
import { Item } from '@/entity/item';
import { CashierState } from '@/store/store_types';


const ROOT_URL = '/api/cashier/';

const state: CashierState = {
    sales: {
        total_price: 0,
        discount_price: 0,
        discount_rate: 0,
        inclusive_tax: 0,
        exclusive_tax: 0,
        deposit: 0,
        items: []
    } as Sales
};

const mutations = {
    /**
     * 売上データ初期化
     */
    initialize: (state: CashierState) => {
        state.sales = {
            total_price: 0,
            discount_price: 0,
            discount_rate: 0,
            inclusive_tax: 0,
            exclusive_tax: 0,
            deposit: 0,
            items: []
        } as Sales;
    },
    /**
     * 商品追加
     */
    addItem: (state: CashierState, selectedItem: Item) =>{
        const index = _.findIndex(state.sales.items, (item: SalesItem) => {
            return selectedItem.name === item.item_name;
        });

        if (index > -1) {
            state.sales.items[index].amount += 1;

            const amount = state.sales.items[index].amount;
            const price = state.sales.items[index].unit_price;
            state.sales.items[index].subtotal = amount * price;
        } else {
            const salesItem: SalesItem = {
                item_name: selectedItem.name,
                unit_price: selectedItem.unit_price,
                amount: 1,
                subtotal: selectedItem.unit_price
            };
            state.sales.items.push(salesItem);
        }

        state.sales.total_price = _.sumBy(state.sales.items, (item: SalesItem) => {
            return item.subtotal;
        });
    },
    /**
     * 商品削減
     * @param {CashierState} state
     * @param {string} itemName
     */
    reduceItem: (state: CashierState, itemName: string) => {
        const index = _.findIndex(state.sales.items, (item: SalesItem) => {
            return itemName === item.item_name;
        });

        if (index > -1) {
            let item = state.sales.items[index];

            if (item.amount > 1) {
                item.amount -= 1;
                const amount = state.sales.items[index].amount;
                const price = state.sales.items[index].unit_price;
                state.sales.items[index].subtotal = amount * price;
            } else {
                state.sales.items.splice(index, 1);
            }

            state.sales.total_price = _.sumBy(state.sales.items, (item: SalesItem) => {
                return item.subtotal;
            });
        }
    },
    /**
     * 商品削除
     * @param {CashierState} state 
     * @param {number} index
     */
    deleteItem: (state: CashierState, index: number) => {
        state.sales.items.splice(index, 1);
        state.sales.total_price = _.sumBy(state.sales.items, (item: SalesItem) => {
            return item.subtotal;
        });
    },
    /**
     * 値引額初期化
     */
    resetDiscountPrice: (state: CashierState) => {
        state.sales.discount_price = 0;
    },
    /**
     * 値引率初期化
     */
    resetDiscountRate: (state: CashierState) => {
        state.sales.discount_rate = 0;
    }
};

const getters = {
    /**
     * 売上データ取得
     */
    getSales: (state: CashierState) => {
        return state.sales;
    },
    /**
     * お釣り取得
     */
    getCharge: (state: CashierState) => {
        const charge = state.sales.deposit - state.sales.total_price;
        return  charge > 0 ? charge : 0;
    },
    /**
     * 売上総合計金額取得
     */
    getGrandTotalPrice: (state: CashierState) => (mode: DISCOUNT_TYPES) => {
        let grandTotalPrice = null;

        switch (mode) {
            case DISCOUNT_TYPES.PRICE:
                // 値引額
                grandTotalPrice = state.sales.total_price - state.sales.discount_price;
                break;
            case DISCOUNT_TYPES.RATE:
                // 値引率
                grandTotalPrice = state.sales.total_price * (1 - state.sales.discount_rate / 100);
                break;
            default:
                // do nothing
                break;
        }

        return grandTotalPrice;
    },
    /**
     * 売上明細があるかどうか
     */
    hasItems: (state: CashierState) => {
        return state.sales.items.length > 0;
    },
};

export const actions = {
    /**
     * 売上登録
     * @param {any} context
     */
    save: async (context: any) => {
        return await axios.post(
            ROOT_URL,
            context.state.sales
        );
    }
};


export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions  
};