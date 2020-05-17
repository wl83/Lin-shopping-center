<template>
  <div class="login-container">
    <header>
      <div class="nav-bar">
        <div class="login-logo">
          <a href=""><span>Lin-Shopping</span></a>
        </div>
        <div class="search-query">
          <el-input placeholder="请输入内容" class="search-query-input" clearable prefix-icon="el-icon-search"></el-input>
        </div>
        <div class="nav-menu">
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">首页</el-menu-item>
            <el-menu-item index="2">购物</el-menu-item>
            <el-menu-item index="3">购物车</el-menu-item>
            <el-menu-item index="4">个人中心</el-menu-item>
          </el-menu>
        </div>
      </div>
    </header>

    <div class="login-grid">
      <div class="login-title">
        <h1><span>用户登录</span></h1>
      </div>
      <div class="login-form">
        <el-form>
          <el-form-item>
            <el-input class="form-item-input" placeholder="请输入手机号码" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item>
            <el-input class="form-item-input" placeholder="请输入密码" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <el-form-item>
            <div class="form-item-link" id="form-item-link-top">
              <el-link icon="el-icon-goods">商店登录</el-link>
            </div>
            <div class="form-item-btn">
              <el-button type="primary">登录</el-button>
            </div>
            <div class="form-item-link" id="form-item-link-bottom">
              <el-link icon="el-icon-edit">立即注册</el-link>
            </div>
          </el-form-item>
        </el-form>
      </div>
      <div class="login-btn-link">

      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
  header{
    width: 100%;
    height: 60px;
    border: 1px solid rgb(214, 214, 214);
  }
  .login-logo{
    width: 200px;
    float: left;
    padding-top: 15px;
    margin-left: 100px;
  }
  .search-query{
    width: 300px;
    float: left;
    padding-top: 10px;
  }
  .nav-menu{
    width: 400px;
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
    margin-left: 200px;
  }
  .login-grid{
    height: 400px;
    width: 50%;
    border: 1px solid;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  .login-title{
    width: 100%;
  }
  .login-title h1{
    text-align: center;
  }
  .form-item-input{
    width: 60%;
    margin-left: 140px;
    margin-top: 30px;
  }
  #form-item-link-top{
    float: left;
  }
  #form-item-link-bottom{
    float: right;
  }
  .form-item-button{
    float: left;
  }

</style>
