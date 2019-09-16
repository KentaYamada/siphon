import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { Sales, DISCOUNT_TYPES } from '@/entity/sales';
import { SalesItem, TargetItem } from '@/entity/sales_item';
import { Category } from '@/entity/category';
import { TAX_OPTIONS } from '@/entity/tax_rate';
import { CashierState } from '@/store/store_types';
import { Item } from '@/entity/item';


const ROOT_URL = '/api/cashier/';

/**
 * 該当する売上明細データのインデックス取得
 * @param salesItems 
 * @param targetItem 
 */
const findSalesItemIndex = (salesItems: SalesItem[], targetItem: TargetItem): number => {
    return _.findIndex(salesItems, (salesItem: SalesItem) => {
        return (salesItem.name == targetItem.item.name) &&
            (salesItem.tax_option === targetItem.tax_option);
    });
};

/**
 * 小計計算
 * @param state 
 */
const calcTotalPrice = (salesItems: SalesItem[]): number  => {
    return _.sumBy(salesItems, (item: SalesItem) => {
        return item.subtotal;
    });
};

const state: CashierState = {
    sales: {
        total_price: 0,
        discount_price: 0,
        discount_rate: 0,
        normal_tax_price: 0,
        reduced_tax_price: 0,
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
            normal_tax_price: 0,
            reduced_tax_price: 0,
            deposit: 0,
            items: []
        } as Sales;
    },
    /**
     * 売上明細追加
     */
    addSalesItem: (state: CashierState, targetItem: TargetItem): void => {
        const index = findSalesItemIndex(state.sales.items, targetItem);

        if (index > -1) {
            const salesItem = state.sales.items[index];
            salesItem.quantity += 1;
            salesItem.subtotal = salesItem.quantity * salesItem.unit_price;
        } else {
            const salesItem = {
                name: targetItem.item.name,
                unit_price: targetItem.item.unit_price,
                quantity: 1,
                subtotal: targetItem.item.unit_price,
                tax_option: targetItem.tax_option,
            } as SalesItem;
            state.sales.items.push(salesItem);
        }

        state.sales.total_price = calcTotalPrice(state.sales.items);
    },
    /**
     * 売上明細削除
     */
    deleteSalesItem: (state: CashierState, targetItem: TargetItem): void => {
        const index = findSalesItemIndex(state.sales.items, targetItem);
        state.sales.items.splice(index, 1);
        state.sales.total_price = calcTotalPrice(state.sales.items);
    },
    /**
     * 明細の商品点数を増やす
     */
    increaseSalesItem: (state: CashierState, targetItem: TargetItem): void => {
        const index = findSalesItemIndex(state.sales.items, targetItem);

        if (index <= -1) {
            return;
        }

        const salesItem = state.sales.items[index] as SalesItem;
        salesItem.quantity += 1;
        salesItem.subtotal = salesItem.quantity * salesItem.unit_price;
        state.sales.total_price = calcTotalPrice(state.sales.items);
    },
    /**
     * 明細の商品点数を減らす
     */
    decreaseSalesItem: (state: CashierState, targetItem: TargetItem): void => {
        const index = findSalesItemIndex(state.sales.items, targetItem);

        if (index <= -1) {
            return;
        }

        const salesItem = state.sales.items[index] as SalesItem;

        if (salesItem.quantity > 1) {
            salesItem.quantity -= 1;
            salesItem.subtotal = salesItem.quantity * salesItem.unit_price;
        } else {
            state.sales.items.splice(index, 1);
        }

        state.sales.total_price = calcTotalPrice(state.sales.items);
    },
    /**
     * 預かり金額更新
     */
    setDeposit: (state: CashierState, deposit: number): void => {
        state.sales.deposit = deposit;
    },
    /**
     * 値引額更新
     */
    setDiscountPrice: (state: CashierState, discountPrice: number): void => {
        state.sales.discount_price = discountPrice;
    },
    /**
     * 値引率更新
     */
    setDiscountRate: (state: CashierState, discountRate: number): void => {
        state.sales.discount_rate = discountRate;
    },
    /**
     * 商品選択で使用するカテゴリデータセット
     */
    setCategories: (state: CashierState, categories: Category[]): void => {
        state.categories = categories;
    },
    /**
     * 商品選択で使用する商品データセット
     */
    setItems: (state: CashierState, categryId: number): void => {
        const category = _.find(state.categories, (category: Category) => {
            return category.id === categryId;
        });
        state.items = _.isUndefined(category) ? [] : <Item[]>category.items;
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
    },
};

const getters = {
    /**
     * 売上総合計金額取得
     */
    grandTotalPrice: (state: CashierState) => (mode: DISCOUNT_TYPES): number | null => {
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
     * おつり取得
     */
    charge: (state: CashierState): number => {
        const charge = state.sales.deposit - state.sales.total_price;
        return  charge > 0 ? charge : 0;
    },
    /**
     * 売上明細データがあるかどうか
     */
    hasSalesItems: (state: CashierState): boolean => {
        return state.sales.items.length > 0;
    },
    /**
     * 通常税率の売上明細取得
     */
    normalTaxSalesItems: (state: CashierState): SalesItem[] => {
        return _.filter(state.sales.items, (item: SalesItem) => {
            return item.tax_option === TAX_OPTIONS.NORMAL;
        });
    },
    /**
     * 軽減税率の売上明細取得
     */
    reducedTaxSalesItems: (state: CashierState): SalesItem[] => {
        return _.filter(state.sales.items, (item: SalesItem) => {
            return item.tax_option === TAX_OPTIONS.REDUCED;
        });
    },
    /**
     * 通常税率の売上明細があるかどうか
     */
    hasNormalTaxSalesItems: (state: CashierState): boolean => {
        const items = _.filter(state.sales.items, (item: SalesItem) => {
            return item.tax_option === TAX_OPTIONS.NORMAL;
        });

        return items.length > 0;
    },
    /**
     * 軽減税率の売上明細があるかどうか
     */
    hasReducedTaxSalesItems: (state: CashierState): boolean => {
        const items = _.filter(state.sales.items, (item: SalesItem) => {
            return item.tax_option === TAX_OPTIONS.REDUCED;
        });

        return items.length > 0;
    },
    /**
     * 選択可能な商品取得
     */
    currentItems: (state: CashierState): Item[] => {
        return state.items;
    },
    /**
     * 選択可能な商品があるかどうか
     */
    hasItems: (state: CashierState): boolean => {
        return state.items.length > 0;
    },
};

const actions = {
    /**
     * 商品選択で使うデータ取得
     */
    fetchSelectionItems: async (context: any) => {
        return await axios.get(ROOT_URL).then((response: AxiosResponse<any>) => {
            const categories = response.data.categories as Category[];
            context.commit('setCategories', categories);

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
        return await axios.post(ROOT_URL, context.state.sales);
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions  
};
