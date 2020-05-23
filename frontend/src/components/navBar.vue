<template>
  <div class="nav-bar">
    <div class="login-logo">
      <a href="/#/"><span>Lin-Shopping</span></a>
    </div>
    <div class="search-query">
      <el-input placeholder="请输入内容" class="search-query-input" v-model="searchQuery.text" clearable prefix-icon="el-icon-search"></el-input>
    </div>
    <div class="nav-menu">
      <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect">
         <!-- :default-active="activeIndex" -->
        <el-menu-item index="1">首页</el-menu-item>
        <el-menu-item index="2">购物车</el-menu-item>
        <el-menu-item index="3">个人中心</el-menu-item>
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
    handleSelect (index) {
      switch (index) {
        case '1': {
          this.$router.push('/')
          break
        }
        case '2': {
          break
        }
        case '3': {
          this.$router.push('customer')
          break
        }
      }
    }
  }
}
</script>

<style lang="less" scoped>

</style>
