<template>
  <div class="cart-submit-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="address-container">
      <div class="address-grid">
        <div class="address-info">
          <div class="address-name-phone-container">
            <div class="address-name-container">
              <span>{{ this.chosenAddr.name }}</span>
            </div>
            <div class="address-phone-container">
              <span>{{ this.chosenAddr.tel }}</span>
            </div>
          </div>
          <div class="address-info-container">
            <span>{{ this.chosenAddr.address }}</span>
          </div>
        </div>
        <div class="address-select-btn">
          <el-button class="address-select" @click="drawer=true" type="primary" style="margin-left: 16px;">
            选择地址
          </el-button>
        </div>
      </div>
    </div>
    <el-drawer
      title="选择地址"
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose">
      <addressgrid :addrList="addrList" @childFn="parentFn"></addressgrid>
      <div class="address-add-container">
        <el-button @click="onAddAddressClicked" class="address-add-btn" type="success">新增地址</el-button>
      </div>
    </el-drawer>

    <cartsubmitgrid :orderList="orderList"></cartsubmitgrid>

    <div class="cart-submit-order">
      <div class="cart-total-price">
        <div class="cart-total-price-wrapper">
          <span>¥{{ this.totalPrice }}</span>
        </div>
      </div>
      <div class="cart-submit-btn">
        <el-button @click="onSubmitClicked" type="success" class="cart-submit">下单</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import cartsubmitgrid from '../../components/cartSubmitGrid.vue'
import addressgrid from '../../components/addressGrid.vue'
export default {
  components: {
    navbar,
    cartsubmitgrid,
    addressgrid
  },
  data () {
    return {
      drawer: false,
      direction: 'rtl',
      num: 1,
      fit: 'contain',
      addrList: [],
      orderList: [],
      chosenAddr: {}
    }
  },
  methods: {
    onAddAddressClicked () {
      this.$router.push({
        name: 'customerAddressAdd',
        query: {
          editType: 'addNewAddress',
          from: 'customerCartSubmit'
        }
      })
    },
    handleClose (done) {
      done()
    },
    parentFn (childData) {
      this.chosenAddr = childData
    },
    onSubmitClicked () {
      if (this.chosenAddr === {}) {
        this.$message.error('请填写地址')
        return
      }
      let addressId = 0
      this.addrList.forEach(addr => {
        if (addr.id === this.chosenAddr.id) {
          addressId = addr.addressId
        }
      })

      this.$http.post('order/create', {
        address_id: addressId
      }, {
        headers: {
          Authorization: window.sessionStorage.getItem('token')
        }
      }).then(response => {
        this.$message.success('订单提交成功')
        this.$router.push('/')
      }).catch(err => {
        if (err.response.data.message === 'Invalid address id') {
          this.$message.error('请填写正确地址')
        } else if (err.response.data.item_id) {
          this.$message.error('某商品库存不足')
        } else {
          console.error(err)
        }
      })
    }
  },
  computed: {
    /* 计算所选商品总价 */
    totalPrice () {
      return (
        this.orderList.reduce(
          (total, item) => total + item.currentPrice * item.count,
          0
        )
      )
    }
  },
  mounted: function () {
    // 获取地址信息
    this.$http.get('address', {
      headers: {
        Authorization: window.sessionStorage.getItem('token')
      }
    }).then(response => {
      const addresses = response.data.addrs

      addresses.forEach((addr, index) => {
        this.addrList.push({
          id: index,
          name: addr.receiver,
          tel: addr.phone,
          address: addr.address,
          addressId: addr.id
        })
      })
    }).catch(err => err)

    // 获取商品item_id
    this.$http.get('cart', {
      headers: {
        Authorization: window.sessionStorage.getItem('token')
      }
    }).then(response => {
      const items = response.data.items

      items.forEach((item, index) => {
        const tmpItem = {}
        if (item.selected) {
          tmpItem.id = index
          this.$http.get('items/' + item.item_id, {})
            .then(response => {
              if (item.selected) {
                tmpItem.itemId = item.item_id
                tmpItem.selected = item.selected
                tmpItem.count = item.count
                tmpItem.name = response.data.name
                tmpItem.currentPrice = response.data.current_price
                tmpItem.originalPrice = response.data.original_price
                tmpItem.inStock = response.data.in_stock
                tmpItem.info = response.data.info
                tmpItem.sales = response.data.sales
                tmpItem.shopId = response.data.shop_id
                tmpItem.images = response.data.images
                this.orderList.push(tmpItem)
              }
            }).catch(err => {
              console.log(err)
            })
        }
      })
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less" scoped>
.address-container{
  width: 100%;
  height: 150px;
  border: 1px solid rgb(148, 148, 148);
  border-top: 0px;
}
.address-grid{
  width: 51%;
  height: 100%;
  border: 1px solid rgb(163, 163, 163);
  border-bottom: 0px;
  left: 50%;
  transform: translate(-50%);
  position: relative;
}
.address-info{
  width: 80%;
  height: 60%;
  left: 50%;
  top: 5%;
  transform: translate(-50%);
  position: relative;
}
.address-select-btn{
  width: 80%;
  height: 30%;
  left: 50%;
  top: 5%;
  transform: translate(-50%);
  position: relative;
}
.address-select{
  left: 50%;
  top: 10%;
  transform: translate(-50%);
  position: relative;
}
.address-name-phone-container{
  width: 100%;
  height: 35%;
  position: relative;
  margin-bottom: 20px;
}
.address-name-container{
  width: 48%;
  height: 100%;
  position: relative;
  float: left;
}
.address-name-container span{
  font-size: 25px;
}
.address-phone-container{
  width: 50%;
  height: 100%;
  position: relative;
  float: left;
}
.address-phone-container span{
  color: rgb(230, 0, 0);
}
.address-info-container{
  width: 100%;
  height: 60%;
  position: relative;
  overflow: hidden;
}
.address-info-container span{
  color: rgb(133, 133, 133);
}
.cart-submit-order{
  width: 100%;
  height: 70px;
  position: fixed;
  bottom: 0;
  border: 1px solid rgb(156, 156, 156);
  background-color: #fff;
}
.cart-total-price{
  width: 50%;
  height: 70px;
  border: 1px solid rgb(149, 149, 149);
  border-top: 0px;
  border-right: 0px;
  border-left: 0px;
  float: left;
}
.cart-total-price-wrapper{
  width: 25%;
  height: 60%;
  left: 70%;
  top: 50%;
  transform: translate(-50%, -50%);
  position: relative;
}
.cart-total-price span{
  font-size: 35px;
  color: rgb(223, 4, 4);
}
.cart-submit-btn{
  width: 49%;
  height: 70px;
  border: 1px solid rgb(158, 158, 158);
  border-right: 0px;
  border-top: 0px;
  float: left;
}
.cart-submit{
  width: 150px;
  position: relative;
  left: 10%;
  top: 50%;
  transform: translate(0,-50%);
}
.address-add-container{
  width: 100%;
  height: 10%;
  position: fixed;
  bottom: 0;
  background-color: #fff;
}
.address-add-btn{
  width: 100px;
  position: absolute;
  left: 12%;
  top: 20%;
}
</style>
