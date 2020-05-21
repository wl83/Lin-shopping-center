<template>
  <div class="register-container">
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

    <div class="register-grid">
      <div class="register-title">
        <h1 style="text-align: center;"><span>用户注册</span></h1>
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
            <el-upload
              class="avatar-uploader"
              action="https://jsonplaceholder.typicode.com/posts/"
              :show-file-list="true"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload">
              <img v-if="imageUrl" :src="imageUrl" class="avatar">
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
          <el-form-item class="form-item">
            <el-button type="primary" class="register-btn">注册</el-button>
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
      searchQuery: {
        text: ''
      },
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
          { required: true, message: '请选择性别', trigger: 'blur' }
        ]
      },
      genderOptions: [{
        value: 0,
        label: '男'
      }, {
        value: 1,
        label: '女'
      }],
      genderValue: '',
      imageUrl: ''
    }
  },
  methods: {
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg'
      const isPng = file.type === 'image/png'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG && !isPng) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isPng && isLt2M
    },
    handleSelect () {

    }
  }
}
</script>

<style lang="less" scoped>
  .register-grid{
    width: 50%;
    height: 650px;
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
  .avatar-uploader{
    width: 100px;
    height: 100px;
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 100px;
    height: 100px;
    line-height: 100px;
    text-align: center;
  }
  .avatar {
    width: 100px;
    height: 100px;
    display: block;
  }
  .register-btn {
    width: 150px;
    position: absolute;
    left: 50%;
    transform: translate(-70%);
  }
</style>
