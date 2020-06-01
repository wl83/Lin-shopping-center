<template>
  <div class="customer-center-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="customer-info-container">
      <div class="customer-image-container">
        <el-image
          class="customer-image"
          :src="'data:image/jpeg;base64,' + image"
          :fit="fit"></el-image>
      </div>
      <div class="customer-intro-container">
        <div class="customer-intro">
          <div class="customer-name-container">
            <p><span>姓名:</span> {{ this.nickname }}</p>
          </div>
          <div class="customer-phone-container">
            <p><span>手机号:</span>{{ this.phone }}</p>
          </div>
          <div class="customer-gender-container">
            <p><span>性别:</span>{{ this.gender }}</p>
          </div>
          <div class="customer-created-time-container">
            <p><span>创建时间:</span>{{ this.created_time }}</p>
          </div>
        </div>
        <div class="customer-manage-container">
          <div class="customer-manage-grid">
            <el-button @click="onCartClicked" icon="el-icon-shopping-cart-2" type="danger" plain class="btn">购物车</el-button>
          </div>
          <div class="customer-manage-grid">
            <el-button @click="onOrderClicked" icon="el-icon-notebook-1" type="success" plain class="btn">全部订单</el-button>
          </div>
          <div class="customer-manage-grid">
            <el-button @click="onReviewClicked" icon="el-icon-edit-outline" type="warning" plain class="btn">历史评价</el-button>
          </div>
          <div class="customer-manage-grid">
            <el-button icon="el-icon-location-information" type="primary" plain class="btn">编辑地址</el-button>
          </div>
          <div class="customer-manage-grid">
            <el-button icon="el-icon-document-delete" type="info" plain class="btn" @click="onLogoutClicked">退出登录</el-button>
          </div>
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
      url: '',
      phone: '',
      nickname: '',
      gender: '',
      created_time: '',
      image: '',
      fit: 'cover'
    }
  },
  methods: {
    onReviewClicked () {

    },
    onLogoutClicked () {
      this.$confirm('此操作将退出登录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        window.sessionStorage.clear()
        this.$message({
          type: 'success',
          message: '退出成功!'
        })
        this.$router.push('customer/login')
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消退出'
        })
      })
    },
    onCartClicked () {
      this.$router.push({ name: 'customerCart' })
    },
    onOrderClicked () {
      this.$router.push({ name: 'customerOrders' })
    }
  },
  mounted: function () {
    this.$http.get('customer', {
      headers: {
        authorization: window.sessionStorage.getItem('token')
      }
    }).then(response => {
      this.phone = response.data.phone
      this.nickname = response.data.nickname
      this.gender = (response.data.gender === 1 ? '男' : '女')
      this.payment_info = response.data.payment_info
      this.created_time = response.data.created_time
      this.image = response.data.image
    }).catch(err => {
      if (err.response.status === 401) {
        this.$router.push('customer/login')
      }
    })
    console.log(this.nickname)
  }
}
</script>

<style lang="less" scoped>
.customer-info-container{
  width: 50%;
  height: 700px;
  border: 1px solid rgb(194, 194, 194);
  margin-top: 20px;
  padding: 20px 20px 20px 20px;
  left: 50%;
  top: 5%;
  transform: translate(-50%);
  position: relative;
}
.customer-image-container{
  width: 25%;
  height: 170px;
  top: 2%;
  left: 50%;
  transform: translate(-50%);
  border: 1px solid rgb(192, 192, 192);
  position: relative;
}
.customer-image{
  width: 100%;
  height: 170px;
}
.customer-intro-container{
  width: 90%;
  height: 330px;
  border: 1px solid rgb(195, 195, 195);
  top: 10%;
  left: 5%;
  position: relative;
}
.customer-intro{
  width: 50%;
  height: 100%;
  border-right: 1px solid rgb(189, 189, 189);
  float: left;
}
.customer-manage-container{
  width: 49%;
  height: 100%;
  float: left;
}
.customer-manage-grid{
  width: 48%;
  height: 50px;
  margin-top: 12px;
  left: 55%;
  transform: translate(-50%);
  position: relative;
}
.btn{
  width: 120px;
  height: 50px;
}
.customer-name-container{
  width: 90%;
  height: 50px;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 20px;
}
.customer-phone-container{
  width: 90%;
  height: 50px;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 20px;
}
.customer-gender-container{
  width: 90%;
  height: 50px;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 20px;
}
.customer-created-time-container{
  width: 90%;
  height: 50px;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 20px;
}
.customer-intro span{
  color: rgb(161, 161, 161);
}
</style>
