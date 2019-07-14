import Vue from 'vue';
import Buefy from 'buefy';
import _ from 'lodash';
import axios, { AxiosResponse, AxiosError } from 'axios';
import App from './App.vue';
import router from './router';
import filters from './filters';
import store from '@/store';
import './registerServiceWorker';
import 'buefy/dist/buefy.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/css/fontawesome.css';

Vue.config.productionTip = false;

// Import Buefy
Vue.use(Buefy, {
    defaultIconPack: 'fas',
});

// Register filters
_.forEach(filters, (filter: Function, key: string) => {
  Vue.filter(key, filter);
});

new Vue({
  router,
  store,
  render: (h) => h(App),
  created: () => {
    if (store.getters['auth/isLoggedIn']) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${store.getters['auth/getAuthToken']}`;
    }
  }
}).$mount('#app');



axios.interceptors.response.use((config: AxiosResponse) => {
  return config;
}, (error: AxiosError) => {
    const response = error.response;

    if (response && response.status === 401) {
        if (response.data.refleshing) {
          // request reflesh token
          const token = axios.defaults.headers.common.Authorization.split(' ')[1];
          const data = {
            token: token
          };
          axios.post('/api/auth/reflesh', data).then((res: AxiosResponse) => {
              // retry original request
              const retryRequest = error.config;
              retryRequest.headers.Authorization = `Bearer ${res.data.auth_token}`;
              axios.request(retryRequest);
          });
        } else {
          // toast??
          store.commit('auth/initialize');
          router.push('/login');
        }
    }

    return Promise.reject(error);
});
