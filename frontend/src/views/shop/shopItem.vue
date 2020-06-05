<template>
  <div class="shop-item-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside class="shop-aside-container"></shopaside>
    </div>
    <div class="shop-item-add-container">
      <div class="shop-item-add-btn-container">
        <el-button @click="onAddNewItemClicked" type="success">添加商品</el-button>
      </div>
    </div>
    <div class="shop-item-table-container">
      <el-table
        class="shop-item-table"
        :data="itemList"
        style="width: 100%">
        <el-table-column
          fixed
          prop="name"
          label="商品名"
          width="120">
        </el-table-column>
        <el-table-column
          prop="itemClass"
          label="商品类别"
          width="100">
        </el-table-column>
        <el-table-column
          prop="originalPrice"
          label="原价"
          width="120">
        </el-table-column>
        <el-table-column
          prop="currentPrice"
          label="现价"
          width="120">
        </el-table-column>
        <el-table-column
          prop="sales"
          label="销量"
          width="120">
        </el-table-column>
        <el-table-column
          prop="inStock"
          label="库存"
          width="120">
        </el-table-column>
        <el-table-column
          prop="info"
          label="商品简介"
          width="300">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="120">
          <template slot-scope="scope">
            <el-button
              @click.native.prevent="updateItem(scope.$index, itemList)"
              type="text"
              size="small">
              更新
            </el-button>
            <el-button
              @click.native.prevent="deleteRow(scope.$index, itemList)"
              type="text"
              size="small">
              移除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import shopaside from '../../components/shopAside.vue'
export default {
  components: {
    navbar,
    shopaside
  },
  data () {
    return {
      itemList: [],
      shopId: ''
    }
  },
  methods: {
    updateItem (index, itemList) {
      this.$router.push({ name: 'addNewItem', params: { itemId: this.itemList[index].itemId }, query: { editType: 'updateOldItem' } })
    },
    deleteRow (index, rows) {
      this.$confirm('此操作将删除商品', '提示', {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$http.delete('items/' + this.itemList[index].itemId, {
          headers: {
            Authorization: window.sessionStorage.getItem('shoptoken')
          }
        }).then(() => {
          this.$message.success('删除成功')
          rows.splice(index, 1)
        })
      }).catch(err => {
        console.log(err)
      })
    },
    onAddNewItemClicked () {
      this.$router.push({ name: 'addNewItem', query: { editType: 'addNewItem' } })
    }
  },
  mounted: function () {
    this.$http.get('items/shop', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      response.data.items.forEach(item => {
        const itemTemp = {}
        itemTemp.itemId = item.item_id
        itemTemp.name = item.name
        itemTemp.currentPrice = item.current_price
        itemTemp.originalPrice = item.original_price
        itemTemp.inStock = item.in_stock
        itemTemp.sales = item.sales
        itemTemp.info = item.info
        itemTemp.itemClass = item.item_class
        this.itemList.push(itemTemp)
      })
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less" scoped>
  .shop-item-table-container{
    height: 100%;
    width: 84%;
    position: fixed;
    right: 0;
  }
  .shop-item-add-container{
    width: 100%;
    height: 100px;
  }
  .shop-item-add-btn-container{
    position: relative;
    left: 57%;
    top: 50%;
    width: 10%;
    height: 50%;
    transform: translate(-50%, -50%);
  }
  .shop-item-table{
    width: 100%;
    height: 100%;
    position: relative;
  }
</style>
