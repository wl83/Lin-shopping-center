<template>
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
</template>

<script>
export default {
  data () {
    return {
      searchQuery: {
        text: ''
      }
    }
  },
  methods: {
    handleSelect () {

    }
  }
}
</script>

<style lang="less" scoped>

</style>
