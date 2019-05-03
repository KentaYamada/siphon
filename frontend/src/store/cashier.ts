import Vue from 'vue';
import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { Sales, DISCOUNT_TYPES } from '@/entity/sales';
import SalesItem from '@/entity/sales_item';
import { Item } from '@/entity/item';
import { CashierState } from '@/store/store_types';
import { Category } from '@/entity/category';
import category from './category';


const ROOT_URL = '/api/cashier/';

const state: CashierState = {
    sales: {
        total_price: 0,
        discount_price: 0,
        discount_rate: 0,
        deposit: 0,
        items: []
    } as Sales,
    categories: [],
    items: []
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
            deposit: 0,
            items: []
        } as Sales;
    },
    /**
     * 商品カテゴリセット
     */
    initCategories: (state: CashierState, categories: Category[]) => {
        state.categories = categories;
    },
    /**
     * 商品データセット
     */
    setItems: (state: CashierState, categoryId?: number) => {
        const category = _.find(state.categories, (category: Category) => {
            return category.id === categoryId;
        });
        const items = _.isUndefined(category) ? [] : category.items;

        Vue.set(state, 'items', items);
    },
    /**
     * 商品追加
     * 
     * @param {CashierState} state
     * @param {Item} selectedItem
     */
    addItem: (state: CashierState, selectedItem: Item) =>{
        const index = _.findIndex(state.sales.items, (item: SalesItem) => {
            return selectedItem.name === item.item_name;
        });

        if (index > -1) {
            state.sales.items[index].quantity += 1;

            const quantity = state.sales.items[index].quantity;
            const price = state.sales.items[index].unit_price;
            state.sales.items[index].subtotal = quantity * price;
        } else {
            const salesItem: SalesItem = {
                item_name: selectedItem.name,
                unit_price: selectedItem.unit_price,
                quantity: 1,
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
     * 
     * @param {CashierState} state
     * @param {string} itemName
     */
    reduceItem: (state: CashierState, itemName: string) => {
        const index = _.findIndex(state.sales.items, (item: SalesItem) => {
            return itemName === item.item_name;
        });

        if (index > -1) {
            let item = state.sales.items[index];

            if (item.quantity > 1) {
                item.quantity -= 1;
                const quantity = state.sales.items[index].quantity;
                const price = state.sales.items[index].unit_price;
                state.sales.items[index].subtotal = quantity * price;
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
     * 
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
    /**
     * 商品選択データ取得
     */
    getSelectionItems: (state: CashierState) => {
        return state.items;
    },
    /**
     * 商品カテゴリ選択データ取得
     */
    getSelectionPanelData: (state: CashierState) => {
        // 2 x 5の二次元配列にする
        const row = 2;
        const col = 5;
        let categories = [];
        let offset = 0;

        for (let i = 0; i< row; i++) {
            categories.push(_.slice(state.categories, offset, col+offset));
            offset += col;
        }

        return categories;
    }
};

export const actions = {
    /**
     * 商品選択で使うデータ取得
     */
    fetchSelectionItems: async (context: any) => {
        return await axios.get(ROOT_URL)
            .then((response: AxiosResponse<any>) => {
                const categories = response.data.categories as Category[];
                context.commit('initCategories', categories);

                if (categories.length > 0) {
                    context.commit('setItems', categories[0].id);
                }
            });
    },
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
