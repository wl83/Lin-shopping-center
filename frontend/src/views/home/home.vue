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
        <itemgrid></itemgrid>
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
