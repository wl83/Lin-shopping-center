<template>
  <div class="register-container">
    <header>

    </header>

    <div class="register-grid">
      <div class="register-title">
        <h1><span>用户注册</span></h1>
      </div>
      <div style= "height:30px;"></div>
      <div class="register-form">
        <el-form :label-position="labelPosition" label-width="80px" ref="customerRegisterFormRef" :model="customerRegisterForm" :rules="customerRegisterFormRules">
          <el-form-item class="form-item" label="手机号" prop="phone">
            <el-input v-model="customerRegisterForm.phone" placeholder="请输入手机号" prefix-icon="el-icon-phone-outline"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="密码" prop="password">
            <el-input v-model="customerRegisterForm.password" placeholder="请输入密码" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="确认密码" prop="passwordAgain">
            <el-input v-model="customerRegisterForm.passwordAgain" placeholder="请再次输入密码" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="性别" prop="gender">
            <el-select v-model="genderValue" placeholder="请选择性别">
              <el-option
                v-for="item in genderOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item class="form-item" label="头像">

          </el-form-item>
          <el-form-item class="form-item">

          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.customerRegisterForm.passwordAgain !== '') {
          this.$refs.customerRegisterFormRef.validateField('checkpasswordAgainPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.customerRegisterForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      labelPosition: 'right',
      customerRegisterForm: {
        phone: '',
        password: '',
        passwordAgain: ''
      },
      customerRegisterFormRules: {
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
        gender: [
          { required: true, message: '请选择性别' }
        ]
      },
      genderOptions: [{
        value: 0,
        label: '男'
      }, {
        value: 1,
        label: '女'
      }],
      genderValue: ''
    }
  }
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
  .register-title{
    width: 100%;
  }
  .register-title h1{
    text-align: center;
  }
  .register-grid{
    width: 50%;
    height: 500px;
    position: absolute;
    left: 50%;
    top: 20%;
    transform: translate(-50%, 0);
    border: 1px solid rgb(199, 198, 198);
    padding-left: 50px;
    padding-right: 50px;
    padding-top: 20px;
    padding-bottom: 20px;
  }
  .form-item{
    margin-bottom: 40px;
  }
</style>
