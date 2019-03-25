import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { Category, CategorySerachOption } from '@/entity/category';
import { CategoryState } from '@/store/store_types';


const ROOT_URL = '/api/categories/';

const state: CategoryState = {
    categories: [],
};

const mutations = {
    setCategories: (state: CategoryState, categories: Category[]) => {
        state.categories = categories;
    }
}

const getters = {
    getCategories: (state: CategoryState) => {
        return state.categories;
    },
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
    hasItems: (state: CategoryState) => {
        return state.categories.length > 0;
    }
};

const actions = {
    /**
     * 商品カテゴリ一覧取得
     * @param { any } context
     * @param { CategorySerachOption } option
     * @return { AxiosResponse }
     */
    fetchCategories: async (context: any, option: CategorySerachOption) => {
        return axios.get(ROOT_URL).then((response: AxiosResponse<any>) => {
            context.commit('setCategories', response.data.categories);
        });
    },
    /**
     * 商品カテゴリ登録
     * @param { any } context
     * @param { Category } category
     * @return { AxiosResponse }
     */
    save: async (context: any, category: Category) => {
        let promise$ = null;

        if (_.isNull(category.id)) {
            promise$ = axios.post(ROOT_URL, category);
        } else {
            const url = ROOT_URL + category.id;
            promise$ = axios.put(url, category);
        }

        return await promise$;
    },
    /**
     * 商品カテゴリ削除
     * @param { any } context
     * @param { number } id
     * @return { AxiosResponse }
     */
    delete: async (context: any, id: number) => {
        const url = ROOT_URL + id;
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
