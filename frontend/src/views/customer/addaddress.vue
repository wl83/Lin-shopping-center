<template>
  <div class="add-address-container">
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

    <div class="add-address-grid">
      <div class="add-address-title">
        <h1><span>新增地址</span></h1>
      </div>
      <div class="add-address-form">
        <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign">
          <el-form-item label="收件人姓名">
            <el-input v-model="formLabelAlign.name" placeholder="请输入收件人姓名" prefix-icon="el-icon-user-solid"></el-input>
          </el-form-item>
          <el-form-item label="收件人手机号">
            <el-input v-model="formLabelAlign.phone" placeholder="请输入收件人手机号" prefix-icon="el-icon-phone"></el-input>
          </el-form-item>
          <el-form-item label="详细地址">
            <el-input v-model="formLabelAlign.address" placeholder="请输入详细地址" prefix-icon="el-icon-location"></el-input>
          </el-form-item>
        </el-form>
      </div>
      <div class="add-address-btn-container">
        <el-button type="success" class="add-address-btn">新增地址</el-button>
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
      labelPosition: 'top',
      formLabelAlign: {
        name: '',
        phone: '',
        address: ''
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
.add-address-grid{
  width: 50%;
  height: 600px;
  border: 1px solid;
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  margin-top: 50px;
}
.add-address-title{
  width: 100%;
  height: 100px;
}
.add-address-title h1{
  text-align: center;
}
.add-address-form{
  padding-left: 40px;
  padding-right: 40px;
}
.add-address-btn-container{
  margin-top: 60px;
}
.add-address-btn{
  position: relative;
  left: 50%;
  transform: translate(-50%);
}
</style>
