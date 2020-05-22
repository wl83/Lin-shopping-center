<template>
  <div class="all-reviews-container">
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

    <div class="review-grid">
      <div class="review-remark-container">

      </div>
      <div class="review-star-container">
        <el-rate
          class="review-star"
          v-model="value"
          disabled
          show-score
          text-color="#ff9900"
          score-template="{value}">
        </el-rate>
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
      value: 0,
      methods: {
        handleSelect () {

        }
      }
    }
  }
}
</script>

<style lang="less" scoped>
.review-grid{
  width: 50%;
  height: 120px;
  border: 1px solid;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 10px;
}
.review-remark-container{
  width: 100%;
  height: 80px;
  border: 1px solid;
}
.review-star-container{
  width: 100%;
  height: 38px;
  border: 1px solid;
}
.review-star{
  left: 5%;
  top: 50%;
  position: relative;
  transform: translate(0, -50%);
}
</style>
