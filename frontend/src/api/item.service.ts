import axios, { AxiosPromise } from 'axios';
import { Item, ItemSearchOption } from '@/entity/item';
import _ from 'lodash';

const ROOT_URL = '/api/items/'

/**
 * Get items by category id
 * @param {number} categoryId
 */
export const fetchItems = (searchOption: ItemSearchOption): AxiosPromise<any> => {
    const url = ROOT_URL;
    return axios.get(url);
};

/**
 * Save or changes api request
 * @param {Item} item
 */
export const saveItem = (item: Item): AxiosPromise<any> => {
    let promise$ = null;

    if (!_.isNull(item.id)) {
        const url = ROOT_URL + item.id;
        promise$ = axios.put(url, item);
    } else {
        promise$ = axios.post(ROOT_URL, item);
    }
    
    return promise$;
};

/**
 * Delete item api request
 * @param {number} id
 */
export const deleteItem = (id: number): AxiosPromise<any> => {
    const url = ROOT_URL + id;
    return axios.delete(url);
};

export default {
    fetchItems,
    saveItem,
    deleteItem
};
