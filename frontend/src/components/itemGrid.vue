<template>
  <div class="item-grid">
    <div
    class="grid"
    v-for="(item, index) in items.filter(it => it.name != null)"
    :key="index"
    @click="onItemClicked"
    >
      <div class="item-image-grid">
        <el-image
          :src="'data:image;base64,' + item.images[0]"
          class="item-image"
          :fit="fit"></el-image>
      </div>
      <div class="item-price">
        <el-link type="info" icon="el-icon-s-goods" class="shop-link">进入店铺</el-link>
        <p><span class="price">¥ {{ item.current_price }}</span></p>
        <p><span class="stock">销量: {{ item.in_stock }}</span></p>
      </div>
      <div class="in-cart">
        <el-button type="primary" class="in-cart-btn">加入购物车</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['items'],
  data () {
    return {
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      fit: 'contain',
      current_price: '',
      in_stock: ''
    }
  },
  methods: {
    onItemClicked (item) {
      this.$router.push({ name: 'item', params: { item_id: item.item_id } })
    }
  }
}
</script>

<style lang="less" scoped>

</style>
