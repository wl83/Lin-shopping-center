<template>
  <div class="shop-add-item-wrapper">
    <header>
      <navbar></navbar>
    </header>
    <div class="shop-aside-name-container">
      <shopaside class="shop-aside-container"></shopaside>
    </div>
    <div class="register-grid">
      <div class="register-title">
        <h1 v-if="!updateFlag" style="text-align: center;"><span>添加商品</span></h1>
        <h1 v-if="updateFlag" style="text-align: center;"><span>更新商品</span></h1>
      </div>
      <div style= "height:30px;"></div>
      <div class="register-form">
        <el-form :label-position="labelPosition" label-width="80px" ref="addItemFormRef" :model="addItemForm" :rules="addItemFormRules">
          <el-form-item class="form-item" label="商品名" prop="name">
            <el-input v-model="addItemForm.name" placeholder="请输入商品名" prefix-icon="el-icon-goods"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="商品类别" prop="itemClass">
            <el-input v-model="addItemForm.itemClass" placeholder="请输入商品类别" prefix-icon="el-icon-goods"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="原价" prop="originalPrice">
            <el-input v-model="addItemForm.originalPrice" placeholder="请输入原价" prefix-icon="el-icon-money"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="现价" prop="currentPrice">
            <el-input v-model="addItemForm.currentPrice" placeholder="请输入现价" prefix-icon="el-icon-money"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="库存" prop="inStock">
            <el-input v-model="addItemForm.inStock" placeholder="请输入库存" prefix-icon="el-icon-document-copy"></el-input>
          </el-form-item>
          <el-form-item class="form-item" label="商品简介" prop="inStock">
            <el-input
              type="textarea"
              placeholder="请输入商品简介"
              v-model="addItemForm.info"
              maxlength="100"
              :rows="3"
              show-word-limit
            >
            </el-input>
          </el-form-item>
          <el-form-item class="form-item" label="商品图片">
            <el-upload
              action="https://jsonplaceholder.typicode.com/posts/"
              list-type="picture-card"
              :file-list="addItemForm.imageList"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              :on-change="handleChange"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload">
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
          </el-form-item>
          <el-form-item class="form-item">
            <el-button v-if="!updateFlag" type="success" class="register-btn" @click="onAddItemClicked">添加</el-button>
            <el-button v-if="updateFlag" type="success" class="register-btn" @click="onAddItemClicked">更新</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../../components/navBar.vue'
import shopaside from '../../components/shopAside.vue'
// import { ImageUpload, ImagePreview } from 'vue-image-upload-preview'
export default {
  components: {
    navbar,
    shopaside
    // 'image-preview': ImagePreview,
    // 'image-upload': ImageUpload
  },
  data () {
    return {
      labelPosition: 'right',
      index: -1,
      images: [],
      itemid: '',
      shopId: '',
      updateFlag: false,
      addItemForm: {
        name: '',
        currentPrice: '',
        originalPrice: '',
        info: '',
        inStock: '',
        itemClass: '',
        imageList: []
      },
      addItemFormRules: {
        name: [
          { required: true, message: '请输入名称', trigger: 'blur' }
        ],
        currentPrice: [
          { required: true, message: '请输入现价', trigger: 'blur' }
        ],
        originalPrice: [
          { required: true, message: '请输入原价', trigger: 'blur' }
        ],
        info: [
          { required: true, message: '请输入商品简介', trigger: 'blur' }
        ],
        inStock: [
          { required: true, message: '请输入库存', trigger: 'blur' }
        ],
        itemClass: [
          { required: true, message: '请输入商品类别', trigger: 'blur' }
        ]
      },
      dialogImageUrl: '',
      dialogVisible: false
    }
  },
  methods: {
    addHead () {
      const tmp = []
      this.images.forEach(item => {
        tmp.push({ content: 'data:image/jpeg;base64,' + item, file: {} })
      })
      return tmp
    },
    getBase64 (file) {
      return new Promise(function (resolve, reject) {
        const reader = new FileReader()
        let imgResult = ''
        reader.readAsDataURL(file)
        reader.onload = function () {
          imgResult = reader.result
        }
        reader.onerror = function (error) {
          reject(error)
        }
        reader.onloadend = function () {
          resolve(imgResult)
        }
      })
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    handleChange (file, fileList) {
      this.getBase64(file.raw).then(res => {
        this.images.push(res.replace(/data:image\/[^;]+;base64,/i, ''))
      })
    },
    handleAvatarSuccess (res, file) {
      this.dialogImageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg' || 'image/png' || 'image/jpg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传图片只能是 JPG/PNG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    onAddItemClicked () {
      for (var i = this.images.length; i >= 0; i -= 2) {
        if (i > 0) {
          this.images.pop()
        }
      }
      console.log(this.images.length)
      alert('!!!')
      this.$refs.addItemFormRef.validate(async valid => {
        if (!valid) {
          return
        }
        if (this.images.length === 0) {
          return this.$message.error('至少上传一张图片')
        }
        if (this.$route.query.editType === 'addNewItem') {
          await this.$http.post('item/create', {
            images: this.images,
            name: this.addItemForm.name,
            original_price: this.addItemForm.originalPrice,
            current_price: this.addItemForm.currentPrice,
            in_stock: this.addItemForm.inStock,
            info: this.addItemForm.info,
            item_class: this.addItemForm.itemClass
          },
          {
            headers: {
              Authorization: window.sessionStorage.getItem('shoptoken')
            }
          }).then(() => {
            this.$message('添加成功')
            this.$router.push('/shop')
          }).catch(err => {
            console.log(err)
          })
        } else if (this.$route.query.editType === 'updateOldItem') {
          await this.$http.put('items/' + this.itemId, {
            images: this.images,
            name: this.addItemForm.name,
            original_price: this.addItemForm.originalPrice,
            current_price: this.addItemForm.currentPrice,
            in_stock: this.addItemForm.inStock,
            info: this.addItemForm.info,
            item_class: this.addItemForm.itemClass
          },
          {
            headers: {
              Authorization: window.sessionStorage.getItem('shoptoken')
            }
          }).then(() => {
            this.$message('更新成功')
            this.$router.push('/shop/items')
          }).catch(err => {
            console.log(err)
          })
        }
      })
    }
  },
  mounted: function () {
    if (this.$route.query.editType === 'updateOldItem') {
      this.updateFlag = true
      this.itemId = this.$route.params.itemId

      this.$http.get('items/' + this.itemId, {})
        .then(response => {
          this.addItemForm.name = response.data.name
          this.addItemForm.currentPrice = response.data.current_price
          this.addItemForm.originalPrice = response.data.original_price
          this.addItemForm.inStock = response.data.in_stock
          this.addItemForm.info = response.data.info
          this.shopId = response.data.shop_id
          this.addItemForm.itemClass = response.data.item_class
          this.images = response.data.images
          this.addItemForm.imageList = this.addHead(this.images)
        })
        .catch(err => {
          if (err.response.status === 401) {
            this.$router.push({ name: 'shopLogin' })
          }
          console.error(err)
        })
    }
  }
}
</script>

<style lang="less" scoped>
  .register-grid{
    width: 50%;
    height: 880px;
    position: absolute;
    left: 55%;
    top: 20%;
    transform: translate(-50%, 0);
    border: 1px solid rgb(199, 198, 198);
    padding-left: 50px;
    padding-right: 50px;
    padding-top: 20px;
    padding-bottom: 20px;
    margin-bottom: 100px;
  }
  .form-item{
    margin-bottom: 40px;
  }
  .avatar-uploader{
    width: 100px;
    height: 100px;
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 100px;
    height: 100px;
    line-height: 100px;
    text-align: center;
  }
  .avatar {
    width: 100px;
    height: 100px;
    display: block;
  }
  .register-btn {
    width: 150px;
    position: absolute;
    left: 50%;
    transform: translate(-70%);
  }
  .progress-bar{
    width: 155px;
  }
  /* .image_upload{
    height: 60px;
    width: 60px;
    background: red
  } */
</style>
