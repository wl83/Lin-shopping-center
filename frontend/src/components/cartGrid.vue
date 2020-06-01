<template>
  <div class="cart-wrapper">
    <div class="cart-item-grid" v-for="(cartitem, index) in cartitems" :key="index">
      <div class="cart-item-checkbox-container">
        <el-checkbox @change="onItemChanged(cartitem)" class="cart-item-checkbox" v-model="cartitem.selected"></el-checkbox>
      </div>
      <div class="cart-item-other-info-container">
      <div class="item-image-container">
        <el-image
        :src="'data:image/jpeg;base64,' + cartitem.images[0]"
        class="cart-item-image"
        :fit="fit"></el-image>
      </div>
      <div class="item-info-container">
        <div class="item-name">
          <span>{{ cartitem.name }}</span>
        </div>
        <div class="item-info">
          <p>{{ cartitem.info }}</p>
        </div>
        <div class="item-price-container">
          <span>¥{{ cartitem.currentPrice }}</span>
        </div>
        <div class="item-number-more">
          <div class="item-number-container">
            <el-input-number @change="onItemChanged(cartitem)" size="small" class="item-number" v-model="cartitem.count" :min='0' label="选择数量"></el-input-number>
          </div>
          <div class="item-more-info">
            <el-link @click="onMoreInfoClicked(cartitem)" class="item-link"><i class="el-icon-view el-icon--right"></i>查看详情</el-link>
          </div>
        </div>
      </div>
    </div>
    </div>
    <div style="height: 100px;"></div>
  </div>
</template>

<script>
export default {
  props: ['cartitems'],
  data () {
    return {
      num: 1,
      fit: 'contain',
      totalPrice: 0
    }
  },
  methods: {
    onMoreInfoClicked (cartitem) {
      this.$router.push({ name: 'item', params: { itemId: cartitem.itemId } })
    },
    onItemChanged (item) {
      this.$http.put('cart', {
        item_id: item.itemId,
        selected: item.selected,
        count: item.count
      }, {
        headers: {
          Authorization: window.sessionStorage.getItem('token')
        }
      }).then(() => {})
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="less">
.cart-wrapper{
  width: 100%;
  height: 700px;
}
.cart-item-grid{
  width: 50%;
  height: 200px;
  border: 1px solid rgb(163, 163, 163);
  position: relative;
  left: 50%;
  transform: translate(-50%);
  margin-top: 30px;
}
.cart-item-other-info-container{
  width: 88%;
  height: 100%;
  float: left;
}
.cart-item-checkbox-container{
  width: 5%;
  height: 100%;
  float: left;
}
.cart-item-checkbox{
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  position: relative;
}
.item-image-container{
  width: 30%;
  height: 180px;
  top: 5%;
  position: relative;
  float: left;
  margin-right: 20px;
}
.cart-item-image{
  width: 100%;
  height: 100%;
}
.item-info-container{
  width: 65%;
  height: 180px;
  top: 5%;
  position: relative;
  float: left;
  padding-left: 10px;
}
.item-name{
  width: 100%;
  height: 40px;
}
.item-name span{
  font-size: 22px;
}
.item-info{
  width: 100%;
  height: 50px;
  overflow: hidden;
  color: rgb(156, 156, 156);
}
.item-price-container{
  width: 100%;
  height: 40px;
}
.item-price-container span{
  font-size: 25px;
  color: rgb(219, 3, 3);
}
.item-number-more{
  width: 100%;
  height: 40px;
}
.item-number-container{
  width: 60%;
  height: 40px;
  position: relative;
  float: left;
}
.item-more-info{
  width: 39%;
  height: 40px;
  float: left;
}
.item-number{
  left: 0;
  top: 50%;
  transform: translate(0,-50%);
}
.item-link{
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
}
</style>
