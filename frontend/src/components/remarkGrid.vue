<template>
  <div class="item-remark">
    <div class="item-avatar-container">
      <el-image
      style="width: 150px; height: 150px"
      :src="url"
      :fit="fit"
      class="item-avatar"
      ></el-image>
      <div style="width: 100%;text-align: center;">
        <span>小明</span>
      </div>
    </div>
    <div class="item-remark-info">
      <div class="item-remark-star">
        <p>评价等级：</p>
      </div>
      <div class="item-review">
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae soluta reiciendis modi quaerat vel dolores eligendi quod atque sequi vitae animi optio voluptatum, quo necessitatibus molestiae. Adipisci quisquam quae temporibus.</p>
      </div>
      <div class="item-time">
        <p>2020-05-01</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.item-remark{
  width: 95%;
  height: 200px;
  border: 1px solid;
  margin-top: 10px;
  position: relative;
  left: 2.5%;
  padding: 10px 10px 10px 10px;
}
.item-avatar-container{
  width: 20%;
  height: 200px;
  border: 1px solid;
  float: left;
  margin-right: 10px;
}
.item-remark-info{
  width: 78%;
  height: 200px;
  border: 1px solid;
  float: left;
}
.item-avatar{
  left: 50%;
  transform: translate(-50%);
}
</style>
