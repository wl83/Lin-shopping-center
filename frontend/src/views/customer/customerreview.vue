<template>
  <div class="all-reviews-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="review-grid">
      <div class="review-remark-container">

      </div>
      <div class="review-star-container">
        <el-rate
          class="review-star"
          v-model="value"
          disabled
          show-score
          text-color="#ff9900"
          score-template="{value}">
        </el-rate>
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
      value: 0
    }
  }
}
</script>

<style lang="less" scoped>
.review-grid{
  width: 50%;
  height: 120px;
  border: 1px solid;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  margin-top: 10px;
}
.review-remark-container{
  width: 100%;
  height: 80px;
  border: 1px solid;
}
.review-star-container{
  width: 100%;
  height: 38px;
  border: 1px solid;
}
.review-star{
  left: 5%;
  top: 50%;
  position: relative;
  transform: translate(0, -50%);
}
</style>
