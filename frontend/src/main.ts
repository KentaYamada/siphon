import Vue from 'vue';
import Buefy from 'buefy';
import App from './App.vue';
import router from './router';
import store from '@/store';
// import axios, { AxiosResponse } from 'axios';
import './registerServiceWorker';
import 'buefy/dist/buefy.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/css/fontawesome.css';

Vue.config.productionTip = false;

// Buefy
Vue.use(Buefy, {
    defaultIconPack: 'fas',
});

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

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
