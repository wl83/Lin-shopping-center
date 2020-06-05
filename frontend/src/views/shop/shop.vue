<template>
  <div class="shop-index-wrapper">
    <header>
      <navbar></navbar>
    </header>

    <div class="shop-aside-name-container">
      <shopaside :shopId="shopId" class="shop-aside-container"></shopaside>
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
</style>
