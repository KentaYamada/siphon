import Vue from 'vue';
import Vuex from 'vuex';
import category from '@/store/category';
import item from '@/store/item';
import user from '@/store/user';
import cashier from '@/store/cashier';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    category,
    item,
    user,
    cashier,
  }
});
