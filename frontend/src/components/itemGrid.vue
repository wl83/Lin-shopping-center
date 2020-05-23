<template>
  <div class="item-grid">
    <div class="item-image-grid">
      <el-image
        :src="url"
        class="item-image"
        :fit="cover"></el-image>
    </div>
    <div class="item-price">
      <el-link type="info" icon="el-icon-s-goods" class="shop-link">进入店铺</el-link>
      <p><span class="price">¥100</span></p>
      <p><span class="stock">销量：100</span></p>
    </div>
    <div class="in-cart">
      <el-button type="primary" class="in-cart-btn">加入购物车</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
    }
  }
}
</script>

<style lang="less" scoped>

</style>
