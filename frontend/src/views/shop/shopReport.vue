<template>
  <div class="shop-report-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside :shopId="shopId" class="shop-aside-container"></shopaside>
    </div>
    <el-card class="box-card">
      <div id="main" style="width: 750px;height:400px;"></div>
    </el-card>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import shopaside from '../../components/shopAside.vue'
import echarts from 'echarts'
export default {
  components: {
    navbar,
    shopaside
  },
  data () {
    return {
      paymentList: [],
      time: [],
      dateList: [],
      day30: [4, 6, 9, 11],
      shopId: ''
    }
  },
  methods: {
    isLeapYear (fullYear) {
      return (fullYear % 4 === 0 && (fullYear % 100 !== 0 || fullYear % 400 === 0))
    },
    getLastDate (date) {
      date = date.split('/')
      if (parseInt(date[2]) > 1) {
        var temp = parseInt(date[2])
        temp--
        date[2] = temp.toString()
        return date.join('/')
      } else { // 月份需要减一
        if (parseInt(date[1]) > 1) {
          temp = parseInt(date[1])
          temp--
          date[1] = temp.toString()
          var flag = false
          for (var i = 0; i < this.day30.length; i++) {
            if (date[1] === this.day30[i]) {
              flag = true
              break
            }
          }
          if (flag) {
            date[2] = '30'
            return date.join('/')
          } else if (date[1] === '2') {
            if (this.isLeapYear(parseInt(date[0]))) {
              date[2] = '29'
            } else {
              date[2] = '28'
            }
            return date.join('/')
          } else {
            date[2] = '31'
            return date.join('/')
          }
        } else { // 年份需要减一
          date[2] = '31'
          date[1] = '12'
          temp = parseInt(date[0])
          temp--
          date[0] = temp.toString()
          return date.join('/')
        }
      }
    }
  },
  mounted () {
    this.shopId = this.$route.params.shopId
    var date = new Date()
    date = date.toLocaleDateString()
    for (var i = 0; i < 7; i++) {
      date = this.getLastDate(date)
      this.dateList.push(date)
    }
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('main'))

    this.$http.get('shop/report', {
      headers: {
        Authorization: window.sessionStorage.getItem('shoptoken')
      }
    }).then(response => {
      response.data.paymentList.forEach(payment => {
        this.paymentList.push(parseFloat(payment))
      })
    }).then(() => {
      var option = {
        title: {
          text: '周销售统计'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: this.dateList.reverse()
        },
        yAxis: {
          data: []
        },
        series: [{
          name: '销量',
          type: 'bar',
          data: this.paymentList.reverse()
        }]
      }
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less" scoped>
  .box-card{
    width: 80%;
    position: relative;
    left: 15%;
  }
</style>
