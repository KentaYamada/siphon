import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/login/Login.vue';
import Top from '@/components/top/Top.vue';
import Cashier from '@/components/cashier/Cashier.vue';
import DailySales from '@/components/sales/daily/DailySales.vue';
import CategoryList from '@/components/category/list/CategoryList.vue';
import ItemList from '@/components/item/list/ItemList.vue';
import UserList from '@/components/user/list/UserList.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'top',
      component: Top,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/categories',
      name: 'categoryList',
      component: CategoryList,
    },
    {
      path: '/items',
      name: 'itemList',
      component: ItemList,
    },
    {
      path: '/users',
      name: 'userList',
      component: UserList,
    },
    {
      path: '/cashier',
      name: 'cashier',
      component: Cashier,
    },
    {
      path: '/sales/daily',
      name: 'dailySales',
      component: DailySales,
    },
  ],
});
