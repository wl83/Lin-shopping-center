<template>
  <div class="add-address-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="add-address-grid">
      <div class="add-address-title">
        <h1><span>新增/更新地址</span></h1>
      </div>
      <div class="add-address-form">
        <el-form ref="addressFormRef" :rules="addressFormRules" :label-position="labelPosition" label-width="80px" :model="addressForm">
          <el-form-item label="收件人姓名" prop="name">
            <el-input v-model="addressForm.name" placeholder="请输入收件人姓名" prefix-icon="el-icon-user-solid"></el-input>
          </el-form-item>
          <el-form-item label="收件人手机号" prop="phone">
            <el-input v-model="addressForm.phone" placeholder="请输入收件人手机号" prefix-icon="el-icon-phone"></el-input>
          </el-form-item>
          <el-form-item label="详细地址" prop="address">
            <el-input v-model="addressForm.address" placeholder="请输入详细地址" prefix-icon="el-icon-location"></el-input>
          </el-form-item>
        </el-form>
      </div>
      <div class="add-address-btn-container">
        <el-button @click="onSaveClicked" type="success" class="add-address-btn">保存</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
export default {
  components: {
    navbar
  },
  data () {
    return {
      labelPosition: 'top',
      addressForm: {
        name: '',
        phone: '',
        address: ''
      },
      addressFormRules: {
        name: [
          { required: true, message: '请输入收件人姓名', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ],
        address: [
          { required: true, message: '请输入详细地址', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onSaveClicked () {
      this.$refs.addressFormRef.validate(async valid => {
        if (!valid) {
          return
        }
        if (!this.isMobileNumber(this.addressForm.phone)) {
          return this.$message.error('手机号格式错误!')
        }
        if (this.$route.query.editType === 'addNewAddress') {
          await this.$http.post('address', {
            receiver: this.addressForm.name,
            phone: this.addressForm.phone,
            address: this.addressForm.address
          },
          {
            headers: {
              Authorization: window.sessionStorage.getItem('token')
            }
          }).then(response => {
            this.$message.success('新增地址成功')
            if (this.$route.query.from === 'customerCartSubmit') {
              this.$router.push('/customer/cart/submit')
            } else {
              this.$router.push('/customer/address')
            }
          }).catch(err => {
            console.log(err)
          })
        } else if (this.$route.query.editType === 'editOldAddress') {
          await this.$http.put('address', {
            receiver: this.addressForm.name,
            phone: this.addressForm.phone,
            address: this.addressForm.address,
            address_id: this.$route.query.addressId
          }, {
            headers: {
              Authorization: window.sessionStorage.getItem('token')
            }
          }).then(response => {
            this.$message.success('更新地址成功')
            this.$router.push('/customer/address')
          }).catch(err => {
            console.log(err)
          })
        }
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
  },
  mounted: function () {
    this.addressForm.name = this.$route.query.receiver
    this.addressForm.phone = this.$route.query.phone
    this.addressForm.address = this.$route.query.address
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
  height: 15%;
}
.add-address-btn{
  position: relative;
  left: 50%;
  transform: translate(-50%);
}
.delete-address-btn{
  position: relative;
  top: 50%;
  left: 38.5%;
  transform: translate(-50%, 0);
}
</style>
