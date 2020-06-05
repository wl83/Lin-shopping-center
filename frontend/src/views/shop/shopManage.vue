<template>
  <div class="shop-manage-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside class="shop-aside-container"></shopaside>
    </div>

    <div class="register-grid">
      <div class="register-title">
        <h1 style="text-align: center;"><span>商家信息管理</span></h1>
      </div>
      <div style= "height:30px;"></div>
      <div class="register-form">
        <el-form :label-position="labelPosition" label-width="80px" ref="shopManageFormRef" :model="shopManageForm" :rules="shopManageFormRules">
          <el-form-item class="form-item" label="店铺名" prop="name">
            <el-input v-model="shopManageForm.name" placeholder="请输入店铺名" prefix-icon="el-icon-phone-outline"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="手机号" prop="phone">
            <el-input v-model="shopManageForm.phone" placeholder="请输入手机号" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="地址" prop="address">
            <el-input v-model="shopManageForm.address" placeholder="请输入地址" prefix-icon="el-icon-location-outline"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="简介" prop="info">
            <el-input
              type="textarea"
              v-model="shopManageForm.info"
              placeholder="请输入店铺简介"
              prefix-icon="el-icon-user"
              :maxlength="100"
              :rows="3"
              show-word-limit>
            </el-input>
          </el-form-item>
          <el-form-item class="form-item">
            <el-button type="primary" class="register-btn" @click="updateShop">保存</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import shopaside from '../../components/shopAside.vue'
export default {
  components: {
    navbar,
    shopaside
  },
  data () {
    return {
      labelPosition: 'right',
      shopId: '',
      shopManageForm: {
        phone: '',
        name: '',
        address: '',
        info: ''
      },
      shopManageFormRules: {
        phone: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ],
        name: [
          { required: true, message: '请输入名称', trigger: 'blur' }
        ],
        address: [
          { required: true, message: '请输入店铺地址', trigger: 'blur' }
        ],
        info: [
          { required: true, message: '请输入店铺简介', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    updateShop () {
      this.$refs.shopManageFormRef.validate(async valid => {
        if (!valid) {
          return
        }
        await this.$http.put('shop', {
          shop_id: this.shopId,
          name: this.shopManageForm.name,
          phone: this.shopManageForm.phone,
          info: this.shopManageForm.info,
          address: this.shopManageForm.address
        },
        {
          headers: {
            Authorization: window.sessionStorage.getItem('shoptoken')
          }
        }).then(() => {
          this.$message.success('更新成功')
          this.$router.push('/shop')
        }).catch(err => {
          console.log(err)
        })
      })
    }
  },
  mounted: function () {
    this.shopId = this.$route.params.shopId
    this.$http.get('shop', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      this.shopManageForm.name = response.data.name
      this.shopManageForm.phone = response.data.phone
      this.shopManageForm.address = response.data.address
      this.shopManageForm.info = response.data.info
    })
  }
}
</script>

<style lang="less" scoped>
  .shop-manage-wrapper{
    width: 100%;
    height: 1000px;
  }
  .register-grid{
    width: 50%;
    height: 550px;
    position: absolute;
    left: 55%;
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
