<template>
<div class="shop-center-container">
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

  <div class="shop-info">
    <div class="shop-image-container">

    </div>
    <div class="shop-info-container">
      <div class="shop-info-name">
        <h1><span>华中科技大学华为旗舰店</span></h1>
      </div>
      <div class="shop-info-intro">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi ducimus magnam architecto doloremque obcaecati omnis. Molestiae deserunt veniam, obcaecati fuga eum fugit accusantium. Esse cumque voluptas nisi molestias asperiores. Facilis.</p>
      </div>
      <div class="shop-info-star">
        <p>评价等级：</p>
      </div>
      <div class="add-item-container">
        <el-button class="add-item-btn" type="success">添加商品</el-button>
      </div>
    </div>
  </div>
  <div class="shop-item-list">
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
.shop-info{
  width: 100%;
  height: 400px;
  border: 1px solid;
  padding: 10px 10px 10px 10px;
}
.shop-image-container{
  width: 350px;
  height: 390px;
  border: 1px solid;
  margin-left: 50px;
  float: left;
}
.shop-info-container{
  width: 850px;
  height: 390px;
  border: 1px solid;
  float: left;
  margin-left: 70px;
  padding-left: 20px;
}
.shop-info-name{
  border: 1px solid;
}
.shop-info-intro{
  border: 1px solid;
  height: 200px;
}
.shop-info-star{
  border: 1px solid;
  height: 90px;
  width: 50%;
  float: left;
}
.shop-item-list{
  width: 100%;
  height: 800px;
  border: 1px solid;
  margin-top: 30px;
}
.add-item-container{
  width: 49%;
  height: 90px;
  float: left;
  border: 1px solid;
}
.add-item-btn{
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  position: relative;
  width: 120px;
}
</style>
