<template>
  <div class="search-container">
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
      <div class="page-container">
        <el-pagination
          class="page"
          background
          layout="prev, pager, next"
          @prev-click="onPrevChangeClicked"
          @next-click="onNextChangeClicked"
          :page-size="3"
          :total="100">
        </el-pagination>
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
      itemName: '',
      items: [],
      groupIndex: 1,
      rankType: 5
    }
  },
  methods: {
    onPrevChangeClicked () {
      this.search(
        this.itemName,
        this.rankType,
        this.groupIndex - 1
      )
    },
    onNextChangeClicked () {
      this.search(
        this.itemName,
        this.rankType,
        this.groupIndex + 1
      )
    },
    search (searchItem, rankType, groupIndex) {
      // console.log('!!!')
      this.items = []
      this.$http.get('item/search', {
        params: {
          item_name: searchItem,
          rank_type: rankType,
          group_index: groupIndex
        }
      }).then(response => {
        this.itemIds = response.data.item_ids
        this.total = response.data.total
        this.itemIds.forEach(itemId => {
          this.$http.get('items/' + itemId, {})
            .then(response => {
              const item = {}
              item.name = response.data.name
              item.current_price = response.data.current_price
              item.original_price = response.data.original_price
              item.in_stock = response.data.in_stock
              item.info = response.data.info
              item.sales = response.data.sales
              item.shop_id = response.data.shop_id
              item.images = response.data.images
              item.item_id = itemId
              this.items.push(item)
            }).catch(err => {
              console.log(err)
            })
        })
      }).catch(err => {
        console.log(err)
      })
    },
    onSearch () {
      this.search(this.itemName, this.rankType, 0)
    }
  },
  mounted: function () {
    this.itemName = this.$route.query.itemName
    // if (this.$route.query.itemName === '') {
    //   console.log('!!!!!!')
    // // }
    // console.log(this.$route.query.itemName)
    // search
    this.onSearch()
  }
}
</script>

<style lang="less" scoped>
.search-container{
  width: 100%;
  height: 750px;
  position: relative;
}
.home-grid{
  width: 100%;
  height: 100%;
  position: relative;
}
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
  top: 40%;
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
  top: 100%;
  right: 35%;
  position: relative;
  margin-bottom: 50px;
}
/* .page{
  width: 1200px;
  height: 10%;
  position: relative;
  left: 50%;
  top: 100%;
  transform: translate(-20%);
} */
</style>
