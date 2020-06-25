<template>
  <div class="all-reviews-container">
    <header>
      <navbar></navbar>
    </header>

    <reviewgrid :reviewList="reviewList"></reviewgrid>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import reviewgrid from '../review/reviewGrid.vue'
export default {
  components: {
    navbar,
    reviewgrid
  },
  data () {
    return {
      value: 0,
      customerId: '',
      reviewList: []
    }
  },
  methods: {
    getReview () {
      this.$http.get('review/search', {
        params: {
          customer_id: this.customerId
        }
      }).then(response => {
        const reviewIds = response.data.review_ids

        reviewIds.forEach(reviewId => {
          this.$http.get('review/' + reviewId, {})
            .then(response => {
              const review = {}
              review.reviewId = reviewId
              review.remark = response.data.remark
              review.star = response.data.star > 5 ? 5 : response.data.star
              review.createdTime = response.data.created_time
              this.reviewList.push(review)
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
    this.customerId = this.$route.params.customerId
    this.getReview()
    console.log(this.reviewList)
  }
}
</script>

<style lang="less" scoped>

</style>
