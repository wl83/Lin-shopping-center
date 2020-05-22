import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './css/global.css'
import './css/navbar.css'
import './css/itemgrid.css'
import './css/cartitem.css'
import './css/ordergrid.css'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$http = axios
axios.defaults.baseURL = 'https://www.liulongbin.top:8888/api/private/v1/'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
