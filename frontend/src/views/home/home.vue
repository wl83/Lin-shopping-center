<template>
  <div class="home-container">
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

    <div class="home-grid">
      <div class="left-arrow">
        <el-button class="left-arrow-icon" icon="el-icon-arrow-left"></el-button>
      </div>
      <div class="scroll-pict">
        <div class="item-grid">
          <div class="item-image-grid">
            <el-image
              :src="url"
              class="item-image"
              :fit="cover"></el-image>
          </div>
          <div class="item-price">
            <el-link type="info" icon="el-icon-s-goods" class="shop-link">进入店铺</el-link>
            <p><span class="price">¥100</span></p>
            <p><span class="stock">销量：100</span></p>
          </div>
          <div class="in-cart">
            <el-button type="primary" class="in-cart-btn">加入购物车</el-button>
          </div>
        </div>
        <div class="item-grid">

        </div>
        <div class="item-grid">

        </div>
      </div>
      <div class="right-arrow">
        <el-button class="right-arrow-icon" icon="el-icon-arrow-right"></el-button>
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
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
    }
  },
  methods: {
    handleSelect () {

    }
  }
}
</script>

<style lang="less" scoped>
.left-arrow{
  position: absolute;
  left: 20px;
  height: 100%;
  width: 50px;
}
.left-arrow-icon{
  position: absolute;
  top: 50%;
  height: 50px;
  border-color: rgb(158, 158, 158);
}
.right-arrow{
  position: absolute;
  height: 100%;
  width: 50px;
  right: 20px;
}
.right-arrow-icon{
  border-color: rgb(158, 158, 158);
  position: absolute;
  top: 50%;
  height: 50px;
}
.scroll-pict{
  width: 1200px;
  height: 100%;
  position: absolute;
  left: 50%;
  transform: translate(-50%);
}

</style>
