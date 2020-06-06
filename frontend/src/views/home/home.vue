<template>
  <div class="home-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="home-grid">
      <div class="left-arrow">
        <el-button @click="onPreClicked" class="left-arrow-icon" icon="el-icon-arrow-left"></el-button>
      </div>
      <div class="scroll-pict">
        <itemgrid :items="items"></itemgrid>
      </div>
      <div class="right-arrow">
        <el-button @click="onNextClicked" class="right-arrow-icon" icon="el-icon-arrow-right"></el-button>
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
      items: [],
      groupIndex: 0
    }
  },
  methods: {
    onPreClicked () {
      if (this.groupIndex === 0) {
        this.$message.warning('不能往前了～')
        return
      }
      this.groupIndex--
      this.getItems(this.groupIndex)
    },
    onNextClicked () {
      this.groupIndex++
      this.getItems(this.groupIndex)
    },
    getItems (groupIndex) {
      this.items = []
      this.$http.get('item/search', {
        params: {
          group_index: groupIndex
        }
      }).then(response => {
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
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted: function () {
    this.getItems(this.groupIndex)
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
