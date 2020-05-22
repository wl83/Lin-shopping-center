<template>
  <div class="address-container">
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

    <div class="address-grid-container">
      <div class="address-grid">
        <div class="address info">
          <p><span>收件人姓名：</span></p>
          <p><span>收件人手机号：</span></p>
          <p><span>详细地址：</span></p>
        </div>
        <div class="delete-address-btn-container">
          <el-button type="danger" class="delete-address-btn">删除</el-button>
        </div>
      </div>
    </div>

    <div class="address-grid-container">
      <div class="address-grid">
        <div class="address info">
          <p><span>收件人姓名：</span></p>
          <p><span>收件人手机号：</span></p>
          <p><span>详细地址：</span></p>
        </div>
        <div class="delete-address-btn-container">
          <el-button type="danger" class="delete-address-btn">删除</el-button>
        </div>
      </div>
    </div>

    <div class="add-address-btn-container">
      <el-button type="success" class="add-address-btn">新增地址</el-button>
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
.address-grid{
  width: 400px;
  height: 200px;
  border: 1px solid;
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  margin-top: 30px;
  padding-left: 10px;
  padding-top: 10px;
}
.delete-address-btn-container{
  width: 100px;
  height: 40px;
  position: relative;
  left: 50%;
  transform: translate(-50%);
}
.address-grid-container{
  width: 100%;
  height: 240px;
}
.delete-address-btn{
  width: 100px;
}
.add-address-btn-container{
  width: 100%;
  height: 40px;
  margin-top: 30px;
}
.add-address-btn{
  position: relative;
  left: 50%;
  transform: translate(-50%);
  width: 100px;

}
</style>
