import Vue from 'vue';
import Buefy from 'buefy';
import App from './App.vue';
import router from './router';
import store from './store';
import VueLodash from 'vue-lodash';
import './registerServiceWorker';
import 'buefy/dist/buefy.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/css/fontawesome.css';

Vue.config.productionTip = false;

// Buefy
Vue.use(Buefy, {
    defaultIconPack: 'fas',
});

// lodash
Vue.use(VueLodash);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
