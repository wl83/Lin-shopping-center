<template>
  <div class="item-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="item-info">
      <div class="item-image">
        <el-image
          :src="'data:image;base64,' + item.images[0]"
          class="item-image"
          :fit="fit"></el-image>
      </div>
      <div class="item-info-more">
        <div class="item-name">
          <h1><span>{{ item.name }}</span></h1>
        </div>
        <div class="item-intro">
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae aliquam vel ipsum. Cupiditate, perferendis. Quod esse, est non nisi necessitatibus similique ipsam pariatur sunt eos fuga vel molestiae, tempora dolore.</p>
        </div>
        <div style="height: 20px;"></div>
        <div class="item-stock" style="height: 30px;">
          <p>库存：</p>
        </div>
        <div class="item-sales" style="height: 30px;">
          <p>销量：</p>
        </div>
        <div class="item-stars" style="height: 30px;">
          <p>评价等级：</p>
        </div>
        <div style="height: 20px;"></div>
        <div style="height: 30px;"></div>
        <div class="item-price-buy">
          <div class="item-price">
            <p><span>¥100</span></p>
          </div>
          <div class="item-shop">
            <el-link type="info" icon="el-icon-s-goods" class="shop-link">进入店铺</el-link>
          </div>
          <div class="item-amount">
            <el-input-number size="small" class="item-input-number" v-model="num" @change="handleChange" :min="1" :max="10"></el-input-number>
          </div>
          <div class="item-in-cart">
            <el-button type="primary" class="in-cart-btn">加入购物车</el-button>
          </div>
        </div>
      </div>
    </div>

    <div class="item-remark-title">
      <h1><span>商品评价</span></h1>
    </div>

    <div class="item-remark-container">
      <div class="item-remark">
        <div class="item-avatar-container">
          <el-image
          style="width: 150px; height: 150px"
          :src="url"
          :fit="fit"
          class="item-avatar"
          ></el-image>
          <div style="width: 100%;text-align: center;">
            <span>小明</span>
          </div>
        </div>
        <div class="item-remark-info">
          <div class="item-remark-star">
            <p>评价等级：</p>
          </div>
          <div class="item-review">
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae soluta reiciendis modi quaerat vel dolores eligendi quod atque sequi vitae animi optio voluptatum, quo necessitatibus molestiae. Adipisci quisquam quae temporibus.</p>
          </div>
          <div class="item-time">
            <p>2020-05-01</p>
          </div>
        </div>
      </div>
      <div class="item-remark">

      </div>
      <div class="item-remark">

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
      url: '',
      fit: 'contain'
    }
  }
}
</script>

<style lang="less" scoped>
.item-info{
  width: 100%;
  height: 500px;
  border: 1px solid;
}
.item-info .item-image{
  width: 30%;
  height: 450px;
  border: 1px solid;
  top: 5%;
  left: 3%;
  position: relative;
  float: left;
}
.item-info-more{
  width: 60%;
  height: 450px;
  border: 1px solid;
  top: 5%;
  right: -6%;
  position: relative;
  float: left;
  padding-left: 20px;
  padding-right: 20px;
}
.item-remark-title{
  width: 100%;
  height: 100px;
  border: 1px solid;
  margin-top: 10px;
}
.item-remark-title h1{
  text-align: center;
}
.item-remark-container{

}
.item-image{
  height: 400px;
  width: 100%;
}
.item-image-carousel{
  height: 400px;
  width: 100%;
}
.item-image-carousel-item{
  height: 400px;
  width: 100%;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}
.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
.item-price-buy{
  width: 100%;
  height: 100px;
}
.item-price-buy .item-price{
  width: 200px;
  float: left;
  top: 65%;
  position: absolute;
}
.item-price-buy .item-price p{
  font-size: 50px;
}
.item-shop{
  float: left;
  width: 15%;
  position: relative;
  left: 15%;
  top: 20%;
}
.item-amount{
  float: left;
  position: relative;
  left: 45%;
  top: 10%;
}
.item-in-cart{
  float: left;
  position: relative;
  left: 50%;
  top: 5%;
}
.item-remark{
  width: 95%;
  height: 200px;
  border: 1px solid;
  margin-top: 10px;
  position: relative;
  left: 2.5%;
  padding: 10px 10px 10px 10px;
}
.item-avatar-container{
  width: 20%;
  height: 200px;
  border: 1px solid;
  float: left;
  margin-right: 10px;
}
.item-remark-info{
  width: 78%;
  height: 200px;
  border: 1px solid;
  float: left;
}
.item-avatar{
  left: 50%;
  transform: translate(-50%);
}
</style>
