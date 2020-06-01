<template>
  <div class="customer-address-grid-wrapper">
    <div class="address-grid-container" v-for="(addr, index) in addrList" :key="index">
      <div class="address-grid">
        <div class="address-info">
          <p><span>收件人姓名: {{ addr.name }}</span></p>
          <p><span>收件人手机号: {{ addr.tel }}</span></p>
          <p><span>详细地址: {{ addr.address }}</span></p>
        </div>
        <div class="delete-address-btn-container">
          <el-button @click="onEditAddressClicked(addr)" type="primary" class="edit-address-btn" icon="el-icon-edit" circle></el-button>
          <el-button @click="onAddressDeleteClicked(addr)" type="danger" class="delete-address-btn" icon="el-icon-delete" circle></el-button>
        </div>
      </div>
    </div>
    <div style="height: 100px;"></div>
  </div>
</template>

<script>
export default {
  props: ['addrList'],
  methods: {
    onEditAddressClicked (addr) {
      this.$router.push({
        name: 'customerAddressAdd',
        query: {
          editType: 'editOldAddress',
          receiver: addr.name,
          phone: addr.tel,
          address: addr.address,
          addressId: addr.addressId
        }
      })
    },
    onAddressDeleteClicked (addr) {
      this.$confirm('此操作将删除地址, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$http.delete('address', {
          headers: {
            Authorization: window.sessionStorage.getItem('token')
          },
          params: {
            address_id: addr.addressId
          }
        }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          this.$router.push('/customer')
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  }
}
</script>

<style lang="less" scoped>
.address-grid{
  width: 400px;
  height: 200px;
  border: 1px solid rgb(139, 139, 139);
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  margin-top: 30px;
  padding-left: 10px;
  padding-top: 10px;
}
.delete-address-btn-container{
  width: 100px;
  height: 40px;
  position: relative;
  left: 85%;
  transform: translate(-50%);
}
.address-grid-container{
  width: 100%;
  height: 240px;
}
.delete-address-btn{
  right: 0;
  position: relative;
}
</style>
