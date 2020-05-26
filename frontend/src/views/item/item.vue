<template>
  <div class="item-page-container">
    <navbar></navbar>

    <div class="item-page-wrapper">
      <div class="item-page-info-container">
        <div class="item-page-image-container">
            <el-image
              :src="'data:image;base64,' + this.images[0]"
              class="item-page-image"
              :fit="fit">
            </el-image>
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
          <!-- <div style="height: 20px;"></div> -->
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
        <!-- <div class="item-page-review-up-container">
          <el-button></el-button>
        </div> -->
        <remarkgrid :reviews="reviews" @childFn="parentFn"></remarkgrid>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import remarkgrid from '../../components/remarkGrid.vue'
export default {
  components: {
    navbar,
    remarkgrid
  },
  data () {
    return {
      num: 1,
      value: 0,
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
      images: [],
      reviews: [],
      logined: false
    }
  },
  methods: {
    parentFn (childData) {
      this.value = childData
    },
    handleChange () {

    }
  },
  mounted: function () {
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
        this.value = response.data.star_value.toFixed(1) > 5 ? 5 : response.data.star_value.toFixed(1)
      })
      .catch(err => {
        console.error(err)
      })
    this.$http.get('review/search', { params: { item_id: this.$route.params.itemId } })
      .then(response => {
        const reviewIds = response.data.review_ids

        reviewIds.forEach(reviewId => {
          this.$http.get('review/' + reviewId, {})
            .then(response => {
              const review = {}
              review.reviewId = response.data.review_id
              review.star = response.data.star > 5 ? 5 : response.data.star
              review.remark = response.data.remark
              review.createdTime = response.data.created_time
              review.customerId = response.data.customer_id
              this.reviews.push(review)
            })
            .catch(err => err)
        })
      })
      .catch(err => err)
    if (window.sessionStorage.getItem('token')) {
      this.$http.get('customer', {
        headers: {
          authorization: window.sessionStorage.getItem('token')
        }
      }).then(() => {
        this.logined = true
      }).catch(() => {})
    }
  }
}
</script>

<style lang="less" scoped>
.item-page-wrapper{
  width: 100%;
  height: 700px;
  padding: 10px 10px 10px 10px;
}
.item-page-info-container{
  width: 50%;
  height: 700px;
  border: 1px solid rgb(189, 189, 189);
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
  float: left;
}
.item-page-image-container{
  width: 25%;
  height: 25%;
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
  height: 72%;
  border: 1px solid rgb(170, 170, 170);
  margin-top: 10px;
}
.item-page-name-container{
  width: 100%;
  height: 15%;
}
.item-page-brief-container{
  width: 100%;
  height: 30%;
  overflow: hidden;
  border-top: 1px solid rgb(189, 189, 189);
  border-bottom: 1px solid rgb(189, 189, 189);
}
.item-page-stock-container{
  width: 100%;
  height: 10%;
}
.item-page-sales-container{
  width: 100%;
  height: 10%;
}
.item-page-star-container{
  width: 100%;
  height: 10%;
}
.item-page-price-buy-container{
  width: 100%;
  height: 15%;
}
.item-page-price-container{
  width: 50%;
  height: 100%;
  float: left;
}
.item-page-buy-container{
  width: 49%;
  height: 100%;
  float: left;
}
.item-page-input-number-container{
  width: 49%;
  height: 100%;
  float: left;
}
.item-page-in-cart-container{
  width: 49%;
  height: 100%;
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
  float: left;
}
.item-page-rate-container{
  width: 89%;
  height: 100%;
  float: left;
}
.item-page-rate{
  top: 50%;
  transform: translate(0,-50%);
  position: relative;
}
.item-page-current-price{
  margin-top: 10px;
  margin-bottom: 0;
}
.item-page-current-price span{
  font-size: 30px;
}
.item-page-original-price{
  margin-top: 0;
  margin-bottom: 0;
}
.item-page-original-price span{
  color: rgb(212, 0, 0);
  text-decoration: line-through;
}
.item-page-review-container{
  width: 45%;
  height: 700px;
  border: 1px solid rgb(167, 167, 167);
  float: left;
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
}
</style>
