(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0ceeda"],{6219:function(e,r,s){"use strict";s.r(r);var t,a=function(){var e=this,r=e.$createElement,s=e._self._c||r;return s("div",[s("van-field",{attrs:{size:"small",clearable:"",label:"收货人姓名",maxlength:"10",placeholder:"请输入收货人姓名","error-message":e.receiverErrmsg},on:{blur:function(r){e.receiverErrmsg=""}},model:{value:e.receiver,callback:function(r){e.receiver=r},expression:"receiver"}}),s("van-field",{attrs:{size:"small",clearable:"",label:"手机号码",type:"number",maxlength:"11",placeholder:"请输入手机号码","error-message":e.phoneErrmsg},on:{blur:function(r){e.phoneErrmsg=""}},model:{value:e.phone,callback:function(r){e.phone=r},expression:"phone"}}),s("van-field",{attrs:{size:"small",clearable:"",autosize:!0,type:"textarea",rows:"4",label:"收货地址",placeholder:"请输入收货地址","error-message":e.addressErrmsg},on:{blur:function(r){e.addressErrmsg=""}},model:{value:e.address,callback:function(r){e.address=r},expression:"address"}}),s("div",{staticStyle:{padding:"15px"}},[s("van-button",{attrs:{round:"",type:"primary",size:"large"},on:{click:e.onSaveClick}},[e._v("保存地址")]),s("div",{staticStyle:{padding:"5px"}}),"addNewAddr"!=this.$route.query.editType?s("van-button",{attrs:{round:"",type:"danger",size:"large"},on:{click:e.onDeleteClick}},[e._v("删除地址")]):e._e()],1)],1)},n=[],o=(s("e7e5"),s("d399")),i=s("bd86"),d=(s("66b9"),s("b650")),c=(s("7f7f"),s("be7f"),s("565f")),l=s("d722"),u={components:(t={},Object(i["a"])(t,c["a"].name,c["a"]),Object(i["a"])(t,d["a"].name,d["a"]),t),data:function(){return{receiver:"",receiverErrmsg:"",phone:"",phoneErrmsg:"",address:"",addressErrmsg:""}},methods:{onDeleteClick:function(){var e=this;l["b"].delete(l["a"]+"address",{headers:{Authorization:this.$store.state.customer_token},params:{address_id:this.$route.query.address_id}}).then((function(){Object(o["a"])("删除地址成功"),e.$router.go(-1)})).catch((function(r){401==r.response.status&&e.$router.push({name:"login"}),console.error(r)}))},onSaveClick:function(){var e=this;this.receiverErrmsg=this.receiver.length>0?null:"请输入收货人姓名",this.phoneErrmsg=11==this.phone.length?null:"输入电话号码格式错误",this.addressErrmsg=this.address.length>0?null:"请输入地址信息",this.receiverErrmsg||this.phoneErrmsg||this.addressErrmsg||("addNewAddr"==this.$route.query.editType?l["b"].post(l["a"]+"address",{receiver:this.receiver,phone:this.phone,address:this.address},{headers:{Authorization:this.$store.state.customer_token}}).then((function(){Object(o["a"])("地址保存成功"),e.$router.go(-1)})).catch((function(r){401==r.response.status&&e.$router.push({name:"login"}),console.error(r)})):"editOldAddr"==this.$route.query.editType&&l["b"].put(l["a"]+"address",{receiver:this.receiver,phone:this.phone,address:this.address,address_id:this.$route.query.address_id},{headers:{Authorization:this.$store.state.customer_token}}).then((function(){Object(o["a"])("地址保存成功"),e.$router.go(-1)})).catch((function(r){401==r.response.status&&e.$router.push({name:"login"}),console.error(r)})))}},mounted:function(){this.receiver=this.$route.query.receiver,this.phone=this.$route.query.phone,this.address=this.$route.query.address}},h=u,p=s("2877"),m=Object(p["a"])(h,a,n,!1,null,null,null);r["default"]=m.exports}}]);
//# sourceMappingURL=chunk-2d0ceeda.3c997507.js.map