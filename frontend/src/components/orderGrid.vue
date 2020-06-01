<template>
  <div class="customer-order-wrapper">
      <div class="order-item" v-for="(order, index) in orderList" :key="index">
        <div class="order-id-container">
          <div class="order-id-title">
            <i class="el-icon-document"></i>
            <span>订单号: {{ order.orderId }}</span>
          </div>
          <div class="order-status-container">
            <span>{{ getStatusText(order.status) }}</span>
          </div>
        </div>
        <el-divider class="divider"></el-divider>
        <div class="order-info-container">
          <div class="order-price-container">
            <span>总价: {{ order.paymentAmount }}</span>
          </div>
          <div class="order-created-time">
            <span>创建时间: {{ order.createdTime }}</span>
          </div>
          <div class="order-payed-time">
            <span>付款时间: {{ order.paymentTime }}</span>
          </div>
        </div>
        <el-divider class="divider"></el-divider>
        <div class="order-more-container">
          <el-button @click="onDetailclicked(order)" class="order-more" type="primary" plain>查看详情</el-button>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  props: ['orderList'],
  methods: {
    onDetailclicked (order) {
      this.$router.push({
        name: 'orderDetail',
        params: {
          orderId: order.orderId
        }
      })
    },
    getStatusText (status) {
      // 订单状态显示
      switch (status) {
        case 0:
          return '待付款'
        case 1:
          return '已付款'
        case 2:
          return '配送中'
        case 3:
          return '已到达'
        case 4:
          return '已收货'
        case 5:
          return '异常'
      }
    }
  }
}
</script>

<style lang="less" scoped>
.order-item{
    width: 60%;
    height: 235px;
    border: 1px solid rgb(146, 146, 146);
    left: 50%;
    transform: translate(-50%);
    position: relative;
    margin-top: 10px;
    padding: 10px 10px 10px 10px;
  }
  .order-id-container{
    width: 100%;
    height: 40px;
  }
  .order-status-container{
    float: left;
    width: 10%;
    height: 70%;
    top: 50%;
    transform: translate(0, -30%);
    position: relative;
  }
  .order-status-container span{
    color: rgb(228, 0, 0);
  }
  .order-id-title{
    width: 85%;
    height: 70%;
    top: 50%;
    transform: translate(0, -30%);
    position: relative;
    float: left;
  }
  .order-info-container{
    width: 100%;
    height: 110px;
  }
  .order-more-container{
    width: 100%;
    height: 45px;
  }
  .order-more{
    left: 50%;
    top: 5%;
    transform: translate(-50%);
    position: relative;
  }
  .order-price-container{
    width: 100%;
    height: 33%;
  }
  .order-created-time{
    width: 100%;
    height: 33%;
  }
  .order-payed-time{
    width: 100%;
    height: 33%;
  }
  .divider{
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>
