<template>
  <div class="login-container">
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
            <!-- :default-active="activeIndex"   -->
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
        <el-form ref="customerLoginFormRef" :model="customerLoginForm" :rules="customerLoginFormRules">
          <el-form-item class="form-item" prop="username">
            <el-input v-model="customerLoginForm.username" class="form-item-input" placeholder="请输入手机号码" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item class="form-item" prop="password">
            <el-input v-model="customerLoginForm.password" class="form-item-input" id="form-item-input-password" placeholder="请输入密码" type="password" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <div style="height: 40px;"></div>
          <el-form-item>
            <div class="form-item-link" id="form-item-link-top">
              <el-link class="form-item-link-top" icon="el-icon-goods">商店登录</el-link>
            </div>
            <div class="form-item-btn">
              <el-button class="login-btn" type="primary" @click="userLogin">登录</el-button>
            </div>
            <div class="form-item-link">
              <el-link class="form-item-link-bottom" icon="el-icon-edit">立即注册</el-link>
            </div>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript" src="./bower_components/mockjs/dist/mock.js"></script>
<script>
export default {
  data () {
    return {
      customerLoginForm: {
        username: '',
        password: ''
      },
      searchQuery: {
        text: ''
      },
      customerLoginFormRules: {
        username: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 16, message: '长度在6到16之间', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    userLogin () {
      this.$refs.customerLoginFormRef.validate(async valid => {
        if (!valid) {
          return
        }
        const { data: res } = await this.$http.post('login', this.customerLoginForm)

        console.log(res)

        if (res.meta.status !== 200) {
          return this.$message.error('登录失败!')
        } else {
          // 登录成功后的操作
          this.$message.success('登录成功!')
          window.sessionStorage.setItem('token', res.data.token)
          this.$router.push('/')
        }
      })
    },
    handleSelect () {

    }
  }
}
</script>

<style lang="less" scoped>
  .login-grid{
    height: 400px;
    width: 40%;
    border: 1px solid rgb(195, 195, 195);
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
  .login-form{
    width: 100%;
    padding: 0px 40px;
    box-sizing: border-box;
  }
  .form-item-input{
    margin-top: 30px;
  }
  .form-item-link-top{
    float: left;
    position: absolute;
    left: 15%;
  }
  .form-item-link-bottom{
    float: left;
    position: absolute;
    left: 70%;
  }
  .login-btn{
    width: 100px;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
  }

</style>
