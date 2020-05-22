<template>
  <div class="cart-submit-container">
    <header>
      <div class="nav-bar">
        <div class="login-logo">
          <a href=""><span>Lin-Shopping</span></a>
        </div>
        <div class="search-query">
          <el-input placeholder="请输入内容" class="search-query-input" v-model="searchQuery.text" clearable prefix-icon="el-icon-search"></el-input>
        </div>
        <div class="nav-menu">
          <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <!-- :default-active="activeIndex" -->
            <el-menu-item index="1">首页</el-menu-item>
            <el-menu-item index="2">购物</el-menu-item>
            <el-menu-item index="3">购物车</el-menu-item>
            <el-menu-item index="4">个人中心</el-menu-item>
          </el-menu>
        </div>
      </div>
    </header>

    <div class="address-container">
      <div class="address-grid">
        <div class="address-info">

        </div>
        <div class="address-select-btn">
          <el-button class="address-select" @click="drawer=true" type="primary" style="margin-left: 16px;">
            选择地址
          </el-button>
        </div>
      </div>
    </div>
    <el-drawer
      title="我是标题"
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose">
      <span>我来啦!</span>
    </el-drawer>

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

    <div class="cart-submit-order">
      <div class="cart-total-price">

      </div>
      <div class="cart-submit-btn">
        <el-button type="success" class="cart-submit">结算</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      searchQuery: {
        text: ''
      },
      drawer: false,
      direction: 'rtl',
      num: 1,
      methods: {
        handleSelect () {

        },
        handleClose (done) {
          this.$confirm('确认关闭？')
            .then(_ => {
              done()
            })
            .catch(_ => {})
        }
      }
    }
  }
}
</script>

<style lang="less" scoped>
.address-container{
  width: 100%;
  height: 200px;
  border: 1px solid;
}
.address-grid{
  width: 50%;
  height: 200px;
  border: 1px solid;
  left: 50%;
  transform: translate(-50%);
  position: relative;
}
.address-info{
  width: 80%;
  height: 130px;
  border: 1px solid;
  left: 50%;
  top: 5%;
  transform: translate(-50%);
  position: relative;
}
.address-select-btn{
  width: 80%;
  height: 50px;
  border: 1px solid;
  left: 50%;
  top: 5%;
  transform: translate(-50%);
  position: relative;
}
.address-select{
  left: 50%;
  top: 10%;
  transform: translate(-50%);
  position: relative;
}
.cart-item-grid{
  width: 50%;
  height: 200px;
  border: 1px solid;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 10px;
}
.cart-submit-order{
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
