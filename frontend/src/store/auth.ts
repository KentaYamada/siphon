import axios from 'axios';
import { Authrication } from '@/entity/auth';
import { AuthState } from '@/store/store_types';


const ROOT_URL = '/api/auth';


const state: AuthState = {
    auth: {
        email: '',
        password: ''
    } as Authrication
};

const mutations = {
    /**
     * 認証情報初期化
     */
    initialize: (state: AuthState) => {
        state.auth = {
            email: '',
            password: ''
        } as Authrication;
    }
};

const getters = {
    /**
     * 認証情報取得
     */
    getAuth: (state: AuthState) => {
        return state.auth;
    }
};

const actions = {
    /**
     * ログインAPIリクエスト
     */
    login: async (context: any) => {
        return await axios.post(ROOT_URL, context.state.auth);
    },
    /**
     * ログアウトAPIリクエスト
     */
    logout: async (context: any) => {
        context.commit('initialize');
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
};