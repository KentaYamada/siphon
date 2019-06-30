import Vue from 'vue';
import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { Category, CategorySerachOption } from '@/entity/category';
import { CategoryState } from '@/store/store_types';


const ROOT_URL = '/api/categories';

const state: CategoryState = {
    categories: [],
};

const mutations = {
    /**
     * 商品カテゴリリストセット
     */
    setCategories: (state: CategoryState, categories: Category[]) => {
        Vue.set(state, 'categories', [...categories]);
    }
}

const getters = {
    /**
     * 商品カテゴリリスト取得
     * @return List of categories
     */
    getCategories: (state: CategoryState) => {
        return state.categories;
    },
    getCategoryLength: (state: CategoryState) => {
        return state.categories.length;
    },
    /**
     * 商品カテゴリ検索 or 新規商品カテゴリ取得
     * @param id
     * @return Find or create category object
     */
    findOrCreate: (state: CategoryState) => (id?: number) => {
        let category = null;

        if (!_.isNull(id) && !_.isUndefined(id)) {
            category = _.find(state.categories, (category: Category) => {
                return category.id === id;
            });
            category = _.clone(category);
        } else {
            category = {
                id: null,
                name: '',
                items: null
            } as Category;
        }
        
        return category;
    },
    /**
     * 商品カテゴリリストがあるかどうか
     */
    hasItems: (state: CategoryState) => {
        return state.categories.length > 0;
    }
};

const actions = {
    /**
     * 商品カテゴリAPIリクエスト
     * @param context
     * @param option category search option
     * @return Axios promise object
     */
    fetchCategories: async (context: any, option: CategorySerachOption) => {
        return axios.get(ROOT_URL, {
                params: option
            })
            .then((response: AxiosResponse<any>) => {
                context.commit('setCategories', response.data.categories);
            });
    },
    /**
     * 商品カテゴリ登録
     * @param context
     * @param category
     * @return Axios promise object
     */
    save: async (context: any, category: Category) => {
        let promise$ = null;

        if (_.isNull(category.id)) {
            promise$ = axios.post(ROOT_URL, category);
        } else {
            const url = `${ROOT_URL}/${category.id}`;
            promise$ = axios.put(url, category);
        }

        return await promise$;
    },
    /**
     * 商品カテゴリ削除
     * @param context
     * @param id
     * @return Axios promise object
     */
    delete: async (context: any, id: number) => {
        const url = `${ROOT_URL}/${id}`;
        return await axios.delete(url);
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
};
