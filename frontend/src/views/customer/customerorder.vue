<template>
  <div class="all-orders-container">
    <header>
      <navbar></navbar>
    </header>

    <ordergrid :orderList="orderList"></ordergrid>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import ordergrid from '../../components/orderGrid.vue'
export default {
  components: {
    navbar,
    ordergrid
  },
  data () {
    return {
      orderList: []
    }
  },
  methods: {

  },
  mounted: function () {
    this.$http.get('customer/orders', {
      headers: {
        Authorization: window.sessionStorage.getItem('token')
      }
    }).then(response => {
      const orderIds = response.data.orders

      orderIds.forEach(orderId => {
        this.$http.get('customer/orders/' + orderId, {
          headers: {
            Authorization: window.sessionStorage.getItem('token')
          }
        }).then(response => {
          const item = {}
          item.status = response.data.status
          item.createdTime = response.data.created_time
          item.paymentTime = response.data.payment_time
          item.paymentAmount = response.data.payment_amount
          item.items = response.data.items
          item.orderId = orderId
          this.orderList.push(item)
        }).catch(err => err)
      })
    })
  }
}
</script>

<style lang="less" scoped>

</style>
