import Vue from 'vue'
import { Button, Form, FormItem, Input, Menu, MenuItem, Link, Message, MessageBox, Select, Option, Upload, Image, Carousel, CarouselItem, InputNumber, Avatar, Drawer, Rate, Progress, Loading, Pagination, Checkbox, CheckboxGroup, Radio, RadioGroup, Divider } from 'element-ui'

Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Link)
Vue.use(Select)
Vue.use(Option)
Vue.use(Upload)
Vue.use(Image)
Vue.use(Carousel)
Vue.use(CarouselItem)
Vue.use(InputNumber)
Vue.use(Avatar)
Vue.use(Drawer)
Vue.use(Rate)
Vue.use(Progress)
Vue.use(Loading)
Vue.use(Pagination)
Vue.component(MessageBox.name, MessageBox)
Vue.use(Checkbox)
Vue.use(CheckboxGroup)
Vue.use(Radio)
Vue.use(RadioGroup)
Vue.use(Divider)

Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm
