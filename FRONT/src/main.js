import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// 부트스트랩 추가
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueCarousel from 'vue-carousel';
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueCarousel);
// 여기까지

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
