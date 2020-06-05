<template>
  <div class="shop-index-wrapper">
    <header>
      <navbar></navbar>
    </header>

    <div class="shop-aside-name-container">
      <shopaside :shopId="shopId" class="shop-aside-container"></shopaside>
    </div>
    <div class="shop-index-container">
      <div class="shop-info-container">
        <div class="shop-name-container">
          <span>{{ name }}</span>
        </div>
        <div class="shop-info-wrapper">
          <span>商店简介: {{ info }}</span>
        </div>
        <div class="shop-address-container">
          <span>商店地址: {{ address }}</span>
        </div>
        <div class="shop-phone-container">
          <span>联系电话: {{ phone }}</span>
        </div>
      </div>
      <div class="shop-data-container">
        <div class="shop-total-item-number-container">
          <div class="shop-total-item-number-titile">
            <span>
              总商品数
            </span>
          </div>
          <div class="shop-total-item-number">
            <span>{{ items.length }}</span>
          </div>
        </div>
        <div class="shop-total-item-number-container">
          <div class="shop-total-item-number-titile">
            <span>
              总订单数
            </span>
          </div>
          <div class="shop-total-item-number">
            <span>{{ orderNum }}</span>
          </div>
        </div>
        <div class="shop-total-item-number-container">
          <div class="shop-total-item-number-titile">
            <span>
              总评价数
            </span>
          </div>
          <div class="shop-total-item-number">
            <span>{{ reviewNum }}</span>
          </div>
        </div>
      </div>
      <div class="shop-itemList-container">
        <itemgrid :items="items"></itemgrid>
      </div>
    </div>

  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import shopaside from '../../components/shopAside.vue'
import itemgrid from '../../components/itemGrid.vue'
export default {
  components: {
    navbar,
    shopaside,
    itemgrid
  },
  data () {
    return {
      shopId: '',
      phone: '',
      name: '',
      address: '',
      info: '',
      items: [],
      itemIds: '',
      orderNum: 0,
      reviewNum: 0
    }
  },
  methods: {
    onManageClicked () {
      this.$router.push({ name: 'shopManage', params: { shopId: this.shopId } })
    },
    onLogOutClicked () {
      this.$confirm('此操作将退出登录, 是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        window.sessionStorage.clear()
        this.$message({
          type: 'success',
          message: '退出成功!'
        })
        this.$router.push('shop/login')
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消退出'
        })
      })
    }
  },
  mounted: function () {
    this.$http.get('shop', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      this.shopId = response.data.shop_id
      this.name = response.data.name
      this.phone = response.data.phone
      this.address = response.data.address
      this.info = response.data.info
    }).catch(err => {
      console.log(err)
    })

    this.$http.get('items/shop', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      this.items = response.data.items
      this.items.forEach(item => {
        const itemId = item.item_id
        this.$http.get('review/shop', {
          params: { item_id: itemId }
        }).then(response => {
          this.reviewNum += response.data.review_ids.length
        }).catch(err => {
          console.log(err)
        })
      })
    }).catch(err => {
      console.log(err)
    })

    this.$http.get('shop/orders', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      this.orderNum = response.data.orders.length
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less" scoped>
  .shop-index-wrapper{
    width: 100%;
    height: 1500px;
  }
  .shop-index-container{
    width: 88%;
    height: 100%;
    position: absolute;
    right: 0;
  }
  .shop-info-container{
    width: 95%;
    height: 25%;
    border: 1px solid rgb(148, 148, 148);
    border-radius: 1em;
    margin-top: 10px;
    position: relative;
    left: 50%;
    top: 2%;
    transform: translate(-50%);
    padding-left: 10px;
  }
  .shop-data-container{
    width: 95%;
    height: 20%;
    border: 1px solid rgb(148, 148, 148);
    border-radius: 1em;
    margin-top: 10px;
    position: relative;
    left: 50%;
    top: 2%;
    transform: translate(-50%);
  }
  .shop-itemList-container{
    width: 95%;
    height: 60% auto;
    /* border: 1px solid; */
    border-radius: 1em;
    margin-top: 10px;
    position: relative;
    left: 50%;
    top: 2%;
    transform: translate(-50%);
  }
  .shop-name-container{
    width: 100%;
    height: 25%;
    /* border: 1px solid; */
  }
  .shop-name-container span{
    font-size: 25px;
  }
  .shop-info-wrapper{
    width: 100%;
    height: 30%;
    /* border: 1px solid; */
  }
  .shop-info-wrapper span{
    color: rgb(112, 112, 112);
  }
  .shop-address-container{
    width: 100%;
    height: 20%;
    /* border: 1px solid; */
  }
  .shop-phone-container{
    width: 100%;
    height: 20%;
    /* border: 1px solid; */
  }
  .shop-total-item-number-container{
    width: 10%;
    height: 70%;
    border: 1px solid rgb(163, 163, 163);
    border-radius: 1em;
    position: relative;
    left: 20%;
    top: 50%;
    transform: translate(-5%, -50%);
    float: left;
    margin-right: 150px;
  }
  .shop-total-item-number-titile{
    width: 100%;
    height: 30%;
    top: 10%;
    position: relative;
    text-align: center;
  }
  .shop-total-item-number-titile span{
    font-size: 20px;
  }
  .shop-total-item-number{
    width: 100%;
    height: 60%;
    text-align: center;
  }
  .shop-total-item-number span{
    font-size: 30px;
    position: relative;
    top: 25%;
    color: rgb(221, 0, 0);
  }
</style>
