import Vue from 'vue';
import Buefy from 'buefy';
import _ from 'lodash';
// import axios, { AxiosResponse } from 'axios';
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
}).$mount('#app');

// todo: module化
/*axios.interceptors.response.use((config: AxiosResponse) => {
  return config;
}, (error: any) => {
    const response = error.response;

    if (response && response.status === 400 && response.data.is_retry) {
      // request reflesh access token
      const data = {'auth_token': ''};
      axios.post('/api/auth/reflesh', data)
          .then(() => {
              // retry original request
              axios.request(error.config);
          });
    }

    return Promise.reject(error);
});*/
