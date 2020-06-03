<template>
  <div class="login-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="login-grid">
      <div class="login-title">
        <h1><span>店铺登录</span></h1>
      </div>
      <div class="login-form">
        <el-form ref="shopLoginFormRef" :model="shopLoginForm" :rules="shopLoginFormRules">
          <el-form-item class="form-item" prop="phone">
            <el-input v-model="shopLoginForm.phone" class="form-item-input" placeholder="请输入手机号码" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item class="form-item" prop="password">
            <el-input v-model="shopLoginForm.password" class="form-item-input" id="form-item-input-password" placeholder="请输入密码" type="password" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <div style="height: 40px;"></div>
          <el-form-item>
            <div class="form-item-link" id="form-item-link-top">
              <el-link href="/#/customer/login" class="form-item-link-top" icon="el-icon-goods">用户登录</el-link>
            </div>
            <div class="form-item-btn">
              <el-button class="login-btn" type="primary" @click="shopLogin">登录</el-button>
            </div>
            <div class="form-item-link">
              <el-link href="/#/shop/register" class="form-item-link-bottom" icon="el-icon-edit">立即注册</el-link>
            </div>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from './navBar.vue'
export default {
  components: {
    navbar
  },
  data () {
    return {
      shopLoginForm: {
        phone: '',
        password: ''
      },
      shopLoginFormRules: {
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
    shopLogin () {
      this.$refs.shopLoginFormRef.validate(async valid => {
        if (!valid) {
          return
        }
        if (!this.isMobileNumber(this.shopLoginForm.phone)) {
          return this.$message.error('手机号格式错误!')
        }
        await this.$http.get('shop/login', {
          params: {
            phone: this.shopLoginForm.phone,
            password: this.shopLoginForm.password
          }
        }).then(response => {
          // 登录成功后的操作
          this.$message.success('登录成功!')
          window.sessionStorage.setItem('shoptoken', response.data.token)
          this.$router.push({ name: 'shop' })
        }).catch(err => {
          console.log(err)
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
