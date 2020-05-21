import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home/home.vue'
import UserLogin from '../components/UserLogin.vue'
import UserRegister from '../components/UserRegister.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/customer/login',
    component: UserLogin
  },
  {
    path: '/customer/register',
    component: UserRegister
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  var nextPath = ['/customer/login', '/customer/register', '/home', '/']
  for (var i = 0; i < nextPath.length; i++) {
    if (to.path === nextPath[i]) {
      return next()
    }
  }

  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/customer/login')
  next()
})

export default router
