import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import UserLogin from '../components/UserLogin.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/user/login',
    component: UserLogin
  }
]

const router = new VueRouter({
  routes
})

export default router
