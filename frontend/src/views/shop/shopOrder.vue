<template>
  <div class="shop-order-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside class="shop-aside-container"></shopaside>
    </div>
    <div class="shop-order-table-container">
      <el-table
        :data="orderList"
        style="width: 100%"
        max-height="250">
        <el-table-column
          fixed
          prop="createdTime"
          label="下单日期"
          width="150">
        </el-table-column>
        <el-table-column
          prop="name"
          label="用户"
          width="100">
        </el-table-column>
        <el-table-column
          prop="phone"
          label="联系电话"
          width="140">
        </el-table-column>
        <el-table-column
          prop="paymentAmount"
          label="总价"
          width="120">
        </el-table-column>
        <el-table-column
          prop="status"
          label="订单状态"
          width="120">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址"
          width="300">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="120">
          <template slot-scope="scope">
            <el-button
              @click.native.prevent="deleteRow(scope.$index, orderList)"
              type="text"
              size="small">
              移除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import shopaside from '../../components/shopAside.vue'
export default {
  components: {
    navbar,
    shopaside
  },
  data () {
    return {
      orderList: [],
      orderIds: ''
    }
  },
  methods: {
    deleteRow (index, rows) {
      rows.splice(index, 1)
    }
  },
  mounted: function () {
    this.$http.get('shop/orders', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      this.orderIds = response.data.orders

      this.orderIds.forEach(orderId => {
        const order = {}

        this.$http.get('shop/orders/' + orderId, {
          headers: {
            Authorization: window.sessionStorage.getItem('shoptoken')
          }
        }).then(response => {
          order.createdTime = response.data.created_time
          order.paymentAmount = response.data.payment_amount
          order.name = response.data.address.receiver
          order.phone = response.data.address.phone
          order.address = response.data.address.address

          this.orderList.push(order)
        })
      })
    })
  }
}
</script>

<style lang="less" scoped>
  .shop-order-table-container{
    height: 100%;
    width: 84%;
    position: fixed;
    right: 0;
  }
</style>
