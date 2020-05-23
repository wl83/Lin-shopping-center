<template>
  <div class="register-container">
    <header>
      <navbar></navbar>
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
            <el-input v-model="customerRegisterForm.password" placeholder="请输入密码" type="password" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="确认密码" prop="passwordAgain">
            <el-input v-model="customerRegisterForm.passwordAgain" placeholder="请再次输入密码" type="password" prefix-icon="el-icon-lock"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="名称" prop="name">
            <el-input v-model="customerRegisterForm.name" placeholder="请输入名称" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="性别" prop="gender">
            <el-select v-model="customerRegisterForm.genderValue" placeholder="请选择性别">
              <el-option
                v-for="item in genderOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item class="form-item" label="头像">
            <div>
              <el-upload
                class="avatar-uploader"
                action="https://jsonplaceholder.typicode.com/posts/"
                v-loading="progressDisplay"
                :show-file-list="false"
                :limit="1"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload"
                :on-progress="beforeAvatarprogress">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </div>
            <div>
              <el-progress v-if="progressDisplay" class="progress-bar" :percentage="loadProgress"></el-progress>
            </div>
          </el-form-item>
          <el-form-item class="form-item">
            <el-button type="primary" class="register-btn" @click="customerRegister">注册</el-button>
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
        passwordAgain: '',
        name: '',
        genderValue: 1
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
        // gender: [
        //   { required: true, message: '请选择性别', trigger: 'blur', type: 'number' }
        // ],
        name: [
          { required: true, message: '请输入名称', trigger: 'blur' }
        ]
      },
      genderOptions: [{
        value: 1,
        label: '男'
      }, {
        value: 2,
        label: '女'
      }],
      imageUrl: '',
      loadProgress: 0,
      progressDisplay: false
    }
  },
  components: {
    navbar
  },
  methods: {
    purify_images () {
      return this.imageUrl.replace(/data:image\/[^;]+;base64,/i, '')
    },
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
      // if (this.image === '') {
      //   console.log(this.imageUrl)
      // } else {
      //   console.log(this.imageUrl)
      // }
    },
    beforeAvatarUpload (file) {
      const pict = ['image/jpg', 'image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/pdf', 'image/JPG', 'image/JPEG', 'image/PBG', 'image/GIF', 'image/BMP', 'image/PDF']
      var isPict = false
      for (var i = 0; i < pict.length; i++) {
        if (file.type === pict[i]) {
          isPict = true
          break
        }
      }
      const isLt10M = file.size / 1024 / 1024 < 10

      if (!isPict) {
        this.$message.error('上传头像图片只能是 JPG 或 PNG 格式!')
      }
      if (!isLt10M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }

      return isPict && isLt10M
    },
    beforeAvatarprogress (event, file, fileList) {
      this.loadProgress = Math.floor(event.percent)
      // console.log(this.loadProgress, this.progressDisplay)
      if (this.loadProgress > 0 && this.loadProgress < 100) {
        this.progressDisplay = true
      } else if (this.loadProgress === 100) {
        this.progressDisplay = false
      }
    },
    customerRegister () {
      // if (!this.customerRegisterForm.genderValue) {
      //   console.log('...')
      // } else {
      //   console.log(this.customerRegisterForm.genderValue)
      // }
      this.$refs.customerRegisterFormRef.validate(async valid => {
        if (!valid) {
          return
        }
        if (!this.isMobileNumber(this.customerRegisterForm.phone)) {
          return this.$message.error('手机号格式错误!')
        }
        // if (!this.customerRegisterForm.genderValue) {
        //   console.log('null')
        // } else {
        //   console.log(this.customerRegisterForm.genderValue)
        // }
        await this.$http.post('customer/register', {
          phone: this.customerRegisterForm.phone,
          password: this.customerRegisterForm.password,
          nickname: this.customerRegisterForm.name,
          gender: this.customerRegisterForm.genderValue,
          image: this.purify_images()
        }).then(() => {
          this.$message.success('注册成功！')
          this.$router.push('customer/login')
        }).catch(err => {
          console.log(err)
          if (typeof err.response.data.message === 'string') {
            if (err.response.data.message.startsWith('Phone')) {
              this.$message.error('手机号已注册！')
              this.$router.push('customer/login')
            }
          } else {
            this.$message.error('注册失败，请重试！')
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
  .progress-bar{
    width: 155px;
  }
</style>
