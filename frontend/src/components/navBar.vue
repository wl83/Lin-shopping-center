<template>
  <header>
  <div class="nav-bar">
    <div class="login-logo">
      <a href="/#/"><span>Lin-Shopping</span></a>
    </div>
    <div class="search-query">
      <el-input @keydown.enter.native="handleSearch" placeholder="请输入内容" class="search-query-input" v-model="searchQuery.text" clearable prefix-icon="el-icon-search"></el-input>
      <el-button @click="handleSearch" class="search-btn" slot="append" icon="el-icon-search"></el-button>
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
  </header>
</template>

<script>
export default {
  props: {
    transmitData: {
      searchFn: Function,
      rankTypeN: Number,
      groupIndexN: Number
    }
  },
  data () {
    return {
      searchQuery: {
        text: ''
      },
      items: []
    }
  },
  methods: {
    handleSelect (index) {
      switch (index) {
        case '1': {
          this.$router.replace('/')
          break
        }
        case '2': {
          this.$router.replace('/customer/cart')
          break
        }
        case '3': {
          this.$router.replace('/customer')
          break
        }
      }
    },
    handleSearch () {
      if (this.$route.path === '/search') {
        this.$parent.search(this.searchQuery.text, this.rankTypeN, this.groupIndexN)
        this.$emit('childFn', this.items)
      } else {
        this.$router.replace({ path: '/search', query: { itemName: this.searchQuery.text } })
      }
      // this.$router.go(0)
    }
  }
}
</script>

<style lang="less" scoped>
header{
    width: 100%;
    height: 60px;
    border: 1px solid rgb(212, 212, 212);
  }
  .login-logo{
    width: 200px;
    float: left;
    padding-top: 15px;
    margin-left: 100px;
  }
  .search-query{
    width: 650px;
    height: 60px;
    float: left;
    padding-top: 10px;
  }
  .nav-menu{
    width: 300px;
    float: right;
  }
  .login-logo a{
    text-align: center;
    text-decoration: none;
    margin-top: 20px;
  }
  .login-logo span{
    color: #409EFF;
    font-size: 20px;
  }
  .search-query-input{
    width: 300px;
    margin-left: 250px;
    float: left;
  }
  .search-btn{
    float: left;
  }
</style>
