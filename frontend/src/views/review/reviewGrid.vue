<template>
  <div class="review-grid-wrapper">
    <div class="review-grid" v-for="(review, index) in reviewList" :key="index">
      <div class="review-remark-container">
        <div class="review-remark">
          <span>{{ review.remark }}</span>
        </div>
        <div class="review-create-time">
          <span>{{ review.createdTime }}</span>
        </div>
      </div>
      <div class="review-star-container">
        <div class="review-star-wrapper">
          <el-rate
          class="review-star"
          v-model="review.star"
          disabled
          show-score
          text-color="#ff9900"
          score-template="{value}">
        </el-rate>
        </div>
        <div class="review-delete-wrapper">
          <el-button @click="onReviewDeleteClicked(review)" type="danger" icon="el-icon-delete" circle></el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['reviewList'],
  data () {
    return {
      star: '',
      customerId: ''
    }
  },
  methods: {
    onReviewDeleteClicked (review) {
      this.$confirm('此操作将删除评论, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$http.delete('review/' + review.reviewId, {
          headers: {
            Authorization: window.sessionStorage.getItem('token')
          }
        }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          this.$router.push('/customer')
        }).catch(err => {
          console.log(err)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  }
}
</script>

<style lang="less" scoped>
.review-grid{
  width: 50%;
  height: 120px;
  border: 1px solid rgb(151, 151, 151);
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 10px;
  padding: 10px 10px 10px 10px;
}
.review-remark-container{
  width: 100%;
  height: 80px;
}
.review-star-container{
  width: 100%;
  height: 38px;
}
.review-star{
  left: 0%;
  top: 50%;
  position: relative;
  transform: translate(0, -50%);
}
.review-remark{
  width: 100%;
  height: 70%;
}
.review-create-time{
  width: 100%;
  height: 20%;
}
.review-create-time span{
  color: rgb(133, 133, 133);
}
.review-star-wrapper{
  width: 88%;
  height: 100%;
  position: relative;
  float: left;
}
.review-delete-wrapper{
  width: 10%;
  height: 100%;
  position: relative;
  float: left;
}
</style>
