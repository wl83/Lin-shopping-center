<template>
  <div class="all-orders-container">
    <header>
      <navbar></navbar>
    </header>

    <div class="order-item">
      <div class="order-id-container">

      </div>
      <div class="order-info-container">

      </div>
      <div class="order-more-container">
        <el-button class="order-more" type="primary" plain>查看详情</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
export default {
  navbar
}
</script>

<style lang="less" scoped>

</style>
