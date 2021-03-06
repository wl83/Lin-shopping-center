import Vue from 'vue'
import { Steps, Step, Dropdown, DropdownMenu, DropdownItem, Card, Tag, Col, Row, Dialog, Container, Aside, Submenu, MenuItemGroup, Table, TableColumn, Button, Form, FormItem, Input, Menu, MenuItem, Link, Message, MessageBox, Select, Option, Upload, Image, Carousel, CarouselItem, InputNumber, Avatar, Drawer, Rate, Progress, Loading, Pagination, Checkbox, CheckboxGroup, Radio, RadioGroup, Divider } from 'element-ui'

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
Vue.use(Container)
Vue.use(Submenu)
Vue.use(Aside)
Vue.use(MenuItemGroup)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Dialog)
Vue.use(Row)
Vue.use(Col)
Vue.use(Tag)
Vue.use(Card)
Vue.use(Dropdown)
Vue.use(DropdownItem)
Vue.use(DropdownMenu)
Vue.use(Step)
Vue.use(Steps)

Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm
