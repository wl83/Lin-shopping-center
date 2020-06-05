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
          width="100"
          :filters="filters"
          :filter-method="filterTag"
          filter-placement="bottom-end">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.status === ('待付款' || '异常') ? 'danger' : scope.row.tag === ('已付款' || '配送中' || '已送达') ? 'primary' : 'success' "
              disable-transitions>{{ scope.row.status }}</el-tag>
          </template>
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
      orderIds: '',
      orderStatus: ['待付款', '已付款', '配送中', '已送达', '已签收', '异常'],
      filters: [
        { text: '待付款', value: '待付款' },
        { text: '已付款', value: '已付款' },
        { text: '配送中', value: '配送中' },
        { text: '已送达', value: '已送达' },
        { text: '已签收', value: '已签收' },
        { text: '异常', value: '异常' }
      ]
    }
  },
  methods: {
    deleteRow (index, rows) {
      rows.splice(index, 1)
    },
    filterTag (value, row) {
      return row.tag === value
    },
    filterHandler (value, row, column) {
      const property = column.property
      return row[property] === value
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
          order.status = this.orderStatus[response.data.status]

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
