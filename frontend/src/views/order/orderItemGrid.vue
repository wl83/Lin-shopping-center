<template>
  <div class="cart-submit-wrapper">
    <div class="cart-item-grid" v-for="(orderItem, index) in orderList" :key="index">
      <div class="cart-item-image-container">
        <el-image
          class="cart-item-image"
          :src="'data:image;base64,' + orderItem.images[0]"
          :fit="fit"></el-image>
      </div>
      <div class="cart-item-info-container">
        <div class="cart-order-item-name-container">
          <span class="cart-order-item-name">{{ orderItem.name }}</span>
        </div>
        <div class="cart-order-item-info-container">
          <p class="cart-order-item-info">{{ orderItem.info }}</p>
        </div>
        <div class="cart-order-item-price-container">
          <span class="cart-order-item-price">¥{{ orderItem.currentPrice }}</span>
        </div>
      </div>
      <div class="cart-order-item-number-container">
        <span class="cart-order-item-number">x{{ orderItem.count }}</span>
      </div>
      <div class="cart-order-review-container">
         <el-button @click="onRviewClicked(orderItem)" type="success" plain>评价</el-button>
      </div>
    </div>
    <div style="height: 100px;"></div>
  </div>
</template>

<script>
export default {
  props: ['orderList'],
  data () {
    return {
      fit: 'contain'
    }
  },
  methods: {
    onRviewClicked (orderItem) {
      this.$router.push({
        name: 'review',
        params: { itemId: orderItem.itemId }
      })
    }
  }
}
</script>

<style lang="less" scoped>
.cart-item-grid{
  width: 50%;
  height: 230px;
  border: 1px solid rgb(153, 153, 153);
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 10px;
  padding-left: 10px;
  padding-top: 10px;
}
.cart-item-image-container{
  width: 25%;
  height: 80%;
  float: left;
}
.cart-item-info-container{
  width: 65%;
  height: 80%;
  float: left;
  margin-left: 10px;
}
.cart-item-image{
  width: 100%;
  height: 100%;
}
.cart-order-item-name-container{
  width: 100%;
  height: 25%;
}
.cart-order-item-info-container{
  width: 100%;
  height: 40%;
  overflow: hidden;
}
.cart-order-item-price-container{
  width: 100%;
  height: 30%;
}
.cart-order-item-number-container{
  width: 5%;
  height: 80%;
  float: left;
}
.cart-order-item-name{
  font-size: 20px;
}
.cart-order-item-info{
  color: rgb(160, 160, 160);
}
.cart-order-item-price{
  font-size: 25px;
  color: rgb(219, 1, 1);
}
.cart-order-item-number{
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.cart-order-review-container{
  float: right;
  right: 2%;
  position: relative;
}
</style>
