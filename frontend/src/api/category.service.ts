import axios, { AxiosPromise } from 'axios';
import _ from 'lodash';
import Category from '@/entity/category';


const ROOT_URL = '/api/categories/';

/**
 * Get all categories api request
 */
export const fetchCategories = () => {
    return axios.get(ROOT_URL);
};

/**
 * Save or changes api request
 * @param {Category} category
 */
export const saveCategory = (category: Category): AxiosPromise<any> => {
    let promise$ = null;
    
    if (!_.isNull(category.id)) {
        const url = ROOT_URL + category.id;
        promise$ = axios.put(url, category);
    } else {
        promise$ = axios.post(ROOT_URL, category);
    }

    return promise$;
}

/**
 * Delete category api request
 * @param {number} id
 */
export const deleteCategory = (id: number): AxiosPromise<any> => {
    const url = ROOT_URL + id;
    return axios.delete(url);
};

export default {
    fetchCategories,
    saveCategory,
    deleteCategory
};
