import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './css/global.css'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$http = axios
axios.defaults.baseURL = 'http://127.0.0.1:3000'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
