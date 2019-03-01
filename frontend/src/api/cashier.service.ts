import axios, { AxiosPromise } from 'axios';
import Sales from '@/entity/sales';


const ROOT_URL = '/api/cashier/';

/**
 * Save sales api request
 * @param {Sales} sales
 * @returns {AxiosPromise}
 */
export const createSales = (sales: Sales): AxiosPromise<any> => {
    return axios.post(ROOT_URL, sales);
};

export default {
    createSales
};
