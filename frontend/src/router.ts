import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/login/Login.vue';
import Top from '@/components/top/Top.vue';
import Cashier from '@/components/cashier/Cashier.vue';
import DailySales from '@/components/sales/daily/DailySales.vue';
import CategoryList from '@/components/category/list/CategoryList.vue';
import ItemList from '@/components/item/list/ItemList.vue';
import TaxEdit from '@/components/tax_rate/TaxRate.vue';
import UserList from '@/components/user/list/UserList.vue';
import store from '@/store';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'top',
      component: Top,
      meta: {
          requireAuth: true
      }
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
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/items',
      name: 'itemList',
      component: ItemList,
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/users',
      name: 'userList',
      component: UserList,
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/cashier',
      name: 'cashier',
      component: Cashier,
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/sales/daily',
      name: 'dailySales',
      component: DailySales,
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/tax',
      name: 'tax',
      component: TaxEdit,
      meta: {
        requireAuth: true
      }
    },
  ],
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireAuth)) {
        if (store.getters['auth/isLoggedIn'] === false) {
          next('/login');
        } else {
          next();
        }
    } else {
      next();
    }
});

export default router;