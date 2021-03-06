import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home/home.vue'
import UserLogin from '../components/UserLogin.vue'
import ShopLogin from '../components/ShopLogin.vue'
import ShopRegister from '../components/ShopRegister.vue'
import UserRegister from '../components/UserRegister.vue'
import Item from '../views/item/item.vue'
import Customer from '../views/customer/customer.vue'
import Shop from '../views/shop/shop.vue'
import Address from '../views/customer/address.vue'
import AddAddress from '../views/customer/addAddress.vue'
import Cart from '../views/customer/cart.vue'
import CartSubmit from '../views/customer/cartSubmit.vue'
import CustomerOrder from '../views/customer/customerOrder.vue'
import CustomerReview from '../views/customer/customerReview.vue'
import OrderDetail from '../views/order/orderDetail.vue'
import Search from '../views/home/search.vue'
import Review from '../views/review/review.vue'
import ShopManage from '../views/shop/shopManage.vue'
import ShopOrder from '../views/shop/shopOrder.vue'
import ShopItem from '../views/shop/shopItem.vue'
import AddItem from '../views/item/addItem.vue'
import ShopReview from '../views/shop/shopReview.vue'
import ShopReport from '../views/shop/shopReport.vue'
import ShopIndex from '../views/shop/shopIndex.vue'

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
    path: '/shop/register',
    name: 'shopRegister',
    component: ShopRegister
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
    path: '/customer/orders/:orderId',
    name: 'orderDetail',
    component: OrderDetail
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
  },
  {
    path: '/customer/orders/:orderId/review/:itemId',
    name: 'review',
    component: Review
  },
  {
    path: '/shop/management',
    name: 'shopManage',
    component: ShopManage
  },
  {
    path: '/shop/orders',
    name: 'shopOrders',
    component: ShopOrder
  },
  {
    path: '/shop/reviews',
    name: 'shopReviews',
    component: ShopReview
  },
  {
    path: '/shop/items',
    name: 'shopItems',
    component: ShopItem
  },
  {
    path: '/shop/items/addNewItem',
    name: 'addNewItem',
    component: AddItem
  },
  {
    path: '/shop/report',
    name: 'shopReport',
    component: ShopReport
  },
  {
    path: '/shop/index',
    name: 'shopIndex',
    component: ShopIndex
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

  const tokenStr1 = window.sessionStorage.getItem('token')
  const tokenStr2 = window.sessionStorage.getItem('shoptoken')
  if (!tokenStr1 && !tokenStr2) {
    return next('/customer/login')
  }
  next()
})

export default router
