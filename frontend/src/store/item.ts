import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { Item, ItemSearchOption } from '@/entity/item';


const ROOT_URL = '/api/items/';

interface ItemState {
    items: Item[];
}

const state: ItemState = {
    items: []
};

const mutations = {
    setItems: (state: ItemState, items: Item[]) => {
        state.items = items;
    }
};

const getters = {
    getItems: (state: ItemState) => {
        return state.items; 
    },
    findOrCreate: (state: ItemState) => (id?: number) => {
        let item = null;

        if (!_.isNull(id) && !_.isUndefined(id)) {
            item = _.find(state.items, (item: Item) => {
                return item.id === id;
            });
            item = _.clone(item);
        } else {
            item = {
                id: null,
                category_id: null,
                name: '',
                unit_price: null
            } as Item;
        }

        return item;
    },
    hasItems: (state: ItemState) => {
        return state.items.length > 0;
    }
};

const actions = {
    fetchItems: async (context: any, option: ItemSearchOption ) => {
        return await axios.get(ROOT_URL)
            .then((response: AxiosResponse<any>) => {
                context.commit('setItems', response.data.items);
            });
    },
    save: async (context: any, item: Item) => {
        let promise$ = null;

        if (_.isNull(item.id)) {
            promise$ = axios.post(ROOT_URL, item);
        } else {
            const url = ROOT_URL + item.id;
            promise$ = axios.put(url, item);
        }

        return await promise$;
    },
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
}
