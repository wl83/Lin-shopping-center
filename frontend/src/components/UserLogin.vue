<template>
  <div class="login-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="login-grid">
      <div class="login-title">
        <h1><span>用户登录</span></h1>
      </div>
      <div class="login-form">
        <el-form ref="customerLoginFormRef" :model="customerLoginForm" :rules="customerLoginFormRules">
          <el-form-item class="form-item" prop="phone">
            <el-input v-model="customerLoginForm.phone" class="form-item-input" placeholder="请输入手机号码" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item class="form-item" prop="password">
            <el-input v-model="customerLoginForm.password" class="form-item-input" id="form-item-input-password" placeholder="请输入密码" type="password" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <div style="height: 40px;"></div>
          <el-form-item>
            <div class="form-item-link" id="form-item-link-top">
              <el-link href="/#/shop/login" class="form-item-link-top" icon="el-icon-goods">商店登录</el-link>
            </div>
            <div class="form-item-btn">
              <el-button class="login-btn" type="primary" @click="userLogin">登录</el-button>
            </div>
            <div class="form-item-link">
              <el-link href="/#/customer/register" class="form-item-link-bottom" icon="el-icon-edit">立即注册</el-link>
            </div>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript" src="./bower_components/mockjs/dist/mock.js"></script>
<script>
import navbar from './navBar.vue'
export default {
  components: {
    navbar
  },
  data () {
    return {
      customerLoginForm: {
        phone: '',
        password: ''
      },
      customerLoginFormRules: {
        phone: [
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
        if (!this.isMobileNumber(this.customerLoginForm.phone)) {
          return this.$message.error('手机号格式错误!')
        }
        await this.$http.get('customer/login', {
          params: {
            phone: this.customerLoginForm.phone,
            password: this.customerLoginForm.password
          }
        }).then(response => {
           // 登录成功后的操作
          this.$message.success('登录成功!')
          window.sessionStorage.setItem('token', response.data.token)
          this.$router.push('/')
        }).catch(err => {
          return this.$message.error('登录失败!')
        })
      })
    },
    isMobileNumber (phone) {
      var flag = false
      var myreg = /^(((13[0-9]{1})|(14[0-9]{1})|(17[0-9]{1})|(15[0-3]{1})|(15[4-9]{1})|(18[0-9]{1})|(199))+\d{8})$/
      if (myreg.test(phone)) {
        flag = true
      }
      return flag
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
