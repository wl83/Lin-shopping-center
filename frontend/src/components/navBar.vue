<template>
  <header>
  <div class="nav-bar">
    <div class="login-logo">
      <a href="/#/"><span>Lin-Shopping</span></a>
    </div>
    <div class="search-query">
      <el-input @keydown.enter.native="handleSearch" placeholder="请输入内容" class="search-query-input" v-model="searchQuery.text" clearable prefix-icon="el-icon-search"></el-input>
      <el-button @click="handleSearch" class="search-btn" slot="append" icon="el-icon-search"></el-button>
      <el-dropdown class="rank-brn" @command="handleCommand">
        <el-button>
          <i class="el-icon-setting"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="a">
            <i class="el-icon-check" v-if="rank==1"></i>
            按价格从大到小
          </el-dropdown-item>
          <el-dropdown-item command="b">
            <i class="el-icon-check" v-if="rank==2"></i>
            按价格从小到大
          </el-dropdown-item>
          <el-dropdown-item command="c">
            <i class="el-icon-check" v-if="rank==3"></i>
            按评价从大到小
          </el-dropdown-item>
          <el-dropdown-item command="d">
            <i class="el-icon-check" v-if="rank==4"></i>
            按评价从小到大
          </el-dropdown-item>
          <el-dropdown-item command="e">
            <i class="el-icon-check" v-if="rank==5"></i>
            按销量从大到小
          </el-dropdown-item>
          <el-dropdown-item command="f">
            <i class="el-icon-check" v-if="rank==6"></i>
            按销量从小到大
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
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
      items: [],
      rank: 5
    }
  },
  methods: {
    handleCommand (command) {
      switch (command) {
        case 'a': {
          this.rank = 1
          break
        }
        case 'b': {
          this.rank = 2
          break
        }
        case 'c': {
          this.rank = 3
          break
        }
        case 'd': {
          this.rank = 4
          break
        }
        case 'e': {
          this.rank = 5
          break
        }
        case 'f': {
          this.rank = 6
          break
        }
      }
    },
    handleSelect (index) {
      const tokenStr1 = window.sessionStorage.getItem('token')
      const tokenStr2 = window.sessionStorage.getItem('shoptoken')
      switch (index) {
        case '1': {
          this.$router.replace('/')
          break
        }
        case '2': {
          if (tokenStr1) {
            this.$router.replace('/customer/cart')
          } else if (!tokenStr1 && tokenStr2) {
            this.$message.warning('请登录顾客账号')
          } else if (!tokenStr1 && !tokenStr2) {
            this.$router.push('/customer/login')
          }
          break
        }
        case '3': {
          if (!tokenStr1 && !tokenStr2) {
            this.$router.replace('/customer/login')
          } else if (!tokenStr1 && tokenStr2) {
            this.$router.replace('/shop')
          } else {
            this.$router.replace('/customer')
          }
          break
        }
      }
    },
    handleSearch () {
      if (this.$route.path.substr(0, 7) === '/search') {
        this.items = []
        this.$parent.search(this.searchQuery.text, this.rank, this.groupIndexN)
        this.$emit('childFn', { items: this.items, rank: this.rank })
      } else {
        this.$router.push({ name: 'search', query: { itemName: this.searchQuery.text, rank: this.rank } })
      }
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
    width: 420px;
    height: 60px;
    float: left;
    padding-top: 10px;
    /* border: 1px solid; */
    position: relative;
    left: 46%;
    top: 50%;
    transform: translate(-100%);
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
    float: left;
  }
  .search-btn{
    float: left;
  }
  .rank-brn{
    float: left;
  }
</style>
