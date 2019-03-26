import _ from 'lodash';
import moment from 'moment';
import axios, { AxiosResponse } from 'axios';
import {
    MonthlySales,
    PopularItem,
    DashboardSearchOption
} from '@/entity/dashboard';
import { DashboardState } from '@/store/store_types';


const ROOT_URL = '/api/dashboard';

const state: DashboardState = {
    monthly_sales: [],
    popular_items: []
};

const mutations = {
    /**
     * 月間売上データセット
     */
    setMonthlySales: (state: DashboardState, monthlySales: MonthlySales[]) => {
        state.monthly_sales = monthlySales;
    },
    /**
     * 月間人気商品リストセット
     */
    setPopularItems: (state: DashboardState, popularItems: PopularItem[]) => {
        state.popular_items = popularItems;
    }
};

const getters = {
    /**
     * 月間売上データ取得
     */
    getMonthlySales: (state: DashboardState) => {
        return state.monthly_sales;
    },
    /**
     * 月間人気商品リスト取得
     */
    getPopularItems: (state: DashboardState) => {
        return state.popular_items;
    },
    /**
     * 月間売上リストがあるかどうか
     */
    hasMonthlySales: (state: DashboardState) => {
        return state.monthly_sales.length > 0;
    },
    /**
     * 月間人気商品リストがあるかどうか
     */
    hasPopularItems: (state: DashboardState) => {
        return state.popular_items.length > 0;
    }
};

const actions = {
    /**
     * ダッシュボードデータ取得APIリクエスト
     */
    fetchDashboardData: async (context: any, option: DashboardSearchOption) => {
        const momentDate = moment(option.target);
        const year = momentDate.year();
        const month = momentDate.month();
        const url = `${ROOT_URL}/${year}/${month}`;

        return await axios.get(url).then((response: AxiosResponse<any>) => {
            context.commit('setMonthlySales', response.data.monthly_sales);
            context.commit('setPopularItems', response.data.popular_items);
        });
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
};