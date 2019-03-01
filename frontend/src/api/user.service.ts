import axios, { AxiosPromise } from 'axios';
import _ from 'lodash';
import { User, UserSearchOption } from '@/entity/user';


const ROOT_URL = '/api/users/';

/**
 * Get users api request
 * @param {any} searchOption
 * @returns {AxiosPromise}
 */
export const fetchUsers = (searchOption: UserSearchOption): AxiosPromise<any> => {
    return axios.get(ROOT_URL);
};

/**
 * Save or changes api request
 * @param {User} user
 * @returns {AxiosPromise}
 */
export const saveUser = (user: User): AxiosPromise<any> => {
    let promise$ = null;

    if (!_.isNull(user.id)) {
        const url = ROOT_URL + user.id;
        promise$ = axios.put(url, user);
    } else {
        promise$ = axios.post(ROOT_URL, user);
    }
    
    return promise$;
};

/**
 * Delete user api request
 * @param {number} id
 * @returns {AxiosPromise}
 */
export const deleteUser = (id: number | null): AxiosPromise<any> => {
    const url = `${ROOT_URL}/${id}`;
    return axios.delete(url);
};

export default {
    fetchUsers,
    saveUser,
    deleteUser
};
