import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { DailySales, DailySalesSearchOption } from '@/entity/daily_sales';
import { DailySalesState } from '@/store/store_types';

const ROOT_URL = '/api/sales/daily';
const CANCEL_SALES_URL = '/api/sales/cancel';


const state: DailySalesState = {
    daily_sales: []
}

const mutations = {
    /**
     * 日次売上リストセット
     */
    setDailySales: (state: DailySalesState, dailySales: DailySales[]) => {
        state.daily_sales = dailySales;
    }
}

const getters = {
    /**
     * 日次売上リスト取得
     */
    getDailySales: (state: DailySalesState) => {
        return state.daily_sales;
    },
    /**
     * 日次売上があるかどうか
     */
    hasItems: (state: DailySalesState) => {
        return state.daily_sales.length > 0;
    }
}

const actions = {
    /**
     * 日次売上取得APIリクエスト
     */
    fetchDailySales: async (context: any, option: DailySalesSearchOption) => {
        return await axios
            .get(ROOT_URL, { params: option })
            .then((response: AxiosResponse) => {
                context.commit('setDailySales', response.data.daily_sales);
            });
    },
    /**
     * 売上取消APIリクエスト
     */
    cancelSales: async (context: any, salesId: number) => {
        const data = {
            sales_id: salesId
        };

        return await axios.post(CANCEL_SALES_URL, { params: data });
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
}
