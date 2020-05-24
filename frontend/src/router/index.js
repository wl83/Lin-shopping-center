import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home/home.vue'
import UserLogin from '../components/UserLogin.vue'
import ShopLogin from '../components/ShopLogin.vue'
import UserRegister from '../components/UserRegister.vue'
import Item from '../views/item/item.vue'
import Customer from '../views/customer/customer.vue'
import Shop from '../views/shop/shop.vue'
import Address from '../views/customer/address.vue'
import AddAddress from '../views/customer/addaddress.vue'
import Cart from '../views/customer/cart.vue'
import CartSubmit from '../views/customer/cartsubmit.vue'
import CustomerOrder from '../views/customer/customerorder.vue'
import CustomerReview from '../views/customer/customerreview.vue'
import Search from '../views/home/search.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/customer/login',
    name: 'customerLogin',
    component: UserLogin
  },
  {
    path: '/shop/login',
    name: 'shopLogin',
    component: ShopLogin
  },
  {
    path: '/customer/register',
    name: 'customerRegister',
    component: UserRegister
  },
  {
    path: '/item',
    name: 'item',
    component: Item
  },
  {
    path: '/customer',
    name: 'customer',
    component: Customer
  },
  {
    path: '/shop',
    name: 'shop',
    component: Shop
  },
  {
    path: '/customer/address',
    name: 'customerAddress',
    component: Address
  },
  {
    path: '/customer/address/add',
    name: 'customerAddressAdd',
    component: AddAddress
  },
  {
    path: '/customer/cart',
    name: 'customerCart',
    component: Cart
  },
  {
    path: '/customer/cart/submit',
    name: 'customerCartSubmit',
    component: CartSubmit
  },
  {
    path: '/customer/orders',
    name: 'customerOrders',
    component: CustomerOrder
  },
  {
    path: '/customer/reviews',
    name: 'customerReviews',
    component: CustomerReview
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  }
]

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  var nextPath = ['/customer/login', '/customer/register', '/home', '/', '/item', '/shop/login', '/shop/register']
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
