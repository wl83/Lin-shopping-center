<template>
  <div class="home-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="home-grid">
      <!-- <div class="left-arrow">
        <el-button @click="onPreClicked" class="left-arrow-icon" icon="el-icon-arrow-left"></el-button>
      </div> -->
      <div class="scroll-pict">
        <itemgrid :items="items"></itemgrid>
      </div>
      <!-- <div class="right-arrow">
        <el-button @click="onNextClicked" class="right-arrow-icon" icon="el-icon-arrow-right"></el-button>
      </div> -->
    </div>
    <div style="height: 100px;"></div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import itemgrid from '../../components/itemGrid.vue'
import axios from 'axios'
export default {
  components: {
    navbar,
    itemgrid
  },
  data () {
    return {
      items: [],
      itemsDisplay: [{}, {}, {}],
      groupIndex: 0
    }
  },
  methods: {
    getItems (groupIndex) {
      this.itemsDisplay = []
      this.itemsDisplay = this.items.splice(groupIndex, groupIndex + 3)
    },
    resolve (response, id) {
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
    },
    reject (err) {
      console.log(err)
    }
  },
  mounted () {
    axios.get('item/search', {})
      .then(response => {
        const itemIds = response.data.item_ids
        for (var i = 0; i < response.data.item_ids.length; i++) {
          this.items.push({})
        }

        itemIds.forEach(itemId => {
          this.$http.get('items/' + itemId, {})
            .then(response => {
              this.resolve(response, itemId)
            })
            .catch(err => {
              this.reject(err)
            })
        })
      })
      .catch(err => {
        console.log(err)
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
.page-container{
  width: 50px;
  height: 50px;
  top: 90%;
  left: 50%;
  transform: translate(-50%);
  position: relative;
  background-color: #76b1f9;
}
.currentPage{
  left: 40%;
  top: 50%;
  transform: translate(0, -50%);
  position: relative;
  color: #fff;
  font-size: 20px;
}
</style>
