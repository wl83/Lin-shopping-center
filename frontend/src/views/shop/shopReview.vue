<template>
  <div class="shop-review-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside :shopId="shopId" class="shop-aside-container"></shopaside>
    </div>
    <div class="shop-order-table-container">
      <el-table
        :data="reviewList"
        style="width: 100%"
        max-height="250">
        <el-table-column
          fixed
          prop="createdTime"
          label="评价日期"
          width="150">
        </el-table-column>
        <el-table-column
          prop="name"
          label="用户"
          width="150">
        </el-table-column>
        <el-table-column
          prop="phone"
          label="联系电话"
          width="150">
        </el-table-column>
        <el-table-column
          prop="itemName"
          label="评价商品"
          width="150">
        </el-table-column>
        <el-table-column
          prop="star"
          label="评价等级"
          width="150">
        </el-table-column>
        <el-table-column
          prop="remark"
          label="评价内容"
          width="450">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import shopaside from '../../components/shopAside.vue'
export default {
  components: {
    navbar,
    shopaside
  },
  data () {
    return {
      reviewList: [],
      shopId: '',
      customerIds: []
    }
  },
  methods: {
    getReviewInfo () {
      this.$http.get('items/shop', {
        headers: {
          Authorization: window.sessionStorage.getItem('shoptoken')
        }
      }).then(response => {
        response.data.items.forEach(item => {
          this.$http.get('review/shop', {
            params: { item_id: item.item_id }
          }).then(response => {
            response.data.review_ids.forEach(reviewId => {
              const reviewTemp = {}
              this.$http.get('review/' + reviewId, {})
                .then(response => {
                  reviewTemp.star = response.data.star
                  reviewTemp.remark = response.data.remark
                  reviewTemp.createdTime = response.data.created_time
                  reviewTemp.itemName = item.name

                  reviewTemp.customerId = response.data.customer_id
                  this.$http.get('customer/' + response.data.customer_id, {})
                    .then(response => {
                      reviewTemp.name = response.data.nickname
                      reviewTemp.phone = response.data.phone
                    }).catch(err => {
                      console.log(err)
                    })
                  this.reviewList.push(reviewTemp)
                }).catch(err => {
                  console.log(err)
                })
            })
          }).catch(err => {
            console.log(err)
          })
        })
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted: function () {
    this.shopId = this.$route.params.shopId
    this.getReviewInfo()
  }
}
</script>

<style lang="less" scoped>
.shop-order-table-container{
    height: 100%;
    width: 86%;
    position: fixed;
    right: 0;
  }
</style>
