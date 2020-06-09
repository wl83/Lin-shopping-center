<template>
  <div class="shop-index-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div style="height: 10px;"></div>
    <div class="shop-index-info-container">
      <el-card class="shop-info-box">
        <div class="shop-index-name-container">
          <span>{{ name }}</span>
        </div>
        <div class="shop-index-desc-container">
          <span>{{ info }}</span>
        </div>
        <div class="shop-index-address-container">
          <i class="el-icon-location-outline"></i>
          <span>{{ address }}</span>
        </div>
        <div class="shop-index-phone-container">
          <span>联系电话: {{ phone }}</span>
        </div>
      </el-card>
    </div>

    <div class="shop-index-itemList-container">
      <itemgrid :items="items"></itemgrid>
    </div>

  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import itemgrid from '../../components/itemGrid.vue'
export default {
  components: {
    navbar,
    itemgrid
  },
  data () {
    return {
      shopId: '',
      name: '',
      info: '',
      address: '',
      phone: '',
      items: []
    }
  },
  mounted () {
    this.shopId = this.$route.params.shopId

    this.$http.get('shops/' + this.shopId, {})
      .then(response => {
        this.name = response.data.name
        this.info = response.data.info
        this.address = response.data.address
        this.phone = response.data.phone
      })
      .catch(err => {
        console.log(err)
      })

    this.$http.get('items/shop/' + this.shopId, {})
      .then(response => {
        this.items = response.data.items
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style lang="less" scoped>
.shop-index-info-container{
  height: 200px;
  width: 100%;
}
.shop-info-box{
  width: 87%;
  position: absolute;
  left: 50%;
  top: 12%;
  padding-left: 50px;
  transform: translate(-50%, -10%);
}
.shop-index-name-container{
  width: 100%;
  height: 70px;
}
.shop-index-name-container span{
  font-size: 30px;
}
.shop-index-desc-container{
  width: 100%;
  height: 100px;
}
.shop-index-desc-container span{
  color: rgb(192, 192, 192);
}
.shop-index-address-container{
  width: 100%;
  height: 40px;
}
.shop-index-phone-container{
  width: 100%;
  height: 30px;
}
.shop-index-itemList-container{
  width: 94%;
  position: absolute;
  left: 50%;
  top: 35%;
  transform: translate(-50%);
}
</style>
