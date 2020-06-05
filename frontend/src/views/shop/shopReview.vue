<template>
  <div class="shop-review-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside :shopId="shopId" class="shop-aside-container"></shopaside>
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
  }
}
</script>

<style lang="less" scoped>

</style>
