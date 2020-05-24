<template>
  <div class="item-page-container">
    <navbar></navbar>

    <div class="item-page-wrapper">
      <div class="item-page-info-container">
        <div class="item-page-image-container">
            <el-image
              :src="'data:image;base64,' + this.images[0]"
              class="item-page-image"
              :fit="fit"></el-image>
        </div>
        <div class="item-page-intro-container">
          <div class="item-page-name-container">
            <p class="item-page-name"><span>{{ this.name }}</span></p>
          </div>
          <div class="item-page-brief-container">
            <p class="item-page-brief"><span>{{ this.info }}</span></p>
          </div>
          <div class="item-page-stock-container">
            <p class="item-page-stock"><span>库存: {{ this.inStock }}</span></p>
          </div>
          <div class="item-page-sales-container">
            <p class="item-page-sales"><span>销量: {{ this.sales }}</span></p>
          </div>
          <div class="item-page-star-container">
            <div class="item-page-star-title-container">
              <p class="item-page-star"><span>评价等级:</span></p>
            </div>
            <div class="item-page-rate-container">
              <el-rate
                class="item-page-rate"
                v-model="value"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}">
              </el-rate>
            </div>
          </div>
          <div class="item-page-price-buy-container">
            <div class="item-page-price-container">
              <p class="item-page-current-price"><span>¥{{ this.currentPrice }}</span></p>
              <p class="item-page-original-price"><span>¥{{ this.originalPrice }}</span></p>
            </div>
            <div class="item-page-buy-container">
              <div class="item-page-input-number-container">
                <el-input-number class="item-page-input-number" size="small" v-model="num" @change="handleChange" :min="1" label="描述文字"></el-input-number>
              </div>
              <div class="item-page-in-cart-container">
                <el-button class="item-page-in-cart-btn" type="primary">加入购物车</el-button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="item-page-review-container">

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
      num: 1,
      value: 3.7,
      url: '',
      fit: 'contain',
      itemId: '',
      name: '',
      shopId: '',
      currentPrice: '',
      originalPrice: '',
      inStock: '',
      info: '',
      sales: '',
      itemClass: '',
      star: '',
      images: []
    }
  },
  methods: {

  },
  mounted: function () {
    console.log(this.$route.params.itemId)
    this.itemId = this.$route.params.itemId
    this.$http.get('items/' + this.$route.params.itemId, {})
      .then(response => {
        this.name = response.data.name
        this.currentPrice = response.data.current_price
        this.originalPrice = response.data.original_price
        this.inStock = response.data.in_stock
        this.info = response.data.info
        this.sales = response.data.sales
        this.shopId = response.data.shop_id
        this.itemClass = response.data.item_class
        this.images = response.data.images
      })
      .catch(err => {
        console.error(err)
      })
  }
}
</script>

<style lang="less" scoped>
.item-page-wrapper{
  width: 100%;
  height: 700px;
  border: 1px solid;
  padding: 10px 10px 10px 10px;
}
.item-page-info-container{
  width: 50%;
  height: 700px;
  border: 1px solid;
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
  float: left;
}
.item-page-image-container{
  width: 25%;
  height: 25%;
  border: 1px solid;
  left: 50%;
  transform: translate(-50%);
  position: relative;
}
.item-page-image{
  width: 100%;
  height: 100%;
}
.item-page-intro-container{
  width: 100%;
  height: 70%;
  border: 1px solid;
  margin-top: 10px;
}
.item-page-name-container{
  width: 100%;
  height: 15%;
  border: 1px solid;
}
.item-page-brief-container{
  width: 100%;
  height: 30%;
  border: 1px solid;
}
.item-page-stock-container{
  width: 100%;
  height: 10%;
  border: 1px solid;
}
.item-page-sales-container{
  width: 100%;
  height: 10%;
  border: 1px solid;
}
.item-page-star-container{
  width: 100%;
  height: 10%;
  border: 1px solid;
}
.item-page-price-buy-container{
  width: 100%;
  height: 20%;
  border: 1px solid;
}
.item-page-price-container{
  width: 50%;
  height: 100%;
  border: 1px solid;
  float: left;
}
.item-page-buy-container{
  width: 49%;
  height: 100%;
  border: 1px solid;
  float: left;
}
.item-page-input-number-container{
  width: 49%;
  height: 100%;
  border: 1px solid;
  float: left;
}
.item-page-in-cart-container{
  width: 49%;
  height: 100%;
  border: 1px solid;
  float: left;
}
.item-page-input-number{
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  position: relative;
}
.item-page-in-cart-btn{
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  position: relative;
}
.item-page-name span{
  font-size: 30px;
}
.item-page-brief{
  color: rgb(122, 122, 122);
}
.item-page-star-title-container{
  width: 10%;
  height: 100%;
  border: 1px solid;
  float: left;
}
.item-page-rate-container{
  width: 89%;
  height: 100%;
  border: 1px solid;
  float: left;
}
.item-page-rate{
  top: 50%;
  transform: translate(0,-50%);
  position: relative;
}
.item-page-current-price span{
  font-size: 30px;
}
.item-page-original-price span{
  color: rgb(212, 0, 0);
  text-decoration: line-through;
}
.item-page-review-container{
  width: 45%;
  height: 700px;
  border: 1px solid;
  float: left;
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
}
</style>
