<template>
  <div class="item-grid">
    <el-card
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
    </el-card>
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
.item-grid{
    width: 100%;
    height: 70%;
    float: left;
  }
  .grid{
    width: 29%;
    height: 100%;
    margin: 20px;
    float: left;
    position: relative;
    margin-top: 90px;
    padding-left: 0;
    padding-top: 10px;
    padding-right: 10px;
  }
  .item-image-grid{
    width: 300px;
    height: 300px;
    left: 50%;
    top: 8%;
    position: relative;
    transform: translate(-50%);
  }
  .item-image{
    width: 300px;
    height: 300px
  }
  .item-price{
    width: 350px;
    height: 100px;
    top: 12%;
    position: relative;
  }
  .item-price .price{
    font-size: 30px;
    float: left;
    top: 50%;
    position: relative;
  }
  .shop-link{
    float: left;
    width: 110px;
    top: 30%;
    position: relative;
    /* transform: translate(-50%); */
  }
  .item-price .stock{
    color: rgb(149, 149, 149);
    width: 100px;
    float: left;
    top: 30%;
    position: absolute;
    margin-left: 20px;
  }
  .in-cart{
    width: 350px;
    height: 70px;
    top: 10%;
    position: relative;
  }
  .in-cart-btn{
    text-align: center;
    width: 110px;
    position: relative;
    left: 50%;
    transform: translate(-50%);
  }
</style>
