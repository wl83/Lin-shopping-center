<template>
  <div class="address-grid-wrapper">
    <div class="address-grid-checkbox-group-container">
      <el-checkbox-group
        class="address-grid-checkbox-group"
        v-model="radio"
        :min="0"
        :max="1"
        @change="onChangeHandler(radio)">
        <el-checkbox class="address-grid-checkbox" v-for="(addr, index) in addrList" :label="index" :key="index">
          <div class="address-grid-name-container">
            <span>{{ addr.name }}</span>
          </div>
          <div class="address-grid-phone-container">
            <span>{{ addr.tel }}</span>
          </div>
          <div class="address-grid-address-container">
            <p>{{ addr.address }}</p>
          </div>
        </el-checkbox>
      </el-checkbox-group>
    </div>
  </div>
</template>

<script>
export default {
  props: ['addrList'],
  data () {
    return {
      checked: true,
      radio: []
    }
  },
  methods: {
    onChangeHandler (radio) {
      this.$emit('childFn', this.addrList[radio])
    }
  }
}
</script>

<style lang="less" scoped>
.address-grid-wrapper{
  width: 100%;
  height: 100%;
}
.address-grid-checkbox-group-container{
  width: 100%;
  height: 100%;
  position: relative;
  padding-left: 20px;
}
.address-grid-checkgroup-group{
  width: 100%;
  height: 100%;
  position: relative;
}
.address-grid-checkbox{
  width: 90%;
  height: 30%;
  position: relative;
  border: 1px solid;
  margin-bottom: 10px;
  padding-top: 10px;
  padding-bottom: 10px;
}
.address-grid-name-container{
  width: 100%;
  height: 20%;
  position: relative;
  margin-bottom: 10px;
}
.address-grid-name-container span{
  font-size: 20px;
}
</style>
