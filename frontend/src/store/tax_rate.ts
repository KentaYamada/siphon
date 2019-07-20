import axios, { AxiosResponse } from 'axios';
import _ from 'lodash';
import moment from 'moment';
import { TaxRate, TAX_TYPES } from '@/entity/tax_rate';
import { TaxRateState } from '@/store/store_types';


const ROOT_URL = '/api/tax_rates';

const state: TaxRateState = {
    tax_rate: {
        rate: 0,
        reduced_rate: 0,
        start_date: moment().toDate(),
        tax_type: TAX_TYPES.INCLUDE
    } as TaxRate,
};

const mutations = {
    setTaxRate: (state: TaxRateState, taxRate: TaxRate) => {
        if (_.isNull(taxRate)) {
            state.tax_rate = {
                rate: 0,
                reduced_rate: 0,
                start_date: moment().toDate(),
                tax_type: TAX_TYPES.INCLUDE
            } as TaxRate;
        } else {
            state.tax_rate = taxRate;
        }
    }
};

const actions = {
    fetchTaxRate: async (context: any) => {
        return axios.get(ROOT_URL).then((response: AxiosResponse) => {
            context.commit('setTaxRate', response.data.tax_rate);
        });
    },
    save: async (context: any) => {
        const taxRate: TaxRate = context.state.tax_rate;
        return await axios.post(ROOT_URL, taxRate);
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    actions
};
