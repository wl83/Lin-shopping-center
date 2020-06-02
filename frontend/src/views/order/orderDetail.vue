<template>
  <div class="order-detail-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="order-detail-address-container">
      <div class="order-detail-address-info-container">
        <div class="order-detail-address-name-container">
          <span>{{ address.name }}</span>
        </div>
        <div class="order-detail-address-phone-container">
          <span>{{ address.tel }}</span>
        </div>
        <div class="order-detail-address-address-container">
          <span>{{ address.address }}</span>
        </div>
      </div>
    </div>

    <orderitemgrid :orderList="orderItems"></orderitemgrid>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import orderitemgrid from './orderItemGrid.vue'
export default {
  components: {
    navbar,
    orderitemgrid
  },
  data () {
    return {
      orderId: '',
      address: {},
      orderItems: []
    }
  },
  computed: {
    /* 计算商品总价 */
    totalPrice () {
      return this.orderItems.reduce(
        (total, item) => total + item.current_price * item.count,
        0
      )
    }
  },
  mounted: function () {
    this.orderId = this.$route.params.orderId // 获取订单ID

    this.$http.get('customer/orders/' + this.orderId, {
      headers: {
        Authorization: window.sessionStorage.getItem('token')
      }
    }).then(response => {
      const items = response.data.items

      items.forEach(item => {
        const orderItem = {}
        orderItem.itemId = item.item_id
        orderItem.count = item.count
        orderItem.reviewId = item.review_id
        const addressId = response.data.address_id

        // 获取地址信息
        this.$http.get('address/' + addressId, {
          headers: {
            Authorization: window.sessionStorage.getItem('token')
          }
        }).then(response => {
          this.address = {
            id: addressId,
            name: response.data.receiver,
            tel: response.data.phone,
            address: response.data.address
          }
        }).catch(err => {
          console.log(err)
        })

        // 获取商品信息
        this.$http.get('items/' + item.item_id, {})
          .then(response => {
            orderItem.name = response.data.name
            orderItem.currentPrice = response.data.current_price
            orderItem.info = response.data.info
            orderItem.shopId = response.data.shop_id
            orderItem.images = response.data.images
            this.orderItems.push(orderItem)
          })
          .catch(err => {
            console.log(err)
          })
      })
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less" scoped>
.order-detail-wrapper{
  width: 100%;
  height: 700px;
}
.order-detail-address-container{
  width: 100%;
  height: 18%;
  border: 1px solid rgb(143, 143, 143);
}
.order-detail-address-info-container{
  width: 50%;
  height: 100%;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  border: 1px solid rgb(155, 155, 155);
  border-top: 0px;
  border-bottom: 0px;
  padding-left: 10px;
  padding-right: 10px;
}
.order-detail-address-name-container{
  width: 100%;
  height: 25%;
}
.order-detail-address-name-container span{
  font-size: 20px;
}
.order-detail-address-phone-container{
  width: 100%;
  height: 25%;
}
.order-detail-address-phone-container span{
  color: rgb(221, 0, 0);
}
.order-detail-address-address-container{
  width: 100%;
  height: 45%;
}
.order-detail-address-address-container span{
  color: rgb(98, 98, 98);
}
.order-detail-total-price-container{
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 10%;
  border: 1px solid;
}
.order-detail-total-price{
  width: 25%;
  height: 100%;
  right: 0;
  position: fixed;
  border: 1px solid;
}
</style>
