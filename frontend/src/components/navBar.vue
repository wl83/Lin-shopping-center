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

</style>
