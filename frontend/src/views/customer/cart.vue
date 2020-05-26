<template>
  <div class="cart-container">
    <header>
      <navbar></navbar>
    </header>

    <cartgrid :cartitems="cartitems"></cartgrid>

    <div class="cart-submit-container">
      <div class="cart-total-price-container">
        <div class="cart-total-price">
          <span>¥{{ this.totalPrice }}</span>
        </div>
      </div>
      <div class="cart-submit-btn">
        <el-button @click="onCartSubmitClicked" :disabled="disableSubmit" type="danger" class="cart-submit">{{ this.submitBarText }}</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import cartgrid from '../../components/cartGrid.vue'
export default {
  components: {
    navbar,
    cartgrid
  },
  data () {
    return {
      cartitems: [],
      totalPrice: 0,
      disableSubmit: true,
      submitBarText: ''
    }
  },
  /* 监测输入数据改变 */
  watch: {
    cartitems: {
      handler: function () {
        const count = this.cartitems.reduce(
          (total, item) => total + (item.selected ? item.count : 0),
          0
        )
        this.submitBarText = '结算' + (count ? `(${count})` : '')

        this.totalPrice =
          this.cartitems.reduce(
            (total, item) =>
              total + (item.selected ? item.currentPrice * item.count : 0),
            0
          )

        this.disableSubmit = !this.cartitems.some(item => item.selected)
      },
      deep: true
    }
  },
  methods: {
    handleChange () {

    },
    getCartList () {
      this.cartitems = []
      this.$http.get('cart', {
        headers: {
          Authorization: window.sessionStorage.getItem('token')
        }
      }).then(response => {
        const items = response.data.items
        items.forEach(item => {
          var tempItem = { selected: false, count: 0 }

          this.$http.get('items/' + item.item_id, {})
            .then(response => {
              tempItem.itemId = item.item_id
              tempItem.id = +item.item_id
              tempItem.selected = item.selected
              tempItem.count = item.count
              tempItem.name = response.data.name
              tempItem.currentPrice = response.data.current_price
              tempItem.originalPrice = response.data.original_price
              tempItem.inStock = response.data.in_stock
              tempItem.info = response.data.info
              tempItem.sales = response.data.sales
              tempItem.shopId = response.data.shop_id
              tempItem.images = response.data.images
              this.cartitems.push(tempItem)
            }).catch(err => {
              console.log(err)
            })
        })
      }).catch(err => {
        console.log(err)
      })
    },
    onCartSubmitClicked () {
      this.$router.push({ name: 'customerCartSubmit' })
    }
  },
  mounted: function () {
    this.getCartList()
    var price = 0
    for (var i = 0; i < this.cartitems.length; i++) {
      price += this.cartitems[i].currentPirce
    }
    this.totalPrice = price
  }
}
</script>

<style lang="less" scoped>
.cart-container{
  width: 100%;
  height: 700px;
}
.cart-submit-container{
  width: 100%;
  height: 70px;
  position: fixed;
  bottom: 0;
  border: 1px solid rgb(146, 146, 146);
  background-color: #fff;
}
.cart-total-price-container{
  width: 50%;
  height: 70px;
  float: left;
}
.cart-total-price{
  width: 20%;
  height: 50%;
  left: 75%;
  top: 50%;
  transform: translate(-10%, -50%);
  position: relative;
}
.cart-total-price span{
  position: relative;
  color: rgb(231, 0, 0);
  font-size: 30px;
}
.cart-submit-btn{
  width: 49%;
  height: 70px;
  border-left: 1px solid rgb(158, 158, 158);
  float: left;
}
.cart-submit{
  width: 150px;
  position: relative;
  left: 10%;
  top: 50%;
  transform: translate(0,-50%);
}
</style>
