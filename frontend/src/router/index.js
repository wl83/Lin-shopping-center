import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home/home.vue'
import UserLogin from '../components/UserLogin.vue'
import UserRegister from '../components/UserRegister.vue'
import Item from '../views/item/item.vue'
import Customer from '../views/customer/customer.vue'
import Shop from '../views/shop/shop.vue'
import Address from '../views/customer/address.vue'
import AddAddress from '../views/customer/addaddress.vue'
import Cart from '../views/customer/cart.vue'
import CartSubmit from '../views/customer/cartsubmit.vue'
import CustomerOrder from '../views/customer/customerorder.vue'

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
  },
  {
    path: '/item/:item_id',
    component: Item
  },
  {
    path: '/customer',
    component: Customer
  },
  {
    path: '/shop/:shop_id',
    component: Shop
  },
  {
    path: '/customer/address',
    component: Address
  },
  {
    path: '/customer/address/add',
    component: AddAddress
  },
  {
    path: '/customer/cart',
    component: Cart
  },
  {
    path: '/customer/cart/submit',
    component: CartSubmit
  },
  {
    path: '/customer/orders',
    component: CustomerOrder
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  var nextPath = ['/customer/login', '/customer/register', '/home', '/', '/item']
  for (var i = 0; i < nextPath.length; i++) {
    if (to.path === nextPath[i]) {
      return next()
    } else if (to.path.substr(0, 5) === '/item') {
      return next()
    }
  }

  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/customer/login')
  next()
})

export default router
