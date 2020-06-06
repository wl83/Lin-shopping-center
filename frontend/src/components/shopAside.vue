<template>
    <div class="shop-aside-wrapper">
    <el-row class="tac">
      <el-col :span="12">
        <el-menu
          default-active=""
          class="el-menu-vertical-demo"
          @select="onMenuSelected"
          >

          <el-menu-item index="1">
            <i class="el-icon-menu"></i>
            <span slot="title">信息管理</span>
          </el-menu-item>

          <el-menu-item index="2">
            <i class="el-icon-goods"></i>
            <span slot="title">商品管理</span>
          </el-menu-item>

          <el-menu-item index="3">
            <i class="el-icon-document"></i>
            <span slot="title">订单管理</span>
          </el-menu-item>

          <el-menu-item index="4">
            <i class="el-icon-edit"></i>
            <span slot="title">全部评价</span>
          </el-menu-item>

          <el-menu-item index="7">
            <i class="el-icon-data-line"></i>
            <span slot="title">查看报表</span>
          </el-menu-item>

          <el-menu-item index="5">
            <i class="el-icon-setting"></i>
            <span slot="title">退出登录</span>
          </el-menu-item>

          <el-menu-item index="6">
            <i class="el-icon-document-delete"></i>
            <span slot="title">注销店铺</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </div>

</template>

<script>
export default {
  props: ['shopId'],
  methods: {
    onMenuSelected (index) {
      switch (index) {
        case '1': {
          this.$router.push({ name: 'shopManage', params: { shopId: this.shopId } })
          break
        }
        case '2': {
          this.$router.push({ name: 'shopItems', params: { shopId: this.shopId } })
          break
        }
        case '3': {
          this.$router.push({ name: 'shopOrders' })
          break
        }
        case '4': {
          this.$router.push({ name: 'shopReviews', params: { shopId: this.shopId } })
          break
        }
        case '5': {
          this.$confirm('此操作将退出登录，是否继续？', '提示', {
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
          break
        }
        case '6': {
          this.$confirm('此操作将注销店铺，店铺内商品也将全部删除，是否继续？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            this.$http.delete('shop', {
              shop_id: this.shopId
            },
            {
              headers: {
                Authorization: window.sessionStorage.getItem('shoptoken')
              }
            }).then(() => {
              this.$message({
                type: 'success',
                message: '注销成功!'
              })
              this.$router.push('/')
            }).catch(err => {
              console.log(err)
            })
          }).catch(() => {
            this.$message({
              type: 'info',
              message: '已取消注销'
            })
          })
          break
        }
        case '7': {
          this.$router.push({ name: 'shopReport', params: { shopId: this.shopId } })
          break
        }
      }
    }
  }
}
</script>

<style lang="less" scoped>
.shop-aside-wrapper{
  width: 100%;
  height: 100%;
}
.tac{
  position: relative;
  width: 100%;
  height: 100%;
}
</style>
