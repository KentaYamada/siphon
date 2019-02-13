import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from '@/components/login/Login.vue';
import Top from '@/components/top/Top.vue';
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
  ],
});
