<template>
  <div class="item-grid">
    <div
    class="grid"
    v-for="(item, index) in items.filter(it => it.name != null)"
    :key="index"
    >
      <div class="item-image-grid">
        <el-image
          :src="'data:image;base64,' + item.images[0]"
          class="item-image"
          :fit="fit"
          @click="onItemClicked(item)"></el-image>
      </div>
      <div class="item-price">
        <el-link type="info" icon="el-icon-s-goods" class="shop-link">进入店铺</el-link>
        <p><span class="price">¥ {{ item.current_price }}</span></p>
        <p><span class="stock">销量: {{ item.sales }}</span></p>
      </div>
      <div class="in-cart">
        <el-button @click="onInCartClicked(item)" type="primary" class="in-cart-btn">加入购物车</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['items'],
  data () {
    return {
      fit: 'contain',
      current_price: '',
      in_stock: ''
    }
  },
  methods: {
    onItemClicked (item) {
      this.$router.push({ name: 'item', params: { itemId: item.item_id } })
    },
    onInCartClicked (item) {
      this.$http.post('cart', {
        item_id: item.item_id
      },
      {
        headers: {
          Authorization: window.sessionStorage.getItem('token')
        }
      }).then(() => {
        this.$message.success('成功加入购物车')
      }).catch(err => {
        if (err.response.status === 401) {
          this.$router.replace({ name: 'customerLogin' })
        } else {
          this.$message.error('商品已加入购物车')
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>

</style>
