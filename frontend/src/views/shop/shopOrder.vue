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
      orderIds: '',
      orderStat: '',
      orderClicked: '',
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
          order.orderId = orderId
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
