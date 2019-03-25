import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import {
    User,
    UserSearchOption
} from '@/entity/user';
import { UserState } from '@/store/store_types';

const ROOT_URL = '/api/users/';

const state: UserState = {
    users: []
};

const mutations = {
    setUsers: (state: UserState, users: User[]) => {
        state.users = users;
    }
}

const getters = {
    getUsers: (state: UserState) => {
        return state.users;
    },
    findOrCreate: (state: UserState) => (id?: number) => {
        let user = null;

        if (!_.isNull(id) && !_.isUndefined(id)) {
            user = _.find(state.users, (user: User) => {
                return user.id === id;
            });
        } else {
            user = {
                id: null,
                name: '',
                nickname: '',
                email: '',
                password: ""
            } as User;
        }

        return user;
    },
    hasItems: (state: UserState) => {
        return state.users.length > 0;
    }
}

const actions = {
    fetchUsers: async (context: any, option: UserSearchOption) => {
        return await axios.get(ROOT_URL).then((response: AxiosResponse<any>) => {
            context.commit('setUsers', response.data.users);
        });
    },
    save : async (context: any, user: User) => {
        let promise$ = null;

        if (_.isNull(user.id)) {
            promise$ = axios.post(ROOT_URL, user);
        } else {
            const url = ROOT_URL + user.id;
            promise$ = axios.put(url, user);
        }

        return await promise$;
    },
    delete: async (context: any, id: number) => {
        const url = ROOT_URL + id;
        return await axios.delete(url);
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
};
