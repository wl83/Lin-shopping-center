<template>
  <div class="register-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="register-grid">
      <div class="register-title">
        <h1 style="text-align: center;"><span>店铺注册</span></h1>
      </div>
      <div style= "height: 30px;"></div>
      <div class="register-form">
        <el-form :label-position="labelPosition" label-width="80px" ref="shopRegisterFormRef" :model="shopRegisterForm" :rules="shopRegisterFormRules">
          <el-form-item class="form-item" label="手机号" prop="phone">
            <el-input v-model="shopRegisterForm.phone" placeholder="请输入手机号" prefix-icon="el-icon-phone-outline"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="密码" prop="password">
            <el-input v-model="shopRegisterForm.password" placeholder="请输入密码" type="password" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="确认密码" prop="passwordAgain">
            <el-input v-model="shopRegisterForm.passwordAgain" placeholder="请再次输入密码" type="password" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="店铺名称" prop="name">
            <el-input v-model="shopRegisterForm.name" placeholder="请输入名称" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="店铺地址" prop="address">
            <el-input v-model="shopRegisterForm.address" placeholder="请输入店铺地址" prefix-icon="el-icon-location-outline"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="店铺介绍" prop="info">
            <el-input
              prefix-icon="el-icon-document"
              type="textarea"
              placeholder="请输入店铺简介"
              v-model="shopRegisterForm.info"
              maxlength="100"
              :rows='3'
              show-word-limit
            >
            </el-input>
          </el-form-item>
          <el-form-item class="form-item" prop="button">
            <el-button type="primary" class="register-btn" @click="shopRegister">注册</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from './navBar.vue'
export default {
  data () {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.shopRegisterForm.passwordAgain !== '') {
          this.$refs.shopRegisterFormRef.validateField('checkpasswordAgainPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.shopRegisterForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      labelPosition: 'right',
      shopRegisterForm: {
        phone: '',
        password: '',
        passwordAgain: '',
        name: '',
        address: '',
        info: '',
        captchaIdentifer: '',
        captchaCode: ''
      },
      shopRegisterFormRules: {
        phone: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 16, message: '长度在6到16字符之间', trigger: 'blur' },
          { validator: validatePass, trigger: 'blur' }
        ],
        passwordAgain: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          { validator: validatePass2, trigger: 'blur' }
        ],
        name: [
          { required: true, message: '请输入店铺名称', trigger: 'blur' }
        ],
        address: [
          { required: true, message: '请输入店铺地址', trigger: 'blur' }
        ],
        info: [
          { required: true, message: '请输入店铺简介', trigger: 'blur' }
        ],
        button: [

        ]
      }
    }
  },
  components: {
    navbar
  },
  methods: {
    shopRegister () {
      this.$refs.shopRegisterFormRef.validate(async valid => {
        if (!valid) {
          return
        }
        if (!this.isMobileNumber(this.shopRegisterForm.phone)) {
          return this.$message.error('手机号格式错误!')
        }
        await this.$http.post('shop/create', {
          phone: this.shopRegisterForm.phone,
          password: this.shopRegisterForm.password,
          name: this.shopRegisterForm.name,
          info: this.shopRegisterForm.info,
          address: this.shopRegisterForm.address,
          captcha_identifer: this.shopRegisterForm.captchaIdentifer,
          captcha_code: this.shopRegisterForm.captchaCode
        }).then(() => {
          this.$message.success('注册成功!')
          this.$router.push({ name: 'shopLogin' })
        }).catch(err => {
          console.log(err)
          if (typeof err.response.data.message === 'string') {
            if (err.response.data.message.startsWith('Phone')) {
              this.$message.error('手机号已注册!')
              this.$router.push({ name: 'shopLogin' })
            }
          } else {
            this.$message.error('注册失败，请重试!')
          }
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
  .register-grid{
    width: 50%;
    height: 700px;
    position: absolute;
    left: 50%;
    top: 20%;
    transform: translate(-50%, 0);
    border: 1px solid rgb(199, 198, 198);
    padding-left: 50px;
    padding-right: 50px;
    padding-top: 20px;
    padding-bottom: 20px;
    margin-bottom: 100px;
  }
  .form-item{
    margin-bottom: 40px;
  }

  .register-btn {
    width: 150px;
    position: absolute;
    left: 50%;
    transform: translate(-70%);
  }
</style>
