<template>
  <div class="item-review-wrapper">
    <div class="item-review-remark" v-for="(review, index) in reviews" :key="index">
      <div class="item-review-remark-info-container">
        <div class="item-review-remark-star">
          <div class="item-review-remark-star-title-container">
            <div class="item-review-title-container">
              <p>评价等级：</p>
            </div>
            <div class="item-review-star-container">
              <el-rate
                class="item-page-rate"
                v-model="review.star"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}">
              </el-rate>
            </div>
          </div>
        </div>
        <div class="item-review-review">
          <p>{{ review.remark }}</p>
        </div>
        <div class="item-review-time">
          <p>{{ review.createdTime }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['reviews'],
  data () {
    return {
      value: 0
    }
  }
}
</script>

<style lang="less" scoped>
.item-review-wrapper{
  width: 96%;
  height: 100%;
}
.item-review-remark{
  width: 100%;
  height: 30%;
  margin-bottom: 20px;
}
.item-review-remark-info-container{
  width: 100%;
  height: 100%;
  border: 1px solid rgb(180, 180, 180);
  float: left;
}
.item-review-remark-star{
  width: 100%;
  height: 25%;
  border: 1px solid rgb(170, 170, 170);
  border-right: 0px;
  border-bottom: 0px;
}
.item-review-remark-star-title-container{
  width: 90%;
  height: 100%;
  padding-left: 10px;
  padding-right: 10px;
}
.item-review-title-container{
  width: 18%;
  height: 100%;
  float: left;
}
.item-review-star-container{
  width: 75%;
  height: 100%;
  float: left;
}
.item-page-rate{
  top: 50%;
  transform: translate(0, -50%);
  position: relative;
}
.item-review-review{
  width: 97%;
  height: 50%;
  border: 1px solid rgb(190, 190, 190);
  border-right: 0px;
  overflow: hidden;
  padding-left: 10px;
  padding-right: 10px;
}
.item-review-time{
  width: 100%;
  padding-left: 10px;
  padding-right: 10px;
}
</style>
