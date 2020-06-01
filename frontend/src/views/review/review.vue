<template>
  <div class="review-wrapper">
    <header>
      <navbar></navbar>
    </header>

    <div class="review-item-container">
      <cartsubmitgrid :orderList="itemList"></cartsubmitgrid>
    </div>

    <div class="review-container">
      <div class="review-star-container">
        <el-rate class="review-rate" v-model="star" show-text></el-rate>
      </div>
      <div class="review-remark-container">
        <el-input
          class="remark-input"
          type="textarea"
          placeholder="请输入评价内容"
          v-model="remark"
          maxlength="200"
          :rows="7"
          show-word-limit
        >
        </el-input>
      </div>
      <div class="review-submit-container">
        <el-button @click="onReviewSubmitClicked" class="review-submit-btn" type="primary">提交</el-button>
      </div>
    </div>
    <div style="height: 100px;"></div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import cartsubmitgrid from '../../components/cartSubmitGrid.vue'
export default {
  components: {
    navbar,
    cartsubmitgrid
  },
  data () {
    return {
      itemList: [],
      itemId: '',
      star: null,
      remark: null
    }
  },
  methods: {
    onReviewSubmitClicked () {
      this.$http.post('review/create', {
        item_id: this.itemId,
        star: this.star,
        remark: this.remark
      }, {
        headers: {
          Authorization: window.sessionStorage.getItem('token')
        }
      }).then(() => {
        this.$message.success('评价成功')
        this.$router.push('/customer')
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted: function () {
    if (this.$route.params.review_id) {
      this.getReview(this.$route.params.review_id)
    } else if (this.$route.params.itemId) {
      this.itemId = this.$route.params.itemId
      this.$http.get('items/' + this.itemId, {})
        .then(response => {
          const item = {}
          item.name = response.data.name
          item.currentPrice = response.data.current_price
          item.info = response.data.info
          item.shop_id = response.data.shop_id
          item.images = response.data.images
          item.count = response.data.count
          this.itemList.push(item)
        }).catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="less" scoped>
  .review-wrapper{
    height: 700px;
    width: 100%;
  }
  .review-item-container{
    height: 33%;
    width: 100%;
    border-bottom: 1px solid rgb(149, 149, 149);
    position: relative;
    left: 50%;
    transform: translate(-50%);
  }
  .review-container{
    width: 50%;
    height: 40%;
    border: 1px solid rgb(153, 153, 153);
    margin-top: 20px;
    left: 50%;
    transform: translate(-50%);
    position: relative;
    padding-left: 10px;
    padding-right: 10px;
  }
  .review-star-container{
    width: 100%;
    height: 15%;
  }
  .review-rate{
    left: 5%;
    top: 50%;
    position: relative;
    transform: translate(0, -50%);
  }
  .review-remark-container{
    height: 58%;
    width: 100%;
  }
  .remark-input{
    height: 100%;
  }
  .review-submit-container{
    width: 100%;
    height: 20%;
  }
  .review-submit-btn{
    position: relative;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 100px;
  }
</style>
