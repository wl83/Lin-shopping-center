<template>
  <div class="cart-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="cart-item-grid">
      <div class="item-image-container">

      </div>
      <div class="item-info-container">
        <div class="item-name">

        </div>
        <div class="item-info">

        </div>
        <div class="item-price-container">

        </div>
        <div class="item-number-more">
          <div class="item-number-container">
            <el-input-number size="small" class="item-number" v-model="num" :min='0' @change="handleChange" label="选择数量"></el-input-number>
          </div>
          <div class="item-more-info">
            <el-link class="item-link"><i class="el-icon-view el-icon--right"></i>查看详情</el-link>
          </div>
        </div>
      </div>
    </div>
    <div class="cart-submit-container">
      <div class="cart-total-price">

      </div>
      <div class="cart-submit-btn">
        <el-button type="danger" class="cart-submit">结算</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
export default {
  components: {
    navbar
  },
  data () {
    return {
      num: 1,
      methods: {
        handleChange () {
        }
      }
    }
  }
}
</script>

<style lang="less" scoped>

.cart-submit-container{
  width: 100%;
  height: 70px;
  position: absolute;
  bottom: 0;
  border: 1px solid;
}
.cart-total-price{
  width: 50%;
  height: 70px;
  border: 1px solid;
  float: left;
}
.cart-submit-btn{
  width: 49%;
  height: 70px;
  border: 1px solid;
  float: left;
}
.cart-submit{
  width: 150px;
  position: relative;
  left: 10%;
  top: 50%;
  transform: translate(0,-50%);
}
</style>
