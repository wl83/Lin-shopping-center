<template>
  <div class="shop-index-wrapper">
    <header>
      <navbar></navbar>
    </header>

    <div class="shop-index-info-container">
      <div class="shop-index-intro-container">
        <div class="shop-title-container">
          <span>{{ this.name }}</span>
        </div>
        <div class="shop-address-container">
          <i class="el-icon-location-outline"></i>
          <span>{{ this.address }}</span>
        </div>
        <div class="shop-info-container">
          <i class="el-icon-document"></i>
          <span>简介: {{ this.info }}</span>
        </div>
        <div class="shop-phone-container">
          <i class="el-icon-phone-outline"></i>
          <span>联系电话: {{ this.phone }}</span>
        </div>
      </div>
        <div class="shop-manage-container">
          <div class="shop-manage-grid">
            <el-button @click="onManageClicked" icon="el-icon-shopping-cart-2" type="primary" plain class="btn">管理商店</el-button>
          </div>
          <div class="shop-manage-grid">
            <el-button icon="el-icon-notebook-1" type="success" plain class="btn">全部订单</el-button>
          </div>
          <div class="shop-manage-grid">
            <el-button icon="el-icon-edit-outline" type="warning" plain class="btn">历史评价</el-button>
          </div>
          <div class="shop-manage-grid">
            <el-button icon="el-icon-document-delete" type="danger" plain class="btn">注销商店</el-button>
          </div>
          <div class="shop-manage-grid">
            <el-button @click="onLogOutClicked" icon="el-icon-setting" type="info" plain class="btn">退出登录</el-button>
          </div>
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
      shopId: '',
      phone: '',
      name: '',
      address: '',
      info: ''
    }
  },
  methods: {
    onManageClicked () {
      this.$router.push({ name: 'shopManage', params: { shopId: this.shopId } })
    },
    onLogOutClicked () {
      this.$confirm('此操作将退出登录, 是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        window.sessionStorage.clear()
        this.$message({
          type: 'success',
          message: '退出成功!'
        })
        this.$router.push('shop/login')
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消退出'
        })
      })
    }
  },
  mounted: function () {
    this.$http.get('shop', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      this.shopId = response.data.shop_id
      this.name = response.data.name
      this.phone = response.data.phone
      this.address = response.data.address
      this.info = response.data.info
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less" scoped>
  .shop-index-wrapper{
    width: 100%;
    height: 700px;
  }
  .shop-index-info-container{
    width: 60%;
    height: 60%;
    border: 1px solid rgb(160, 160, 160);
    position: relative;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    padding: 10px 10px 10px 10px;
  }
  .shop-index-intro-container{
    width: 70%;
    height: 95%;
    border: 1px solid;
    float: left;
  }
  .shop-manage-container{
    width: 28%;
    height: 95%;
    border: 1px solid;
    float: right;
  }
  .shop-title-container{
    width: 100%;
    height: 25%;
  }
  .shop-title-container span{
    position: relative;
    top: 25%;
    font-size: 25px;
  }
  .shop-address-container{
    width: 100%;
    height: 20%;
  }
  .shop-address-container span{
    color: rgb(144, 144, 144);
  }
  .shop-info-container{
    width: 100%;
    height: 20%;
  }
  .shop-phone-container{
    width: 100%;
    height: 20%;
  }
  .shop-manage-grid{
    width: 100%;
    height: 15%;
    margin-top: 10px;
  }
  .shop-manage-grid .btn{
    position: relative;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
</style>
