<template>
  <div class="shop-order-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside :shopId="shopId" class="shop-aside-container"></shopaside>
    </div>
    <div class="shop-order-table-container">
      <el-table
        class="shop-order-table"
        :data="orderList"
        style="width: 100%">
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
              :type="scope.row.status === ('待付款' || '异常') ? 'danger' : scope.row.status === ('已付款' || '配送中' || '已送达') ? 'primary' : 'success' "
              disable-transitions>{{ scope.row.status }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址"
          width="330">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="120">
          <template slot-scope="scope">
            <el-button
              @click.native.prevent="handleOrderStatus(scope.$index)"
              type="text"
              size="small">
              处理
            </el-button>
            <el-button
              @click.native.prevent="handleOrderDetail(scope.$index)"
              type="text"
              size="small">
              查看
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog
      title="更新订单状态"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose">
      <el-dropdown @command="handleCommand">
        <span class="el-dropdown-link">
          {{ orderStatus[orderStat] }}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="a">待付款</el-dropdown-item>
          <el-dropdown-item command="b">已付款</el-dropdown-item>
          <el-dropdown-item command="c">配送中</el-dropdown-item>
          <el-dropdown-item command="d">已送达</el-dropdown-item>
          <el-dropdown-item command="e">异常</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateOrderStatus">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog title="收货地址" :visible.sync="dialogTableVisible1">
      <el-table :data="orderDetailTable">
        <el-table-column property="name" label="商品名" width="150"></el-table-column>
        <el-table-column property="itemId" label="商品ID" width="100"></el-table-column>
        <el-table-column property="currentPrice" label="现价" width="150"></el-table-column>
        <el-table-column property="amount" label="数量" width="100"></el-table-column>
        <el-table-column property="inStock" label="库存"></el-table-column>
      </el-table>
    </el-dialog>

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
      dialogVisible: false,
      dialogTableVisible1: false,
      orders: [],
      orderDetailTable: [],
      orderStat: '',
      orderClicked: '',
      shopId: '',
      itemIds: [],
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
    updateOrderStatus () {
      this.$confirm('确定更新订单状态?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$http.put('shop/orders/' + this.orderClicked, {
          status: this.orderStat
        },
        {
          headers: {
            Authorization: window.sessionStorage.getItem('shoptoken')
          }
        }).then(() => {
          this.$message.success('更新成功')
          this.dialogVisible = false
        }).catch(err => {
          console.log(err)
        })
      })
    },
    handleOrderStatus (index) {
      this.dialogVisible = true
      this.orderClicked = this.orderList[index].orderId
    },
    handleOrderDetail (index) {
      this.orderDetailTable = []
      this.items = this.orderList[index].items
      this.items.forEach(item => {
        this.$http.get('items/' + item.item_id, {})
          .then(response => {
            const orderItemTemp = {}
            orderItemTemp.name = response.data.name
            orderItemTemp.itemId = item.item_id
            orderItemTemp.currentPrice = response.data.current_price
            orderItemTemp.inStock = response.data.in_stock
            orderItemTemp.amount = item.amount

            this.orderDetailTable.push(orderItemTemp)
          })
          .catch(err => {
            console.log(err)
          })
      })
      this.dialogTableVisible1 = true
    },
    handleClose (done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    handleCommand (command) {
      switch (command) {
        case 'a': {
          this.orderStat = 0
          break
        }
        case 'b': {
          this.orderStat = 1
          break
        }
        case 'c': {
          this.orderStat = 2
          break
        }
        case 'd': {
          this.orderStat = 3
          break
        }
        case 'e': {
          this.orderStat = 5
          break
        }
      }
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
    this.shopId = this.$route.params.shopId

    this.$http.get('shop/orders', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      this.orders = response.data.orders

      this.orders.forEach(order => {
        const orderTemp = {}

        this.$http.get('shop/orders/' + order.order_id, {
          headers: {
            Authorization: window.sessionStorage.getItem('shoptoken')
          }
        }).then(response => {
          orderTemp.orderId = order.order_id
          orderTemp.createdTime = response.data.created_time
          orderTemp.paymentAmount = order.price
          orderTemp.name = response.data.address.receiver
          orderTemp.phone = response.data.address.phone
          orderTemp.address = response.data.address.address
          orderTemp.status = this.orderStatus[response.data.status]
          orderTemp.items = order.items

          this.orderList.push(orderTemp)
        })
      })
    })
  }
}
</script>

<style lang="less" scoped>
  .shop-order-wrapper{
    width: 100%;
    height: 700px;
  }
  .shop-order-table-container{
    height: 100%;
    width: 84%;
    position: absolute;
    right: 0;
  }
  .shop-order-table{
    width: 100%;
    height: 100%;
    position: relative;
  }
</style>
