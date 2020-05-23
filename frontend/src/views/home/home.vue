<template>
  <div class="home-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="home-grid">
      <div class="left-arrow">
        <el-button class="left-arrow-icon" icon="el-icon-arrow-left"></el-button>
      </div>
      <div class="scroll-pict">
        <itemgrid :items="items"></itemgrid>
      </div>
      <div class="right-arrow">
        <el-button class="right-arrow-icon" icon="el-icon-arrow-right"></el-button>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import itemgrid from '../../components/itemGrid.vue'
export default {
  components: {
    navbar,
    itemgrid
  },
  data () {
    return {
      items: []
    }
  },
  mounted: function () {
    this.$http.get('item/search', {}).then(response => {
      const itemIds = response.data.item_ids

      itemIds.forEach(id => {
        this.$http.get('items/' + id, {}).then(response => {
          const item = {}
          item.name = response.data.name
          item.current_price = response.data.current_price
          item.original_price = response.data.original_price
          item.in_stock = response.data.in_stock
          item.info = response.data.info
          item.sales = response.data.sales
          item.shop_id = response.data.shop_id
          item.images = response.data.images
          item.item_id = id
          this.items.push(item)
        }).catch(err => {
          console.error(err)
        })
      })
    })
  }
}
</script>

<style lang="less" scoped>
.left-arrow{
  position: absolute;
  left: 20px;
  height: 100%;
  width: 50px;
}
.left-arrow-icon{
  position: absolute;
  top: 50%;
  height: 50px;
  border-color: rgb(158, 158, 158);
}
.right-arrow{
  position: absolute;
  height: 100%;
  width: 50px;
  right: 20px;
}
.right-arrow-icon{
  border-color: rgb(158, 158, 158);
  position: absolute;
  top: 50%;
  height: 50px;
}
.scroll-pict{
  width: 1200px;
  height: 100%;
  position: absolute;
  left: 50%;
  transform: translate(-50%);
}

</style>
