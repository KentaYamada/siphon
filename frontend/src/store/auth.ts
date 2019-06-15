import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { Authrication } from '@/entity/auth';
import { AuthState } from '@/store/store_types';


const ROOT_URL = '/api/auth';
const LOGIN_URL = `${ROOT_URL}/login`;
const LOGOUT_URL = `${ROOT_URL}/logout`;
const REFLESH_TOKEN_URL = `${ROOT_URL}/reflesh`;

const state: AuthState = {
    auth: {
        //user_id: null,
        email: '',
        password: '',
    } as Authrication,
    is_logged_in: false,
    auth_token: '',
};

const mutations = {
    /**
     * 認証情報初期化
     */
    initialize: (state: AuthState): void => {
        state.auth = {
            email: '',
            password: '',
        } as Authrication;
        state.is_logged_in = false;
        state.auth_token = ''
    },
    /**
     * 認証情報を保持
     */
    setAccessToken: (state: AuthState, accessToken: string): void => {
        state.auth_token = accessToken;
        state.is_logged_in = true;
    }
};

const getters = {
    /**
     * Get current auth info.
     * 
     * @param state
     * @returns auth entity
     */
    getAuth: (state: AuthState): Authrication => {
        return state.auth;
    },
    /**
     * ログインしているかどうか
     */
    isLoggedIn: (state: AuthState): boolean => {
        return state.is_logged_in;
    }
};

const actions = {
    /**
     * Request auth
     */
    login: async (context: any) => {
        return await axios.post(ROOT_URL, context.state.auth)
            .then((res: AxiosResponse) => {
                axios.defaults.headers.common['Authoricate'] = `Bearer ${res.data.auth_token}`;
                context.commit('setAccessToken', res.data.auth_token);
                return Promise.resolve(res);
            });
    },
    /**
     * Request logout
     */
    logout: async (context: any) => {
        const data = {
            auth_token: <AuthState>context.state.auth_token
        };

        context.commit('initialize');

        return await axios.post(LOGOUT_URL, data);
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
};