<template>
  <div class="customer-center-container">
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

    <div class="customer-info-container">
      <div class="customer-image-container">

      </div>
      <div class="customer-intro-container">

      </div>
    </div>

    <div class="customer-manage-container">
      <div class="customer-manage-grid">

      </div>
      <div class="customer-manage-grid">

      </div>
      <div class="customer-manage-grid">

      </div>
      <div class="customer-manage-grid">

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
      methods: {
        handleSelect () {

        }
      }
    }
  }
}
</script>

<style lang="less" scoped>
.customer-info-container{
  width: 100%;
  height: 400px;
  border: 1px solid;
  margin-top: 20px;
  padding: 20px 20px 20px 20px;
}
.customer-manage-container{
  width: 100%;
  height: 300px;
  border: 1px solid;
  margin-top: 30px;
  margin-bottom: 30px;
}
.customer-image-container{
  width: 30%;
  height: 350px;
  border: 1px solid;
  top: 5%;
  left: 3%;
  position: relative;
  float: left;
}
.customer-intro-container{
  width: 60%;
  height: 350px;
  border: 1px solid;
  top: 5%;
  left: 5%;
  position: relative;
  float: left;
}
.customer-manage-grid{
  width: 100px;
  height: 100px;
  border: 1px solid;
  float: left;
  position: relative;
  left: 25%;
  top: 50%;
  transform: translate(-50%, -50%);
  margin-right: 100px;
}
</style>
