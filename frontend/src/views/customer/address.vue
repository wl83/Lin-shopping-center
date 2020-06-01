<template>
  <div class="address-container">
    <header>
      <navbar></navbar>
    </header>

    <addressgrid :addrList="addrList"></addressgrid>

    <div class="add-address-btn-container">
      <el-button @click="onAddAddressClicked" type="success" class="add-address-btn">新增地址</el-button>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import addressgrid from './addressGrid.vue'
export default {
  components: {
    navbar,
    addressgrid
  },
  data () {
    return {
      addrList: []
    }
  },
  methods: {
    onAddAddressClicked () {
      this.$router.push({
        name: 'customerAddressAdd',
        query: {
          editType: 'addNewAddress'
        }
      })
    }
  },
  mounted: function () {
    this.$http.get('address', {
      headers: {
        Authorization: window.sessionStorage.getItem('token')
      }
    }).then(response => {
      response.data.addrs.forEach((addr, index) => {
        this.addrList.push({
          id: index,
          name: addr.receiver,
          tel: addr.phone,
          address: addr.address,
          addressId: addr.id
        })
      })
    }).catch(err => {
      if (err.response.status === 401) {
        this.$router.push({ name: 'customerLogin' })
      }
      console.error(err)
    })
  }
}
</script>

<style lang="less" scoped>
.add-address-btn-container{
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 70px;
  margin-top: 30px;
  border: 1px solid rgb(134, 134, 134);
  background-color: #fff;
}
.add-address-btn{
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 130px;
}
</style>
