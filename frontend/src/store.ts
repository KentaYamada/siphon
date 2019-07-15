import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import category from '@/store/category';
import item from '@/store/item';
import user from '@/store/user';
import cashier from '@/store/cashier';
import dashboard from '@/store/dashboard';
import auth from '@/store/auth';
import daily_sales from '@/store/daily_sales';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    category,
    item,
    user,
    cashier,
    dashboard,
    auth,
    daily_sales
  },
  plugins: [
      createPersistedState(),
  ]
});
