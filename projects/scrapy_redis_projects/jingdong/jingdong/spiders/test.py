#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
product_pettern = re.compile(r'(product: \{[\s\S]*?\};)')

src = """<!DOCTYPE HTML>
<html lang="zh-CN">
<head>
    <!-- shouji -->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>【华为LOK-350】荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏【行情 报价 价格 评测】-京东</title>
    <meta name="keywords" content="HUAWEILOK-350,华为LOK-350,华为LOK-350报价,HUAWEILOK-350报价"/>
    <meta name="description" content="【华为LOK-350】京东JD.COM提供华为LOK-350正品行货，并包括HUAWEILOK-350网购指南，以及华为LOK-350图片、LOK-350参数、LOK-350评论、LOK-350心得、LOK-350技巧等信息，网购华为LOK-350上京东,放心又轻松" />
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="mobile-agent" content="format=xhtml; url=//item.m.jd.com/product/100013116298.html">
    <meta http-equiv="mobile-agent" content="format=html5; url=//item.m.jd.com/product/100013116298.html">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <link rel="canonical" href="//item.jd.com/100013116298.html"/>
        <link rel="dns-prefetch" href="//misc.360buyimg.com"/>
    <link rel="dns-prefetch" href="//static.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img10.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img11.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img13.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img12.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img14.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img30.360buyimg.com"/>
    <link rel="dns-prefetch" href="//pi.3.cn"/>
    <link rel="dns-prefetch" href="//ad.3.cn"/>
    <link rel="dns-prefetch" href="//dx.3.cn"/>
    <link rel="dns-prefetch" href="//c.3.cn"/>
    <link rel="dns-prefetch" href="//d.jd.com"/>
    <link rel="dns-prefetch" href="//x.jd.com"/>
    <link rel="dns-prefetch" href="//wl.jd.com"/>
                        <link rel="stylesheet" type="text/css" href="//misc.360buyimg.com/??jdf/1.0.0/unit/ui-base/5.0.0/ui-base.css,jdf/1.0.0/unit/shortcut/5.0.0/shortcut.css,jdf/1.0.0/unit/myjd/2.0.0/myjd.css,jdf/1.0.0/unit/nav/5.0.0/nav.css,jdf/1.0.0/unit/global-footer/5.0.0/global-footer.css,jdf/1.0.0/unit/service/5.0.0/service.css">
                        <style>
#shop-head [style*="2147483647"] div[hui-mod] {display: none !important;}
#shop-head .j-attent-dialog-wrap{display: none;}
#shop-head .sh-brand-wrap-630128 {
font: 14px/1.5 '\5fae\8f6f\96c5\9ed1', Arial, sans-serif;
height: 110px;
overflow:hidden;
position:relative;
}
#shop-head .sh-brand-wrap-630128 img {
vertical-align: middle;
}
#shop-head .sh-brand-wrap-630128 .sh-brand {
position: relative;
margin: 0 auto;
width: 990px;
overflow:hidden;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-container {
    position: absolute;
    width: 1920px;
    text-align: center;
    left: 50%;
    margin-left: -960px;
    height: 110px;
    overflow: hidden;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-container .sh-hot-content {
    display: inline-block;
    width: fit-content;
    position: relative;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-container .hot-link{
    display: 'inline-block';
    position:absolute;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .shop-name-box {
position: absolute;
top: 50%;
margin-top: -30px;
height: 60px;
left: 190px;
vertical-align: top;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .shop-name-box .shop-name{
font-size: 18px;
color: #333;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .shop-logo-box {
position: absolute;
top: 50%;
margin-top: -40px;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-wrap img {
width: 180px;
height: 60px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .hot-link {
display: 'inline-block';
position:absolute;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .coupons {
position: absolute;
right: 0;
top: 50%;
margin-top: -28px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .coupons .coupon {
float: left;
margin-left: 10px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .follow-me {
display: inline-block;
*display: inline;
*zoom: 1;
padding-left: 24px;
width: 47px;
height: 23px;
line-height: 23px;
color: #000;
font-size: 12px;
background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAABZCAMAAABbssnGAAAA/1BMVEUAAAD///////+xGRqxGRqxGRr////uub2xGRr////uub2xGRr///+xGRr////////uub3uub3uub3////uub2xGRruub3uub3////uub2xGRr////uub2xGRruub3////uub2xGRqxGRqxGRqxGRqxGRr////uub2xGRr////uub3kOTzlQEOzHx/++/vsoqbsmJzoaWz9+Pj78vL03t7y2Njv0dHtyMjqwcHtq6/jrKzNbG3GV1jEUFHmTE+/QEG8Oju1Jie6MjP57+/25ub25eXou7zgpKTblJTpfYHRdHXnX2LIXV3mWFvmU1bBSEnBR0i3KSrWhofVg4O6NDWxIW+2AAAAKHRSTlMAl9DQlkxEREQGBgbw8JtMTNCb1tbWmJa3t7fx8fHv1dXVm5yZmktLhfBmHAAAAn5JREFUWMPtmMdy2zAQhlfFIq3eZVuWi+IkAIu61SVLcu92kvd/logAMcT4tgBPHn2Xf3n5ZmcxWMwQfBKRaJriSNN0NJIAmdwpVeU0B4L9CNUhu+9rDqgeB1yUpbpkPc0vXl+OL0Xg8WbER/zkEndG6WwbT3hPCSDBigfi8fLC4gEvSgA/qxWRWOE9EYiydGWPi/dEIc1yLXvWeE8aeM5kz4zi8fu5/Qw0n7cq/UR5MQo8I6oyH3G3xmt/OGOqQAQSohyu2JkPqQoJgJKob94Jeb9R0pS83UMFrcWiRZXIhXTfQ9s/XJTV3YeCXEnZUuL7WXov6khDnda992LHju+LUbPwnBRqBsjkzyxVzvIgSFYtHapJX3No6XHIRUVLl6Kn+c3rdqctAo83Iz7irm073W04tr0NLGUAgxWPtsfzM4tHvMiAGsulLbHEe2pQYOnIHgfvKcBJKJ5j4NmVPV0Lj9/PxJHamaj0U+BFJ/B0LJX5iLvVcfxumAZ/XoYo20t25m1LBQOgLOrJm22/TZQ0ZW/3BJ+vr5Ya+ZDue6j7B5JFvW6SIMiXlS3lPMgYKjv6uFA1YMeO74sZj2UIjgzJxOImyOydE1XO90CQuiA6XKR8zRHR44iLfhJdmmw2vL6aX4nA482Ij/i+RXtTQqY92rrHeyoAJiv+UI+7OxZ/8SIT4iwHVGKA98QhxrIne3p4TwwyLPuyp4/3ZIDnVPZMCR6/n811oLn+p9JPjBeLVvDXhajMJ+5X874/nDlRIA6mKD8G7Mw/iAomQEXUmyGlw42SpsLul8AdjVyiBNtBTaLLj1D3D6Saet2kgv1cUbZU9r6+Fw2koUEawXvxHzpC3Z34XwtFAAAAAElFTkSuQmCC) 0 0 no-repeat;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .follow-me:hover {
background-position: 0 -33px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-light-bg {
color: #fff;
background-position: 0 -66px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search {
position: absolute;
right: 0;
top: 50%;
margin-top: -32px;
height: 64px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-kw {
margin-right: -6px;
padding-left: 5px;
width: 164px;
height: 32px;
vertical-align: top;
border: 2px solid #000;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-submit {
padding: 0 15px;
border: 0;
height: 38px;
vertical-align: top;
background-color: #000;
color: #fff;
cursor: pointer;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-hw {
padding-top: 5px;
font-size: 12px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-hw .hw-link {
margin-right: 10px;
color: #666;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-black-bg .m-kw {
border-color: #b1191a;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-black-bg .m-submit {
background-color: #b1191a;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-black-bg .m-hw .hw-link {
color: #fff;
}
#shop-head .sh-brand-wrap-630128 .userDefinedArea {
 margin: 0 auto;
}
#shop-head .sh-head-menu-922476 ul,
.sh-head-menu-922476 ol,
.sh-head-menu-922476 dl,
.sh-head-menu-922476 li,
.sh-head-menu-922476 dt,
.sh-head-menu-922476 dd {
margin: 0;
padding: 0;
list-style: none;
}
#shop-head .sh-head-menu-922476 .sh-hd-container {
background-color: #fff;
}
#shop-head .sh-head-menu-922476 a {
text-decoration: none;
color: #666666;
}
#shop-head .sh-head-menu-922476 {
width: 100%;
}
#shop-head .sh-head-menu-922476 .sh-hd-wrap {
font: 14px/1.5 '\5fae\8f6f\96c5\9ed1', Arial, sans-serif;
position: relative;
margin: 0 auto;
height: 40px;
font-size: 14px;
color: #333;
width: 1210px;
}
#shop-head .sh-head-menu-922476 .menu-list {
width: 100%;
height: 40px;
list-style: none;
}
#shop-head .sh-head-menu-922476 .mc {
overflow: visible;
}
#shop-head .sh-head-menu-922476 .menu-list .menu {
float: left;
line-height: 24px;
height: 24px;
padding: 8px 0;
border-radius: 12px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu:hover .arrow,
.sh-head-menu-922476 .menu-list .menu .hover .arrow {
font-size: 0;
line-height: 0;
height: 0;
width: 0;
border-top: 0;
border-left: 5px dashed transparent;
border-right: 5px dashed transparent;
border-bottom: 5px solid #fff;
}
#shop-head .sh-head-menu-922476 .menu-list .menu:hover .main-link,
.sh-head-menu-922476 .menu-list .menu .hover .main-link {
color: #fff !important;
background-color: #333;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .main-link {
position: relative;
z-index: 4;
display: block;
padding: 0 15px;
color: #333;
border-radius: 12px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .home-link {
font-weight:bold;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .arrow {
display: inline-block;
*display: inline;
*zoom: 1;
vertical-align: middle;
margin-left: 10px;
font-size: 0;
line-height: 0;
height: 0;
width: 0;
border-bottom: 0;
border-left: 5px dashed transparent;
border-right: 5px dashed transparent;
border-top: 5px solid #666;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap {
display: none;
position: absolute;
left: 0;
top: 39px;
right: 0;
z-index: 99;
padding: 20px 40px;
border: 1px solid #bebab0;
background-color: rgba(247, 242, 234, 0.9);
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-pannel {
float: left;
padding: 0;
_display: inline;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title {
margin-bottom: 13px;
height: 54px;
line-height: 54px;
border-bottom: dashed 1px #c9c9c9;
padding: 0 20px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-list {
padding: 0 20px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title .sub-tit-link {
font-size: 14px;
font-weight: bold;
color: #333;
line-height: 24px;
display: inline-block;
height: 24px;
padding: 0 10px;
margin-left: -10px;
border-radius: 12px;
min-width: 74px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title .sub-tit-link:hover {
border: solid 1px #e4393c;
color: #e4393c;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .leaf {
font-size: 12px;
height: 26px;
line-height: 26px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .leaf .leaf-link:hover {
color: #c81623;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .all-goods-wrap {
clear: both;
padding-left: 20px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .all-goods-wrap .all-goods-link {
font-weight: bold;
padding-left: 20px;
border: solid 1px #666;
border-radius: 12px;
height: 24px;
line-height: 24px;
padding: 0 10px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu:hover .sub-menu-wrap {
display: block;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .all-goods-link-wrap {
clear: both;
padding: 23px 20px 0;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .all-goods-link {
display: inline-block;
border: solid 1px #666;
height: 24px;
line-height: 24px;
border-radius: 12px;
padding: 0 10px;
margin-left: -10px;
font-weight:bold;
color: #000;
}
#shop-head .sh-head-menu-922476 .s-form {
position: absolute;
top: 8px;
right: 0;
}
#shop-head .sh-head-menu-922476 .s-form .s-inp {
padding: 0 0 0 10px;
width: 130px;
line-height: 22px;
height: 22px;
background-color: #ffffff;
color: #c9c9c9;
vertical-align: top;
outline: none;
border: solid 1px #e1e1e1;
border-top-left-radius: 11px;
border-bottom-left-radius: 11px;
}
#shop-head .sh-head-menu-922476 .s-form .s-submit {
margin-left: -5px;
padding: 0 10px;
border: 0;
height: 24px;
width: 46px;
cursor: pointer;
border-top-right-radius: 11px;
border-bottom-right-radius: 11px;
background:#333 url("//img13.360buyimg.com/cms/jfs/t3121/284/4170076300/1201/43e1ad98/583543d4Nc7e0c1a4.png") no-repeat center;
}</style>
                            <link rel="stylesheet" type="text/css" href="//static.360buyimg.com/item/unite/1.0.102/components/??default/common/common.css,default/main/main.css,default/address/address.css,default/prom/prom.css,default/colorsize/colorsize.css,default/buytype/buytype.css,default/track/track.css,default/suits/suits.css,default/baitiao/baitiao.css,default/o2o/o2o.css,default/summary/summary.css,default/buybtn/buybtn.css,default/crumb/crumb.css,default/fittings/fittings.css,default/detail/detail.css" />
    <link rel="stylesheet" type="text/css" href="//static.360buyimg.com/item/unite/1.0.102/components/??default/contact/contact.css,default/popbox/popbox.css,default/preview/preview.css,default/info/info.css,default/imcenter/imcenter.css,default/jdservice/jdservice.css,default/vehicle/vehicle.css,default/poprent/poprent.css,default/jdservicePlus/jdservicePlus.css,default/jdserviceF/jdserviceF.css" />
        <script charset="gbk">
        var pageConfig = {
            compatible: true,
            product: {
                modules: [
                    'address',
                    'prom',
                    'colorsize',
                    'buytype',
                    'baitiao',
                    'summary',
                    'o2o',
                    'buybtn',
                    'track',
                    'suits',
                    'crumb',
                    'fittings',
                    'detail',
                    'contact',
                    'popbox',
                    'preview',
                    'info',
                    'imcenter',
                    'jdservice',
                    'jdservicePlus',
                    'jdserviceF',
                    'commitments',
                    'gift',
                    'vehicle'                ],
                            imageAndVideoJson: {"mainVideoId":"500127490"},
                        ostime: 1597632529.902,
            skuid: 100013116298,
        skuMarkJson: {"isxg":false,"isJDexpress":false,"isrecyclebag":false,"isSds":false,"isSopJSOLTag":false,"isyy":false,"isPOPDistribution":false,"isSopUseSelfStock":false,"isGlobalPurchase":false,"NosendWMS":false,"isOripack":false,"ispt":false,"unused":false,"pg":false,"isSopWareService":false,"isTimeMark":false,"presale":false},
            name: '荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏',
            skuidkey:'1D0E1F519F13C574A9C1890B7F09BA4F',
            href: '//item.jd.com/100013116298.html',
                        src: 'jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg',
                            imageList: ["jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg","jfs/t1/121777/6/2122/484886/5ec27a37Eb1ce27c7/cfe6e3e6482b572c.jpg","jfs/t1/120414/33/2130/177459/5ec27a36E369ebf5c/42c7e0972b18c878.jpg","jfs/t1/113819/16/7319/71328/5ec27a37Eb37a95e9/4b53e325d49ef1dd.jpg","jfs/t1/123399/27/2081/126919/5ec27a37E208530a6/febac8a84c2692a1.jpg","jfs/t1/121153/9/2143/465712/5ec27a37E9cb1c5dd/f030a7f8272abd01.jpg","jfs/t1/119305/30/7358/90692/5ec29d36Ed04efcf3/0c152bde1ecb5b26.jpg","jfs/t1/117399/1/7576/96607/5ec39e98Ef99c103d/00262b4fec44ca7b.jpg"],
                        cat: [737,794,798],
            forceAdUpdate: '8271',
        brand: 8557,
        pType: 1,
        isClosePCShow: false,
         pTag:424538,                                                 isPop:false,
        venderId:1000000904,
        shopId:'1000000904',
        shopSwitch:true,
                                specialAttrs:["Customize-0","thwa-1","zglx-0","isFzxp-2","SoldOversea-0","sfkc-0","isOverseaPurchase-0","is7ToReturn-1","fxg-1","isCanUseDQ-1","isCanUseJQ-1"],
        recommend : [0,1,2,3,4,5,6,7,8,9],
        easyBuyUrl:"//easybuy.jd.com/skuDetail/newSubmitEasybuyOrder.action",
        qualityLife: "//c.3.cn/qualification/info?skuId=100013116298&pid=100013116298&catId=798",
                colorSize: [{"版本":"X1 50“ 新品惠购","skuId":100007791251,"尺寸":"荣耀智慧屏X1系列"},{"版本":"X1 55“ 央视推荐","skuId":100013116298,"尺寸":"荣耀智慧屏X1系列"},{"版本":"X1 65“ 超值之选","skuId":100013150076,"尺寸":"荣耀智慧屏X1系列"},{"版本":"55“ 超薄金属机身818旗舰芯片","skuId":100007006134,"尺寸":"荣耀智慧屏 系列"},{"版本":"55“  4G超大内存818旗舰芯片","skuId":100005171625,"尺寸":"荣耀智慧屏 系列"},{"版本":"55“ 视频通话震撼音效炫彩灯效","skuId":100004099019,"尺寸":"荣耀智慧屏PRO系列"},{"版本":"55“ 视频通话远场语音超大内存","skuId":100005172199,"尺寸":"荣耀智慧屏PRO系列"}],        warestatus: 1,                         desc: '//cd.jd.com/description/channel?skuId=100013116298&mainSkuId=100013116298&charset=utf-8&cdn=2',
                /**/
                 /**/
                twoColumn: false,                        isCloseLoop:true,                                isBookMvd4Baby: false,        addComments:true,
        mainSkuId:'100013116298',        foot: '//dx.3.cn/footer?type=common_config2',
                                  shangjiazizhi: false        }
        };
                                try {
                        function is_sort_black_list() {
              var jump_sort_list = {"6881":3,"1195":3,"10011":3,"6980":3,"12360":3};
              if(jump_sort_list['737'] == 1 || jump_sort_list['794']==2 || jump_sort_list['798']==3) {
                return false;
              }
              return false;
            }

            function jump_mobile() {
              if(is_sort_black_list()) {
                return;
              }

              var userAgent = navigator.userAgent || "";
              userAgent = userAgent.toUpperCase();
                            if(userAgent == "" || userAgent.indexOf("PAD") > -1) {
                  return;
              }

                            if(window.location.hash == '#m') {
                var exp = new Date();
                exp.setTime(exp.getTime() + 30 * 24 * 60 * 60 * 1000);
                document.cookie = "pcm=1;expires=" + exp.toGMTString() + ";path=/;domain=jd.com";
                                window.showtouchurl = true;
                return;
              }

                            if (/MOBILE/.test(userAgent) && /(MICROMESSENGER|QQ\/)/.test(userAgent)) {
                  var paramIndex = location.href.indexOf("?");
                  window.location.href = "//item.m.jd.com/product/100013116298.html"+(paramIndex>0?location.href.substring(paramIndex,location.href.length):'');
                  return;
              }

                            var jump = true;
              var cook = document.cookie.match(/(^| )pcm=([^;]*)(;|$)/);
              if(cook && cook.length > 2 && unescape(cook[2]) == "1") {
                jump = false;
              }
              var mobilePhoneList = ["IOS","IPHONE","ANDROID","WINDOWS PHONE"];
              for(var i=0, len=mobilePhoneList.length; i<len; i++) {
                if(userAgent.indexOf(mobilePhoneList[i]) > -1) {
                  if(jump) {
                    var paramIndex = location.href.indexOf("?");
                    window.location.href = "//item.m.jd.com/product/100013116298.html"+(paramIndex>0?location.href.substring(paramIndex,location.href.length):'');
                  } else {
                                        window.showtouchurl = true;
                  }
                  break;
                }
              }
            }
            jump_mobile();
        } catch(e) {}
    </script>
    <script src="//misc.360buyimg.com/??jdf/lib/jquery-1.6.4.js,jdf/1.0.0/unit/base/1.0.0/base.js,jdf/1.0.0/unit/trimPath/1.0.0/trimPath.js,jdf/1.0.0/ui/ui/1.0.0/ui.js,jdf/1.0.0/ui/dialog/1.0.0/dialog.js"></script>

            <script type="text/JSConfig" id="J_JSConfig">{
"ART":{},
"BASE":{
"PRICE":{"5G":true},
"RESERVATION":{
"reservedPriceSignal":true
},
"PREVIEW_PRICE":{
"IMAGES":{
"100000":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"100001":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"100002":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"100003":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"100004":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"100005":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"100010":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"900050":"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg"
},
"NOTEXT_IMAGES":[
"//m.360buyimg.com/cc/jfs/t1/4527/32/11268/15520/5bcec10dEbfb8ca48/426e6302a70f2a4d.jpg",
"//m.360buyimg.com/cc/jfs/t1/125100/34/1827/7738/5ebfcad0Ebff2e0b6/b901ff651860bea9.jpg"
]
}
},
"BOOK":{},
"GLOBAL":{
"blackFriImgUrl":"//img11.360buyimg.com/imagetools/jfs/t1/69266/12/15860/24140/5dd773a4E6f6cbee6/05c1fe7f8d00dbeb.png",
"INFORMANT":{
"appId":"2eede73a8409439501dcdb85a971c083512a7af1",
"state":"",
"fu":true,
"iu":true,
"th":{
"bt":5000,
"st":3000,
"wt":3000,
"idt":3000,
"is":3000
}
},
"PLUS":{
"giftPackageSignal":false,
"memberStore":["1000281625","1000076153","1000332823"]
},
"COLORSIZE":{
"itemClickSignal":false
},
"IOU":{"newCheckoutSignal":true}
},
"WORLDBUY":{}
}</script>
        <script>
        seajs.config({
            paths: {
                'MISC' : '//misc.360buyimg.com',
                'PUBLIC_ROOT': '//static.360buyimg.com/item/unite/1.0.102/components/public',
                'MOD_ROOT' : '//static.360buyimg.com/item/unite/1.0.102/components/default',
                'PLG_ROOT' : '//static.360buyimg.com/item/unite/1.0.102/components/default/common/plugins',
                'JDF_UI'   : '//misc.360buyimg.com/jdf/1.0.0/ui',
                'JDF_UNIT' : '//misc.360buyimg.com/jdf/1.0.0/unit'
            },
            alias: {
                "home/widget/mobile_pop": "//nfa.jd.com/loadFa.action?aid=0_0_8762"
            }
        });
    </script>

</head>
<body version="140120" class="clothing cat-1-737 cat-2-794 cat-3-798 cat-4- item-100013116298 JD JD-1">
        <!--shortcut start-->
<div id="shortcut-2014">
	<div class="w">
    	<ul class="fl">
    		<li id="ttbar-home"><i class="iconfont">&#xe608;</i><a href="//www.jd.com/" target="_blank">京东首页</a></li>
    		<li class="dorpdown" id="ttbar-mycity"></li>
    	</ul>
    	<ul class="fr">
			<li class="fore1" id="ttbar-login">
				<a href="javascript:login();" class="link-login">你好，请登录</a>&nbsp;&nbsp;<a href="javascript:regist();" class="link-regist style-red">免费注册</a>
			</li>
			<li class="spacer"></li>
			<li class="fore2">
				<div class="dt">
					<a target="_blank" href="//order.jd.com/center/list.action">我的订单</a>
				</div>
			</li>
			<li class="spacer"></li>
			<li class="fore3 dorpdown" id="ttbar-myjd">
				<div class="dt cw-icon">
					<!-- <i class="ci-right"><s>◇</s></i> -->
					<a target="_blank" href="//home.jd.com/">我的京东</a><i class="iconfont">&#xe605;</i>
				</div>
				<div class="dd dorpdown-layer"></div>
			</li>
			<li class="spacer"></li>
			<li class="fore4" id="ttbar-member">
				<div class="dt">
					<a target="_blank" href="//vip.jd.com/">京东会员</a>
				</div>
			</li>
			<li class="spacer"></li>
			<li class="fore5"   id="ttbar-ent">
				<div class="dt">
					<a target="_blank" href="//b.jd.com/">企业采购</a>
				</div>
			</li>
			<li class="spacer"></li>
			<li class="fore6 dorpdown" id="ttbar-serv">
				<div class="dt cw-icon">
					<!-- <i class="ci-right"><s>◇</s></i> -->
					客户服务<i class="iconfont">&#xe605;</i>
				</div>
				<div class="dd dorpdown-layer"></div>
			</li>
			<li class="spacer"></li>
			<li class="fore7 dorpdown" id="ttbar-navs">
				<div class="dt cw-icon">
					<!-- <i class="ci-right"><s>◇</s></i> -->
					网站导航<i class="iconfont">&#xe605;</i>
				</div>
				<div class="dd dorpdown-layer"></div>
			</li>
			<li class="spacer"></li>
			<li class="fore8 dorpdown" id="ttbar-apps">
				<div class="dt cw-icon">
					<!-- <i class="ci-left"></i> -->
					<!-- <i class="ci-right"><s>◇</s></i> -->
					<a target="_blank" href="//app.jd.com/">手机京东</a>
				</div>
			</li>
    	</ul>
		<span class="clr"></span>
    </div>
</div>
<div id="o-header-2013"><div id="header-2013" style="display:none;"></div></div>
<!--shortcut end-->    <link rel="stylesheet" type="text/css" href="//misc.360buyimg.com/??jdf/1.0.0/unit/global-header/1.0.0/global-header.css,jdf/1.0.0/unit/shoppingcart/2.0.0/shoppingcart.css">
    <style type="text/css">
    #search-2014 .button {
        width: auto;
        padding: 0 8px;
        font:12px simsun;
        overflow:visible;
    }
    #search-2014 .button01 {
        background: #474e5c;
    }
    #search-2014 .text {
        width: 340px;
    }
    #search-2014 .form {
        width: 480px;
    }
    #shelper {
        width: 349px;
    }
    .root61 #search-2014, .root61 #search-2014 .form {
        _width: 560px;
    }
</style>

<div class="w">
    <div id="logo-2014">
        <a href="//www.jd.com/" class="logo" clstag="shangpin|keycount|topitemnormal|d01">京东</a>
        <div class="extra">
            <div id="channel"></div>
            <div id="categorys-mini">
                <div class="cw-icon">
                    <h2><a href="//www.jd.com/allSort.aspx" clstag="shangpin|keycount|topitemnormal|d02">全部分类<i class="ci-right"><s>◇</s></i></a></h2>
                </div>
                <div id="categorys-mini-main">
                    <span class="loading"></span>
                </div>
            </div>
        </div>
    </div>

    <div id="search-2014" >
        <ul id="shelper" class="hide"></ul>
        <div class="form">
            <input type="text" onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off" id="key" accesskey="s" class="text" />
            <button onclick="search('key');return false;" class="button cw-icon" clstag="shangpin|keycount|topitemnormal|d03">搜全站</button>
            <button type="button" class="button button01" clstag="shangpin|keycount|topitemnormal|d04">搜本店</button>
        </div>
    </div>
    <div id="settleup-2014" class="dorpdown">
        <div class="cw-icon">
            <i class="ci-left"></i>
            <i class="ci-right">&gt;</i>
            <a target="_blank" href="//cart.jd.com/cart.action" clstag="shangpin|keycount|topitemnormal|d05">我的购物车</a>
        </div>
        <div class="dorpdown-layer">
            <div class="spacer"></div>
            <div id="settleup-content">
                <span class="loading"></span>
            </div>
        </div>
    </div>
    <div id="hotwords"></div>
    <span class="clr"></span>
    <script>
                (function() {
            //搜本店
            $('.button01').click(function() {
                url = '//mall.jd.com/advance_search-' + 394032 + '-' + pageConfig.product.venderId + '-' + pageConfig.product.shopId + '-0-0-0-1-1-24.html';
                location.href = url + '?keyword=' + encodeURIComponent(encodeURIComponent(jQuery.trim($('#key').val())));
            });
            $(function() {
                $("#navmore").hover(function() {
                    $(this).addClass("hover")
                }, function() {
                    $(this).removeClass("hover")
                });
            });
        })();
        seajs.use('MOD_ROOT/common/vendor/jshop-lib.min');  
        //店铺头 搜索热词
        (function(cfg) {
            function setPlaceholder(val) {
                $('#key').val(val)
                .bind('focus',function(){
                    if (this.value==val){ this.value='';this.style.color='#333' }
                })
                .bind('blur',function(){
                    if (this.value==''){ this.value=val;this.style.color='#999' }
                });
            }
            function render(r) {
                if (!r || !r.length) return;
                var html = '';
                var el = document.getElementById('hotwords')

                for (var i = 0; i < r.length; i++) {
                    var item = r[i];

                    if (i === 0) {
                        setPlaceholder(item.name)
                    } else {
                        html += '<a target="_blank" data-id="'+ item.id +'" href="'+ item.url_info +'">'+ item.name +'</a>'
                    }
                }

                if (el) el.innerHTML = html
            }
            $.ajax({
                url: '//cds.3.cn/hotwords/get',
                data: { cate: cfg.cat.join(',') },
                dataType: 'jsonp',
                success: render
            })
        })(pageConfig.product);
    </script>
</div>    <div id="shop-head" clstag="shangpin|keycount|product|dianputou"></div><!--#shop-head-->
    <textarea id="J_ShopHead" style="display:none;"><div class="layout-area J-layout-area" >
		<div class="layout layout-auto J-layout" name="通栏布局（100%）" id="225425554" prototypeId="20" area="" layout_name="insertLayout" >
			<div class="layout-one" name="main">
				<style type="text/css" >
#shop-head [style*="2147483647"] div[hui-mod] {display: none !important;}
#shop-head .j-attent-dialog-wrap{display: none;}
#shop-head .sh-brand-wrap-630128 {
font: 14px/1.5 '\5fae\8f6f\96c5\9ed1', Arial, sans-serif;
height: 110px;
overflow:hidden;
position:relative;
}
#shop-head .sh-brand-wrap-630128 img {
vertical-align: middle;
}
#shop-head .sh-brand-wrap-630128 .sh-brand {
position: relative;
margin: 0 auto;
width: 990px;
overflow:hidden;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-container {
    position: absolute;
    width: 1920px;
    text-align: center;
    left: 50%;
    margin-left: -960px;
    height: 110px;
    overflow: hidden;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-container .sh-hot-content {
    display: inline-block;
    width: fit-content;
    position: relative;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-container .hot-link{
    display: 'inline-block';
    position:absolute;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .shop-name-box {
position: absolute;
top: 50%;
margin-top: -30px;
height: 60px;
left: 190px;
vertical-align: top;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .shop-name-box .shop-name{
font-size: 18px;
color: #333;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .shop-logo-box {
position: absolute;
top: 50%;
margin-top: -40px;
}
#shop-head .sh-brand-wrap-630128 .sh-hot-wrap img {
width: 180px;
height: 60px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .hot-link {
display: 'inline-block';
position:absolute;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .coupons {
position: absolute;
right: 0;
top: 50%;
margin-top: -28px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .coupons .coupon {
float: left;
margin-left: 10px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .follow-me {
display: inline-block;
*display: inline;
*zoom: 1;
padding-left: 24px;
width: 47px;
height: 23px;
line-height: 23px;
color: #000;
font-size: 12px;
background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAABZCAMAAABbssnGAAAA/1BMVEUAAAD///////+xGRqxGRqxGRr////uub2xGRr////uub2xGRr///+xGRr////////uub3uub3uub3////uub2xGRruub3uub3////uub2xGRr////uub2xGRruub3////uub2xGRqxGRqxGRqxGRqxGRr////uub2xGRr////uub3kOTzlQEOzHx/++/vsoqbsmJzoaWz9+Pj78vL03t7y2Njv0dHtyMjqwcHtq6/jrKzNbG3GV1jEUFHmTE+/QEG8Oju1Jie6MjP57+/25ub25eXou7zgpKTblJTpfYHRdHXnX2LIXV3mWFvmU1bBSEnBR0i3KSrWhofVg4O6NDWxIW+2AAAAKHRSTlMAl9DQlkxEREQGBgbw8JtMTNCb1tbWmJa3t7fx8fHv1dXVm5yZmktLhfBmHAAAAn5JREFUWMPtmMdy2zAQhlfFIq3eZVuWi+IkAIu61SVLcu92kvd/logAMcT4tgBPHn2Xf3n5ZmcxWMwQfBKRaJriSNN0NJIAmdwpVeU0B4L9CNUhu+9rDqgeB1yUpbpkPc0vXl+OL0Xg8WbER/zkEndG6WwbT3hPCSDBigfi8fLC4gEvSgA/qxWRWOE9EYiydGWPi/dEIc1yLXvWeE8aeM5kz4zi8fu5/Qw0n7cq/UR5MQo8I6oyH3G3xmt/OGOqQAQSohyu2JkPqQoJgJKob94Jeb9R0pS83UMFrcWiRZXIhXTfQ9s/XJTV3YeCXEnZUuL7WXov6khDnda992LHju+LUbPwnBRqBsjkzyxVzvIgSFYtHapJX3No6XHIRUVLl6Kn+c3rdqctAo83Iz7irm073W04tr0NLGUAgxWPtsfzM4tHvMiAGsulLbHEe2pQYOnIHgfvKcBJKJ5j4NmVPV0Lj9/PxJHamaj0U+BFJ/B0LJX5iLvVcfxumAZ/XoYo20t25m1LBQOgLOrJm22/TZQ0ZW/3BJ+vr5Ya+ZDue6j7B5JFvW6SIMiXlS3lPMgYKjv6uFA1YMeO74sZj2UIjgzJxOImyOydE1XO90CQuiA6XKR8zRHR44iLfhJdmmw2vL6aX4nA482Ij/i+RXtTQqY92rrHeyoAJiv+UI+7OxZ/8SIT4iwHVGKA98QhxrIne3p4TwwyLPuyp4/3ZIDnVPZMCR6/n811oLn+p9JPjBeLVvDXhajMJ+5X874/nDlRIA6mKD8G7Mw/iAomQEXUmyGlw42SpsLul8AdjVyiBNtBTaLLj1D3D6Saet2kgv1cUbZU9r6+Fw2koUEawXvxHzpC3Z34XwtFAAAAAElFTkSuQmCC) 0 0 no-repeat;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .follow-me:hover {
background-position: 0 -33px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-light-bg {
color: #fff;
background-position: 0 -66px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search {
position: absolute;
right: 0;
top: 50%;
margin-top: -32px;
height: 64px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-kw {
margin-right: -6px;
padding-left: 5px;
width: 164px;
height: 32px;
vertical-align: top;
border: 2px solid #000;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-submit {
padding: 0 15px;
border: 0;
height: 38px;
vertical-align: top;
background-color: #000;
color: #fff;
cursor: pointer;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-hw {
padding-top: 5px;
font-size: 12px;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .m-search .m-hw .hw-link {
margin-right: 10px;
color: #666;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-black-bg .m-kw {
border-color: #b1191a;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-black-bg .m-submit {
background-color: #b1191a;
}
#shop-head .sh-brand-wrap-630128 .sh-brand .for-black-bg .m-hw .hw-link {
color: #fff;
}
#shop-head .sh-brand-wrap-630128 .userDefinedArea {
 margin: 0 auto;
}

</style>





<div onclick="log('shop_03','mall_03','1000000904','19268','630128')" class="fn-clear  sh-brand-wrap-630128" modeId="19268" instanceId="225425557" module-name="new_shop_signs" style="margin-bottom:0px;;margin-bottom: 0px" origin="0" moduleTemplateId="630128"
          >
    <div class="mc" style=";">
		
        
        
		
<div class="j-module" module-function="autoCenter" module-param="{}">
        <div class="userDefinedArea" style="width:1920px" data-title="">
            <div style="height:110px;background:url(//img14.360buyimg.com/cms/jfs/t1/148733/29/3196/108190/5f119116E318f67cd/7d4a453c8f9b4abd.jpg) no-repeat top center;">
	<div style="width:1920px;height:110px;margin:0 auto;position:relative;">
		<div class="j-module" module-function="saleAttent" module-param="{attentType:'vender'}">
			<a href="javascript:;" class="e-attention current" data-id="1000000904" data-state="2" data-type="0" style="width:308px;height:97px;display:block;position:absolute;top:5px;left:311px;font-size:0;">关注店铺</a> <a href="//item.jd.com/100012545868.html" data-state="0" data-type="0" style="width:86px;height:104px;display:block;position:absolute;top:2px;left:627px;"></a> <a href="//item.jd.com/100012545852.html" data-state="0" data-type="0" style="width:89px;height:107px;display:block;position:absolute;top:2px;left:725px;"></a> <a href="//item.jd.com/100014002656.html" data-state="0" data-type="0" style="width:90px;height:105px;display:block;position:absolute;top:3px;left:826px;"></a> <a href="//item.jd.com/100010260254.html" data-state="0" data-type="0" style="width:84px;height:107px;display:block;position:absolute;top:2px;left:927px;"></a> <a href="//item.jd.com/100013309402.html" data-state="0" data-type="0" style="width:83px;height:106px;display:block;position:absolute;top:1px;left:1024px;"></a> <a href="//item.jd.com/100007815187.html" data-state="0" data-type="0" style="width:98px;height:105px;display:block;position:absolute;top:3px;left:1268px;"></a><a href="//item.jd.com/100007851351.html" data-state="0" data-type="0" style="width:115px;height:105px;display:block;position:absolute;top:3px;left:1124px;"></a> <a href="//item.jd.com/100013116298.html" data-state="0" data-type="0" style="width:141px;height:104px;display:block;position:absolute;top:7px;left:1394px;"></a> 
		</div>
	</div>
</div>
<div class="j-module" module-function="saleAttent" module-param="{attentType:'vender'}" style="display:none;">
	<a id="nan-yyyyy" href="javascript:;" class="e-attention" data-id="1000000904" data-state="0" data-type="2">关注店铺dataType2</a> 
</div>
        </div>
    </div>

<script type="text/javascript">
    function importHotZoneData() {
        $.each($('.hot-link'), function(index, item) {
            var pxArray = $(item).attr('px').split(',');
            $(item).css({
                left: pxArray[0] + 'px',
                top: pxArray[1]+ 'px',
                width: pxArray[2] - 2+ 'px',
                height: pxArray[3] - 2+ 'px'
            });
        });
    }
    importHotZoneData();
    function addAttentHtml(){
        var attentHtml = '<div class="j-attent-dialog-wrap">'
                +'<div class="attent-dialog-mask"></div>'
                +'<div class="attent-dialog">'
                +   '<div class="attent-mt">'
                +       '<span class="attent-close"  title="关闭">关闭</span>'
                +       '<span class="attent-title">提示</span>'
                +   '</div>'
                +   '<div class="attent-mc">'
                +       '<div class="attent-con">'
                +           '<span class="attent-msg"></span>'
                +           '<span class="attent-other"></span>'
                +       '</div>'
                +   '</div>'
                +'</div>'
                +'</div><div class="j-attent-tip-wrap attent-tip-wrap"><i></i></div>';

        var jAttWrap = $(".j-attent-dialog-wrap");

        if(jAttWrap.length === 0){
            jAttWrap = $(attentHtml).appendTo("body");
        }
    }
    addAttentHtml();
    function _seacrh_hot_keyword(obj){
        var base_url = "//mall.jd.com/view_search" +  "-394032" + "-1000000904" + "-1000000904"   + "-0-1-0-0-1-1-24.html";
        var keyword = $(obj).html();
        if(keyword){
            keyword = encodeURIComponent(keyword);
            keyword = encodeURIComponent(keyword);
        }else{
            keyword="";
        }
        var url = base_url + "?keyword="+keyword+"&isGlobalSearch=1";
        window.open(url);
    }

    function shop_signs_search(obj){
        var base_url = "//mall.jd.com/view_search" +  "-394032" + "-1000000904" + "-1000000904"   + "-0-1-0-0-1-1-24.html";
        var keyword = $(obj).prev().val();
        if(keyword){
            keyword = encodeURIComponent(keyword);
            keyword = encodeURIComponent(keyword);
        }else{
            keyword="";
        }
        var url = base_url + "?keyword="+keyword+"&isGlobalSearch=1";
        window.open(url);
    }

    $('.m-kw').keydown(function(e){
        if(e.keyCode==13){
            var base_url = "//mall.jd.com/view_search" +  "-394032" + "-1000000904" + "-1000000904"   + "-0-1-0-0-1-1-24.html";
            var keyword = $(this).val();
            if(keyword){
                keyword = encodeURIComponent(keyword);
                keyword = encodeURIComponent(keyword);
            }else{
                keyword="";
            }
            var url = base_url + "?keyword="+keyword+"&isGlobalSearch=1";
            window.open(url);
            return false;
        }
    });

    function _shop_attention(){
        jQuery('#shop-signs-attention').unbind('click');
        jQuery('#shop-signs-attention').click(function() {
            S_ifollow.follow(this);
            var url = "//f-mall.jd.com/rpc/vender/follow";
            url+="?sysName=mall.jd.com&venderId=" +"1000000904";
            jQuery.ajax({
                url:url,
                type : 'GET',
                dataType : 'jsonp',
                //jsonp: 'jsonpCallback',
                success:function (data){
                    S_ifollow.requestSuccess(data);
                },
                error:function(){

                }
            });
        });
    }
    _shop_attention();
</script>

        
    </div>
</div>

<style type="text/css" >
#shop-head .sh-head-menu-922476 ul,
.sh-head-menu-922476 ol,
.sh-head-menu-922476 dl,
.sh-head-menu-922476 li,
.sh-head-menu-922476 dt,
.sh-head-menu-922476 dd {
margin: 0;
padding: 0;
list-style: none;
}
#shop-head .sh-head-menu-922476 .sh-hd-container {
background-color: #fff;
}
#shop-head .sh-head-menu-922476 a {
text-decoration: none;
color: #666666;
}
#shop-head .sh-head-menu-922476 {
width: 100%;
}
#shop-head .sh-head-menu-922476 .sh-hd-wrap {
font: 14px/1.5 '\5fae\8f6f\96c5\9ed1', Arial, sans-serif;
position: relative;
margin: 0 auto;
height: 40px;
font-size: 14px;
color: #333;
width: 1210px;
}
#shop-head .sh-head-menu-922476 .menu-list {
width: 100%;
height: 40px;
list-style: none;
}
#shop-head .sh-head-menu-922476 .mc {
overflow: visible;
}
#shop-head .sh-head-menu-922476 .menu-list .menu {
float: left;
line-height: 24px;
height: 24px;
padding: 8px 0;
border-radius: 12px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu:hover .arrow,
.sh-head-menu-922476 .menu-list .menu .hover .arrow {
font-size: 0;
line-height: 0;
height: 0;
width: 0;
border-top: 0;
border-left: 5px dashed transparent;
border-right: 5px dashed transparent;
border-bottom: 5px solid #fff;
}
#shop-head .sh-head-menu-922476 .menu-list .menu:hover .main-link,
.sh-head-menu-922476 .menu-list .menu .hover .main-link {
color: #fff !important;
background-color: #333;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .main-link {
position: relative;
z-index: 4;
display: block;
padding: 0 15px;
color: #333;
border-radius: 12px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .home-link {
font-weight:bold;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .arrow {
display: inline-block;
*display: inline;
*zoom: 1;
vertical-align: middle;
margin-left: 10px;
font-size: 0;
line-height: 0;
height: 0;
width: 0;
border-bottom: 0;
border-left: 5px dashed transparent;
border-right: 5px dashed transparent;
border-top: 5px solid #666;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap {
display: none;
position: absolute;
left: 0;
top: 39px;
right: 0;
z-index: 99;
padding: 20px 40px;
border: 1px solid #bebab0;
background-color: rgba(247, 242, 234, 0.9);
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-pannel {
float: left;
padding: 0;
_display: inline;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title {
margin-bottom: 13px;
height: 54px;
line-height: 54px;
border-bottom: dashed 1px #c9c9c9;
padding: 0 20px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-list {
padding: 0 20px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title .sub-tit-link {
font-size: 14px;
font-weight: bold;
color: #333;
line-height: 24px;
display: inline-block;
height: 24px;
padding: 0 10px;
margin-left: -10px;
border-radius: 12px;
min-width: 74px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title .sub-tit-link:hover {
border: solid 1px #e4393c;
color: #e4393c;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .leaf {
font-size: 12px;
height: 26px;
line-height: 26px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .leaf .leaf-link:hover {
color: #c81623;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .all-goods-wrap {
clear: both;
padding-left: 20px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .all-goods-wrap .all-goods-link {
font-weight: bold;
padding-left: 20px;
border: solid 1px #666;
border-radius: 12px;
height: 24px;
line-height: 24px;
padding: 0 10px;
}
#shop-head .sh-head-menu-922476 .menu-list .menu:hover .sub-menu-wrap {
display: block;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .all-goods-link-wrap {
clear: both;
padding: 23px 20px 0;
}
#shop-head .sh-head-menu-922476 .menu-list .menu .all-goods-link {
display: inline-block;
border: solid 1px #666;
height: 24px;
line-height: 24px;
border-radius: 12px;
padding: 0 10px;
margin-left: -10px;
font-weight:bold;
color: #000;
}
#shop-head .sh-head-menu-922476 .s-form {
position: absolute;
top: 8px;
right: 0;
}
#shop-head .sh-head-menu-922476 .s-form .s-inp {
padding: 0 0 0 10px;
width: 130px;
line-height: 22px;
height: 22px;
background-color: #ffffff;
color: #c9c9c9;
vertical-align: top;
outline: none;
border: solid 1px #e1e1e1;
border-top-left-radius: 11px;
border-bottom-left-radius: 11px;
}
#shop-head .sh-head-menu-922476 .s-form .s-submit {
margin-left: -5px;
padding: 0 10px;
border: 0;
height: 24px;
width: 46px;
cursor: pointer;
border-top-right-radius: 11px;
border-bottom-right-radius: 11px;
background:#333 url("//img13.360buyimg.com/cms/jfs/t3121/284/4170076300/1201/43e1ad98/583543d4Nc7e0c1a4.png") no-repeat center;
}

</style>





<div onclick="log('shop_03','mall_03','1000000904','18169','922476')" class="fn-clear  sh-head-menu-922476" modeId="18169" instanceId="225425558" module-name="shop_link" style="margin-bottom:0px;;margin-bottom: 0px" origin="0" moduleTemplateId="922476"
          >
    <div class="mc" style=";">
		
        
        
		<div style="height: 40px;overflow: hidden;">
    <div class="j-module" module-function="autoCenter" module-param="{}">
        <div class="userDefinedArea" style="width:1882px" data-title="">
            <div onclick="log('shop_03','mall_03','1000004259','18169','922476')" class="fn-clear sh-head-menu-922476" modeid="18169" instanceid="202428619" module-name="shop_link" style="margin-bottom:0px;" origin="0" moduletemplateid="922476" data-has-point="true">
	<div class="mc">
		<div style="height:40px;overflow:hidden;">
			<div class="j-module" module-function="autoCenter" module-param="{}">
				<div class="userDefinedArea" style="width:1920px;margin:0px auto 0px -38px;" data-title="">
<style type="text/css" >
#shop-head .user_jy47_daohang {width:1920px;height:40px;font-family:microsoft yahei;font-size:16px;color:white;margin:0 auto;}
#shop-head .user_jy47_daohang .mt {display:none;}
#shop-head .user_jy47_daohang .no_display {display:none;}
#shop-head .user_jy47_daohang .l {width:180px;height:40px;float:left;}
#shop-head .user_jy47_daohang .l .s_all {display:block;width:150px;height:40px;overflow:hidden;background:url(//img11.360buyimg.com/cms/g13/M05/12/00/rBEhVFLXagYIAAAAAAAAUfY5SdkAAH-wQP__PgAAABp340.gif) 150px center no-repeat #131313;padding-left:30px;color:white!important;line-height:40px;text-align:left;}
#shop-head .user_jy47_daohang .l .s_box {display:none;width:990px;height:auto;overflow:hidden;background-color:#f8f6f6;}
#shop-head .user_jy47_daohang .l .s_box .fenlei {display:inline;width:990px;height:490px;overflow:hidden;margin:10px 0 0 10px;float:left;}
#shop-head .user_jy47_daohang .l .s_box .fenlei .fl {width:990px;height:35px;overflow:hidden;margin-bottom:10px;}
#shop-head .user_jy47_daohang .l .s_box .fenlei .fl .yiji {display:block;width:100px;height:35px;overflow:hidden;padding:0 10px 0;text-align:left;line-height:35px;font-size:14px;font-weight:blob;color:black;float:left;}
#shop-head .user_jy47_daohang .l .s_box .fenlei .fl .erji {width:800px;height:35px;overflow:hidden;}
#shop-head .user_jy47_daohang .l .s_box .fenlei .fl .erji a {display:block;width:auto;height:35px;overflow:hidden;padding:0 10px;line-height:35px;float:left;font-size:12px;font-family:arial;}
#shop-head .user_jy47_daohang .l .s_box .fenlei .fl .erji a:hover {text-decoration:underline;color:black!important;}
#shop-head .user_jy47_daohang .l .s_box .fenlei .fl:hover {background-color:#eee;}
#shop-head .user_jy47_daohang .l .s_box .s_banner {display:inline;width:320px;height:200px;overflow:hidden;margin:10px 10px 0 0;float:right;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .s_title {width:320px;height:35px;overflow:hidden;border-bottom:1px solid black;line-hieght:25px;font-size:14px;color:black;line-height:30px;font-weight:bold;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .banner_box {width:320px;height:165px;overflow:hidden;margin-top:8px;position:relative;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .banner_box .s_content {width:320px;height:165px;overflow:hidden;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .banner_box .s_content .banner {display:block;width:320px;height:165px;overflow:hidden;float:left;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .banner_box .s_content .banner img {display:block;width:320px;height:165px;overflow:hidden;background:url(//img11.360buyimg.com/cms/g12/M00/06/0F/rBEQYFNFAXcIAAAAAAAk03BOOKwAAEF5wLbSlkAACTr902.gif) no-repeat center center #eee;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .banner_box .s_tabs {width:auto;height:auto;overflow:hidden;position:absolute;bottom:10px;right:10px;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .banner_box .s_tabs span {display:block;width:9px;height:9px;overflow:hidden;background-color:#eee;float:left;margin-left:5px;}
#shop-head .user_jy47_daohang .l .s_box .s_banner .banner_box .s_tabs span.show {background-color:red;}
#shop-head .user_jy47_daohang .l:hover .s_box {display:block;}
#shop-head .user_jy47_daohang .r {width:1100px;height:40px;background-color:black;margin: 0 auto;}
#shop-head .user_jy47_daohang .r .s_nav {height:40px;float:left;}
#shop-head .user_jy47_daohang .r .no_s_nav {display:none;}
#shop-head .user_jy47_daohang .r .s_nav .nav_title {display:block;width:auto;_width:50px;height:40px;padding:0 8px 0;line-height:40px;color:white;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box {display:none;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .menu {width:120px;height:auto;overflow:hidden;padding:5px 15px 10px 15px;float:left;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .menu .s_title {width:100%;height:40px;overflow:hidden;border-bottom:1px solid black;margin-bottom:5px;line-height:40px;font-weight:bold;color:black;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .menu a {display:block;width:auto;height:38px;overflow:hidden;line-height:38px;font-size:12px;color:black;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .menu a:hover {text-decoration:underline;}
#shop-head .user_jy47_daohang .r .s_nav:hover .nav_title {background-color:red;color:white;}
#shop-head .user_jy47_daohang .r .s_nav:hover .nav_box {display:block;width:auto;height:auto;background-color:#fafafa;position:absolute;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items {max-width:425px;height:auto;overflow:hidden;padding:5px 15px 15px 15px;float:left;position:relative;border-left:1px solid #eeeeee;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .s_title {width:100%;height:40px;overflow:hidden;border-bottom:1px solid black;font-weight:bold;color:black;margin-bottom:10px;line-height:40px;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item {display:inline;width:100px;height:auto;overflow:hidden;float:left;margin-left:6px;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item1 {margin-left:0px;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .pic {display:block;width:98px;height:98px;overflow:hidden;border:1px solid #e3e3e3;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .pic img {display:block;width:98px;height:98px;overflow:hidden;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .pic:hover {border-color:red;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .biaoti {width:100px;height:30px;overflow:hidden;line-height:33px;font-size:12px;color:black;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .price {width:100px;height:30px;overflow:hidden;line-height:28px;font-size:11px;font-family:arial;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .price .cu {font-weight:bold;color:red;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .price .yuan {font-size:10px;color:gray;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .price .yuan .jsNum {text-decoration:line-through;}
#shop-head .user_jy47_daohang .r .s_nav .nav_box .s_items .item .buy {display:block;width:62px;height:28px;overflow:hidden;background-color:red;text-align:center;line-height:28px;color:white;font-size:12px;font-family:arial;}
</style>
					<div class="user_header" style="width:1920px;background-color:#000000;">
						<div class="user_jy47_daohang">
							<div class="mc">
								<div class="user_nav_color" style="width:1920px;height:40px;position:absolute;z-index:6;">
<style type="text/css" >
#shop-head .user_nav_erji{display:none;width:1920px;height:240px;z-index:7;background:#red;position:absolute;top:40px;left:0px}
#shop-head .user_hover:hover .user_nav_erji{display:block;}
</style>
									<div class="r" style="background-color:#000000;">
<style type="text/css" >
#shop-head .user_nav_color .l .s_box .s_banner .banner_box .s_tabs span {background-color:#eeeeee;}
#shop-head .user_nav_color .l .s_box .s_banner .banner_box .s_tabs span.show {background-color:#d11e35;}
#shop-head .user_nav_color .r .s_nav:hover .nav_title { background-color:#d11e35;}
#shop-head .user_nav_color .r .s_nav .nav_box .s_items .item .pic:hover { border-color:#65b1ff }
#shop-head .user_nav_color .r .s_nav .nav_box .s_items .item .price .cu { color:#65b1ff;}
</style>
										<div class="l">
											<a class="s_all" href="#" target="_blank" style="background-color:#d11e35;">查看所有商品</a> 
											<div class="s_box">
												<div class="fenlei">
													<div class="fl">
														<a class="yiji" href="#!">荣耀V系列</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100010260254.html" clstag="pageclick|keycount|shop_link_202294379_1|1000000904">荣耀V30PRO</a><a target="_blank" href="//item.jd.com/100010260230.html" clstag="pageclick|keycount|shop_link_202294379_2|1000000904">荣耀V30</a><a target="_blank" href="//item.jd.com/100001864325.html" clstag="pageclick|keycount|shop_link_202294379_3|1000000904">荣耀V20</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">HONOR系列</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100012545868.html" clstag="pageclick|keycount|shop_link_202294379_8|1000000904">荣耀30 Pro</a> <a target="_blank" href="//item.jd.com/100012545852.html" clstag="pageclick|keycount|shop_link_202294379_8|1000000904">荣耀30</a> <a target="_blank" href="//item.jd.com/100014002656.html" clstag="pageclick|keycount|shop_link_202294379_8|1000000904">荣耀30 青春版</a> <a target="_blank" href="//item.jd.com/100006604003.html" clstag="pageclick|keycount|shop_link_202294379_8|1000000904">荣耀30S</a> <a target="_blank" href="//item.jd.com/100004036237.html" clstag="pageclick|keycount|shop_link_202294379_8|1000000904">荣耀20PRO</a> <a target="_blank" href="//item.jd.com/100005603522.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_9|1000000904">荣耀20</a> <a target="_blank" href="//item.jd.com/100004559325.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_10|1000000904">荣耀20S</a> <a target="_blank" href="//item.jd.com/100005207373.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_11|1000000904">荣耀20青春版</a><a target="_blank" href="//item.jd.com/100003060627.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_11|1000000904">荣耀20i</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">荣耀X系列</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100014002946.html" clstag="pageclick|keycount|shop_link_202294379_15|1000000904"> 荣耀X10 Max</a> <a target="_blank" href="//item.jd.com/100013309402.html" clstag="pageclick|keycount|shop_link_202294379_12|1000000904"> 荣耀X10</a> <a target="_blank" href="//item.jd.com/100006947212.html" clstag="pageclick|keycount|shop_link_202294379_12|1000000904"> 荣耀9X</a><a target="_blank" href="//item.jd.com/100006828852.html" clstag="pageclick|keycount|shop_link_202294379_13|1000000904"> 荣耀9XPRO</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">荣耀Play系列</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100013369088.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_24|1000000904"> 荣耀Play4 Pro</a><a target="_blank" href="//item.jd.com/100013525204.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_25|1000000904"> 荣耀Play4</a> <a target="_blank" href="//item.jd.com/100006728101.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_23|1000000904"> 荣耀Play4T Pro</a> <a target="_blank" href="//item.jd.com/100012253152.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_23|1000000904"> 荣耀Play4T</a> <a target="_blank" href="//item.jd.com/100012134984.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_23|1000000904"> 荣耀畅玩9A</a> <a target="_blank" href="//item.jd.com/100008031678.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_23|1000000904"> 荣耀Play3</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">智慧屏</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100007006134.html" clstag="pageclick|keycount|shop_link_202294379_31|1000000904"> 荣耀智慧屏</a> <a target="_blank" href="//item.jd.com/100004099019.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_32|1000000904"> 荣耀智慧屏Pro</a><a target="_blank" href="//item.jd.com/100005171625.html" clstag="pageclick|keycount|shop_link_202294379_31|1000000904"> 荣耀智慧屏4G版</a> <a target="_blank" href="//item.jd.com/100005172199.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_32|1000000904"> 荣耀智慧屏Pro4G版</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">笔记本</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100007818806.html" clstag="pageclick|keycount|shop_link_202294379_33|1000000904">MagicBook pro intel版</a> <a target="_blank" href="//item.jd.com/100004563443.html" clstag="pageclick|keycount|shop_link_202294379_34|1000000904">MagicBook Pro 锐龙版</a> <a target="_blank" href="//item.jd.com/100010816812.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_35|1000000904">MagicBook 14 锐龙版</a> <a target="_blank" href="//item.jd.com/100006229449.html" clstag="pageclick|keycount|shop_link_202294379_36|1000000904">MagicBook 14 intel版</a> <a target="_blank" href="//item.jd.com/100006008837.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_37|1000000904">MagicBook 15 锐龙版</a> <a target="_blank" href="//item.jd.com/100010816646.html" clstag="pageclick|keycount|shop_link_202294379_38|1000000904">MagicBook 15 intel版</a> <a target="_blank" href="//item.jd.com/100004870923.html" clstag="pageclick|keycount|shop_link_202294379_39|1000000904">MagicBook 2019</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">穿戴</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100010206902.html" clstag="pageclick|keycount|shop_link_202294379_40|1000000904">荣耀手表 2</a> <a target="_blank" href="//item.jd.com/100010206886.html" clstag="pageclick|keycount|shop_link_202294379_41|1000000904">荣耀手表</a><a target="_blank" href="//item.jd.com/100006756282.html" clstag="pageclick|keycount|shop_link_202294379_42|1000000904">荣耀手环5 NFC</a><a target="_blank" href="//item.jd.com/100009212514.html" clstag="pageclick|keycount|shop_link_202294379_43|1000000904">荣耀手环5i</a> <a target="_blank" href="//item.jd.com/100002546206.html" clstag="pageclick|keycount|shop_link_202294379_44|1000000904">儿童手表小K2</a> <a target="_blank" href="//item.jd.com/100010109128.html" clstag="pageclick|keycount|shop_link_202294379_45|1000000904">荣耀体脂称 2</a> <a target="_blank" href="//item.jd.com/100000101418.html" clstag="pageclick|keycount|shop_link_202294379_45|1000000904">荣耀手环Running版</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">平板</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100000654489.html" clstag="pageclick|keycount|shop_link_202294379_46|1000000904">平板5 10.1英寸</a> <a target="_blank" href="//item.jd.com/100002244263.html" clstag="pageclick|keycount|shop_link_202294379_47|1000000904">平板5 8英寸</a> <a target="_blank" href="//item.jd.com/4215115.html" clstag="pageclick|keycount|shop_link_202294379_48|1000000904">畅玩平板2 9.6英寸</a> <a target="_blank" href="//item.jd.com/5127282.html" clstag="pageclick|keycount|shop_link_202294379_49|1000000904">畅玩平板2 8英寸</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">路由</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100010173422.html" clstag="pageclick|keycount|shop_link_202294379_53|1000000904">荣耀猎人路由器</a> <a target="_blank" href="//item.jd.com/100002413882.html" clstag="pageclick|keycount|shop_link_202294379_54|1000000904">荣耀路由Pro2</a> <a target="_blank" href="//item.jd.com/100004742552.html" clstag="pageclick|keycount|shop_link_202294379_55|1000000904">荣耀路由X2增强版</a> <a target="_blank" href="//item.jd.com/100000996930.html" clstag="pageclick|keycount|shop_link_202294379_56|1000000904">荣耀路由X2</a> <a target="_blank" href="//item.jd.com/5123258.html" clstag="pageclick|keycount|shop_link_202294379_57|1000000904">荣耀路由X1 增强版</a> <a target="_blank" href="//item.jd.com/5360861.html#crumb-wrap" clstag="pageclick|keycount|shop_link_202294379_58|1000000904">荣耀分布式路由</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">智能家居</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100010297528.html" clstag="pageclick|keycount|shop_link_202294379_61|1000000904">智能摄像头</a> <a target="_blank" href="//item.jd.com/100005944301.html" clstag="pageclick|keycount|shop_link_202294379_62|1000000904">电动牙刷Pro</a> <a target="_blank" href="//item.jd.com/100004885505.html" clstag="pageclick|keycount|shop_link_202294379_63|1000000904">即热饮水吧</a> <a target="_blank" href="//item.jd.com/100004885513.html" clstag="pageclick|keycount|shop_link_202294379_64|1000000904">护眼台灯Pro</a> <a target="_blank" href="//item.jd.com/100010656762.html" clstag="pageclick|keycount|shop_link_202294379_65|1000000904">LED小夜灯</a> <a target="_blank" href="//item.jd.com/100010656742.html" clstag="pageclick|keycount|shop_link_202294379_66|1000000904">手机U盘</a> <a target="_blank" href="//item.jd.com/100005939825.html" clstag="pageclick|keycount|shop_link_202294379_67|1000000904">手机壳</a> 
														</div>
													</div>
													<div class="fl">
														<a class="yiji" href="#!">配件</a> 
														<div class="erji">
															<a target="_blank" href="//item.jd.com/100009211026.html" clstag="pageclick|keycount|shop_link_202294379_71|1000000904">xSport PRO运动耳机</a> <a target="_blank" href="//item.jd.com/100001854373.html " clstag="pageclick|keycount|shop_link_202294379_72|1000000904">FlyPods青春版真无线耳机</a> <a target="_blank" href="//item.jd.com/4635252.html" clstag="pageclick|keycount|shop_link_202294379_73|1000000904">xSport AM61耳机</a> <a target="_blank" href="//item.jd.com/100002582455.html" clstag="pageclick|keycount|shop_link_202294379_74|1000000904">移动电源2</a> <a target="_blank" href="//item.jd.com/100010111510.html" clstag="pageclick|keycount|shop_link_202294379_75|1000000904">AP61无线充电器</a><a target="_blank" href="//item.jd.com/2988013.html" clstag="pageclick|keycount|shop_link_202294379_76|1000000904">AM116耳机</a> <a target="_blank" href="//item.jd.com/100003539713.html" clstag="pageclick|keycount|shop_link_202294379_76|1000000904">魔方蓝牙音箱</a> 
														</div>
													</div>
												</div>
											</div>
										</div>
										<div class="s_nav">
											<a class="nav_title" href="//honor.jd.com/" target="_blank" clstag="pageclick|keycount|shop_link_202294379_77|1000000904">首页</a> 
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/2PimE38Vam99eMLJWXiLTx1VgLJs/index.html" clstag="pageclick|keycount|shop_link_202294379_78|1000000904">V系列</a> 
											<div class="user_nav_erji">
												<img title="V系列.jpg" src="//img14.360buyimg.com/cms/jfs/t1/98686/32/12607/118963/5e4a58cdEb767b0a0/bd20faa04e59758b.png" usemap="#V系列" border="0" /> 
												<map name="V系列" id="V系列">
													<area shape="rect" coords="530,17,742,225" href="//item.jd.com/100010260254.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_79|1000000904" /> 
<area shape="rect" coords="845,18,1096,228" href="//item.jd.com/100010260230.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_80|1000000904" /> 
<area shape="rect" coords="1200,17,1402,228" href="//item.jd.com/100001864325.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_81|1000000904" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/2PimE38Vam99eMLJWXiLTx1VgLJs/index.html" target="blank" clstag="pageclick|keycount|shop_link_202294379_83|1000000904">HONOR系列</a> 
											<div class="user_nav_erji">
												<img title="honor系列.jpg" src="//img13.360buyimg.com/cms/jfs/t1/129229/31/6613/126651/5f067b17E76a868fe/063ee6166b768128.jpg" usemap="#honorxi" border="0" /> 
												<map name="honorxi" id="honorxi">
													<area shape="rect" coords="347,20,518,220" href="//item.jd.com/100012545868.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_85|1000000904" />
<area shape="rect" coords="542,21,716,219" href="//item.jd.com/100012545852.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_86|1000000904" />
								<area shape="rect" coords="758,21,906,216" href="//item.jd.com/100014002656.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_87|1000000904" />
<area shape="rect" coords="961,19,1126,219" href="//item.jd.com/100006604003.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_88|1000000904" />
<area shape="rect" coords="1193,19,1355,226" href="//item.jd.com/100003395441.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_88|1000000904" />
<area shape="rect" coords="1405,22,1563,227" href="//item.jd.com/100005207373.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_88|1000000904" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/2PimE38Vam99eMLJWXiLTx1VgLJs/index.html" clstag="pageclick|keycount|shop_link_202294379_92|1000000904">X系列</a> 
											<div class="user_nav_erji">
												<img src="//img12.360buyimg.com/cms/jfs/t1/150245/36/2381/96862/5f067c95E6565ec42/7d85aee70a55739a.jpg" usemap="#X系列" border="0" /> 
												<map name="X系列" id="X系列">
													<area shape="rect" coords="734,5,950,298" href="//item.jd.com/100014002946.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_93|1000000904" />
													<area shape="rect" coords="521,4,702,235" href="//item.jd.com/100013309402.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_94|1000000904" />
								<area shape="rect" coords="965,8,1176,233" href="//item.jd.com/100006947212.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_94|1000000904" />
<area shape="rect" coords="1196,6,1417,235" href="//item.jd.com/100006828852.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_95|1000000904" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/2PimE38Vam99eMLJWXiLTx1VgLJs/index.html" clstag="pageclick|keycount|shop_link_202294379_102|1000000904">Play系列</a> 
											<div class="user_nav_erji">
												<img src="//img10.360buyimg.com/cms/jfs/t1/121929/12/4234/74206/5ed9f460E6e4b530b/1f7245308badf3e8.jpg" usemap="#Play系列" border="0" /> 
												<map name="Play系列" id="Play系列">
													<area shape="rect" coords="762,14,938,234" href="//item.jd.com/100006728101.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_105|1000000904" /> 
													<area shape="rect" coords="364,23,521,223" href="//item.jd.com/100013369088.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_107|1000000904" /> 
													<area shape="rect" coords="565,21,737,231" href="//item.jd.com/100013525204.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_105|1000000904" />
								<area shape="rect" coords="968,21,1134,234" href="//item.jd.com/100012253152.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_107|1000000904" />
								<area shape="rect" coords="1170,26,1329,237" href="//item.jd.com/100008031678.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_109|1000000904" />
								<area shape="rect" coords="1363,23,1538,238" href="//item.jd.com/100012134984.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_109|1000000904" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/3WQtnQtAMfQuEhLft7BkLJcnD21i/index.html" clstag="pageclick|keycount|shop_link_202294379_112|1000000904">智慧屏</a> 
											<div class="user_nav_erji">
												<img src="//img14.360buyimg.com/cms/jfs/t1/130655/27/4985/350606/5f165783Ee63608cd/27c6f6109700c493.png" usemap="#智慧屏" border="0" /> 
												<map name="智慧屏" id="智慧屏">
													<area shape="rect" coords="968,8,1156,235" href="//item.jd.com/100007006134.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_113|1000000904" />
													<area shape="rect" coords="356,7,550,238" href="//item.jd.com/100007791251.html" target="_blank" />
													<area shape="rect" coords="555,8,749,239" href="//item.jd.com/100013150076.html" target="_blank" />
												  <area shape="rect" coords="1170,13,1358,235" href="//item.jd.com/100004099019.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_114|1000000904" />
<area shape="rect" coords="1374,12,1565,234" href="//item.jd.com/100005171625.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_114|1000000904" /><area shape="rect" coords="1608,18,1805,236" href="//item.jd.com/100005172199.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_114|1000000904" />                                         
												<area shape="rect" coords="753,8,954,236" href="//item.jd.com/100013116298.html" target="_blank" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/SiW9ix69AMqDQ9tVFcYZQntcSvP/index.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_115|1000000904">笔记本</a> 
											<div class="user_nav_erji">
												<img src="//img10.360buyimg.com/cms/jfs/t1/141597/32/3779/131467/5f1bf219E0de508e4/4263e54fa95d5d3b.jpg" alt="" border="0" usemap="#Mapbijiben" /> 
												<map name="Mapbijiben">
													<area shape="rect" coords="334,31,520,226" href="//item.jd.com/100007851351.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_116|1000000904" />
													<area shape="rect" coords="522,31,708,226" href="//item.jd.com/100014190484.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_116|1000000904" />
<area shape="rect" coords="713,29,879,225" href="//item.jd.com/100007852387.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_117|1000000904" />
<area shape="rect" coords="884,31,1055,226" href="//item.jd.com/100014191898.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_118|1000000904" />
<area shape="rect" coords="1062,29,1224,225" href="//item.jd.com/100014190474.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_119|1000000904" />
<area shape="rect" coords="1229,32,1395,224" href="//item.jd.com/100013171828.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" /><area shape="rect" coords="1403,27,1565,225" href="//item.jd.com/100007187885.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/2kNJSZotAF8vsKFqWDtcGvYSL7tK/index.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_121|1000000904"> 穿戴</a> 
											<div class="user_nav_erji">
												<img src="//img13.360buyimg.com/cms/jfs/t1/103893/7/16443/65923/5e7d7323E094b1ed4/ce6bb68eff328366.jpg" alt="" border="0" usemap="#Mapchuandai" /> 
												<map name="Mapchuandai">
													<area shape="rect" coords="338,27,524,222" href="//item.jd.com/100010206902.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_116|1000000904" />
<area shape="rect" coords="530,25,696,221" href="//item.jd.com/100010206886.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_117|1000000904" />
<area shape="rect" coords="702,26,873,221" href="//item.jd.com/100006756282.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_118|1000000904" />
<area shape="rect" coords="879,25,1041,221" href="//item.jd.com/100000970765.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_119|1000000904" />
<area shape="rect" coords="1049,26,1215,218" href="//item.jd.com/100009212514.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
<area shape="rect" coords="1220,24,1370,220" href="//item.jd.com/100002546206.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
<area shape="rect" coords="1374,23,1562,220" href="//item.jd.com/100010109128.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/gFg5uUZmCCVEV52KQ8LzsDtBCc1/index.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_129|1000000904">平板</a> 
											<div class="user_nav_erji">
												<img src="//img11.360buyimg.com/cms/jfs/t1/147562/19/3166/108200/5f1110a8E80d7125c/de2a93e0c0f34af4.jpg" alt="" border="0" usemap="#Mappingban" /> 
												<map name="Mappingban">
													<area shape="rect" coords="564,35,782,225" href="//item.jd.com/100014226800.html" target="_blank" />
												  <area shape="rect" coords="972,32,1193,219" href="//item.jd.com/100013843488.html" />
<area shape="rect" coords="794,30,965,225" href="//item.jd.com/100002244263.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_118|1000000904" />
<area shape="rect" coords="335,31,550,227" href="//item.jd.com/100013315044.html" />
												<area shape="rect" coords="1199,29,1399,222" href="//item.jd.com/100013843506.html" />
												<area shape="rect" coords="1407,31,1574,224" href="//item.jd.com/100007592959.html" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/3yiXHf9ZzEQ2ojYSi4tK9kq8fqr2/index.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_137|1000000904">路由</a> 
											<div class="user_nav_erji">
												<img src="//img13.360buyimg.com/cms/jfs/t1/141713/11/493/52885/5ee32091E3e631e59/9bc543724098dccc.jpg" alt="" border="0" usemap="#Mapluyou" /> 
												<map name="Mapluyou">
													<area shape="rect" coords="1017,15,1189,235" href="//item.jd.com/100010173422.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_116|1000000904" />
<area shape="rect" coords="1197,16,1379,239" href="//item.jd.com/100002413882.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_117|1000000904" />
<area shape="rect" coords="1386,10,1565,237" href="//item.jd.com/100004742552.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_118|1000000904" />
<area shape="rect" coords="351,3,585,241" href="//item.jd.com/100007155439.html" />
											  <area shape="rect" coords="591,3,810,236" href="//item.jd.com/100013213792.html" />
											  <area shape="rect" coords="822,7,1012,238" href="//item.jd.com/100007208701.html" target="_blank" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/eqZF46ybnWkryXE68wrCwufKQEZ/index.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_145|1000000904">智能家居</a> 
											<div class="user_nav_erji">
												<img src="//img10.360buyimg.com/cms/jfs/t1/136648/4/394/44390/5eccd664E9b65758b/0c254805af308010.jpg" alt="" border="0" usemap="#Mapqinxuan" /> 
												<map name="Mapqinxuan">
													<area shape="rect" coords="339,25,525,220" href="//item.jd.com/100013292050.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_116|1000000904" />
<area shape="rect" coords="530,25,696,221" href="//item.jd.com/100007180075.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_117|1000000904" />
<area shape="rect" coords="704,24,875,219" href="//item.jd.com/100007293461.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_118|1000000904" />
<area shape="rect" coords="879,25,1041,221" href="//item.jd.com/100005944301.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_119|1000000904" />
<area shape="rect" coords="1049,26,1215,218" href="//item.jd.com/100010297528.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" /><area shape="rect" coords="1220,24,1370,220" href="//item.jd.com/100011793872.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
<area shape="rect" coords="1374,23,1562,220" href="//item.jd.com/100012889532.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
												</map>
											</div>
										</div>
										<div class="s_nav user_hover">
											<a class="nav_title" href="//pro.jd.com/mall/active/3xknWQgQF6LAFXh6EX3xxEDype4H/index.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_153|1000000904">音频配件</a> 
											<div class="user_nav_erji">
												<img src="//img13.360buyimg.com/cms/jfs/t1/110002/11/8518/74741/5e69e2c0E89e058d8/310494b489c3df40.jpg" alt="" border="0" usemap="#Mappeijian" /> 
												<map name="Mappeijian">
													<area shape="rect" coords="338,27,524,222" href="//item.jd.com/100011463172.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_116|1000000904" />
<area shape="rect" coords="533,28,682,223" href="//item.jd.com/100009211026.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_117|1000000904" />
<area shape="rect" coords="694,25,855,224" href="//item.jd.com/100001854373.html#crumb-wrap" target="_blank" clstag="pageclick|keycount|shop_link_202294379_118|1000000904" />
<area shape="rect" coords="869,26,1021,222" href="//item.jd.com/4635252.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_119|1000000904" />
<area shape="rect" coords="1030,25,1211,222" href="//item.jd.com/100002582453.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
<area shape="rect" coords="1216,28,1382,223" href="//item.jd.com/100010111510.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
<area shape="rect" coords="1386,28,1552,225" href="//item.jd.com/100003539713.html" target="_blank" clstag="pageclick|keycount|shop_link_202294379_120|1000000904" />
												</map>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
        </div>
    </div>
</div>


        
    </div>
</div>


			</div>
		</div>
	</div></textarea>
<script>
    (function(cfg) {
        var $nav1 = $('#navitems-group1');
        var $nav2 = $('#navitems-group2');
        var html = '<li class="fore1" id="nav-home"> <a href="//www.jd.com/">首页</a> </li>';

        if (cfg.cmsNavigation && cfg.cmsNavigation.length && $nav1.length) {
            $nav2.html('');
            var corner_class = "";
            var corner_i="";
            for (var i = 0; i < cfg.cmsNavigation.length; i++) {
                var nav = cfg.cmsNavigation[i];
                if(nav.corner&&nav.corner!=""){
                    corner_class = "new-tab";
                    corner_i="<i class='icon-new'>"+nav.corner+"<span></span></i>";
                }else{
                    corner_class="";
                    corner_i="";
                }
                var j = i + 3;
                if(j.toString().length == 1) {
                    j = "0" + j;
                }
                html += '<li class="fore'+ i +' '+corner_class+'" clstag="shangpin|keycount|topitemnormal|c' + j + '">'+corner_i+'<a href="'+ nav.address +'" target="_blank">'+ nav.name +'</a> </li>';
            }

            $nav1.html(html);
        }
    })(pageConfig.product);
</script>

<div class="crumb-wrap" id="crumb-wrap">
    <div class="w">
                <div class="crumb fl clearfix">
                        <div class="item first"><a href='//jiadian.jd.com' clstag="shangpin|keycount|product|mbNav-1">家用电器</a></div>
            <div class="item sep">&gt;</div>
                        <div class="item"><a href='//list.jd.com/list.html?cat=737,794' clstag="shangpin|keycount|product|mbNav-2">大 家 电</a></div>
            <div class="item sep">&gt;</div>
                        <div class="item"><a href='//list.jd.com/list.html?cat=737,794,798' clstag="shangpin|keycount|product|mbNav-3">平板电视</a></div>
            <div class="item sep">&gt;</div>
                                                <div class="item">
                                <div class="J-crumb-br crumb-br EDropdown">
                    <div class="inner border">
                        <div class="head" data-drop="head">
                            <a href='//list.jd.com/list.html?cat=737,794,798&ev=exbrand_8557' clstag="shangpin|keycount|product|mbNav-5">华为（HUAWEI）</a>
                            <span class="arrow arr-close"></span>
                        </div>
                        <div class="content hide" data-drop="content">
                                                        <ul class="br-reco plist-1 lh clearfix" clstag="shangpin|keycount|product|mbTJ-1"></ul>
                                                        <ul class="br-list" clstag="shangpin|keycount|product|mbTJ-2">
                                                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_18374" target='_blank' title="小米（MI）">小米（MI）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_7888" target='_blank' title="海信（Hisense）">海信（Hisense）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_2505" target='_blank' title="TCL">TCL</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_5565" target='_blank' title="创维（Skyworth）">创维（Skyworth）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_8557" target='_blank' title="华为（HUAWEI）">华为（HUAWEI）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_10317" target='_blank' title="康佳（KONKA）">康佳（KONKA）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_20710" target='_blank' title="长虹（CHANGHONG）">长虹（CHANGHONG）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_7817" target='_blank' title="海尔（Haier）">海尔（Haier）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798&ev=exbrand_53513" target='_blank' title="酷开（coocaa）">酷开（coocaa）</a></li>
                                                                                                <li><a href="//list.jd.com/list.html?cat=737,794,798" target='_blank' title="更多">更多>></a></li>
                                                                                            </ul>
                        </div>
                    </div>
                </div>
                            </div>
            <div class="item sep">&gt;</div>
                        <div class="item ellipsis" title="华为LOK-350">华为LOK-350</div>
        </div><!-- .crumb -->
                        <div class="contact fr clearfix">
                            <div class="name goodshop EDropdown">
                    <em class="u-jd">
                        自营
                    </em>
                </div>
                        <div class="J-hove-wrap EDropdown fr">
                <div class="item">
                    <div class="name">
                                                <a href="//honor.jd.com" target="_blank" title="荣耀京东自营旗舰店" clstag="shangpin|keycount|product|dianpuname1">荣耀京东自营旗舰店</a>
                                            </div>
                </div>
                                <div class="item hide J-im-item">
                    <div class="J-im-btn" clstag="shangpin|keycount|product|dongdong_1"></div>
                </div>
                <div class="item hide J-jimi-item">
                    <div class="J-jimi-btn" clstag="shangpin|keycount|product|jimi_1"></div>
                </div>
                                <div class="item">
                    <div class="follow J-follow-shop" data-vid="1000000904" clstag="shangpin|keycount|product|guanzhu">
                        <i class="sprite-follow"></i><span>关注店铺</span>
                    </div>
                </div>
                                <div class="contact-layer ">
                    <div class="content " data-drop="content">
                        <div class="score-body">
                                                        <div class="pop-shop-im">
                                <div class="hide J-contact-text">客服</div>
                                <div class="hide J-im-item">
                                    <div class="J-im-btn clearfix"></div>
                                </div>
                                <div class="hide J-jimi-item">
                                    <div class="J-jimi-btn clearfix"></div>
                                </div>

                                                            </div>
                                                        <div class="pop-shop-qr-code J-contact-qrcode clearfix">
                                <div class="qr-code hide J-wd-qrcode">
                                    <img src="//misc.360buyimg.com/lib/img/e/blank.gif" width="78" height="78" alt="关注微店"/>
                                    <p>关注微店</p>
                                </div>
                                <div class="qr-code J-m-qrcode" data-url="https://cd.jd.com/qrcode?skuId=100013116298&location=3&isWeChatStock=2">
                                    <div class="J-m-wrap"></div>
                                    <p>手机下单</p>
                                </div>
                            </div>
                                                        <div class="btns">
                                                                <a href="//honor.jd.com" target="_blank" class="btn-def enter-shop J-enter-shop" clstag="shangpin|keycount|product|jindian1">
                                    <i class="sprite-enter"></i><span>进店逛逛</span>
                                </a>
                                <span class="separator">|</span>
                                <a href="#none" class="btn-def follow-shop J-follow-shop" data-vid="1000000904" clstag="shangpin|keycount|product|guanzhu1">
                                    <i class="sprite-follow"></i><span>关注店铺</span>
                                </a>
                                                            </div>
                        </div>
                    </div>
                </div>
            </div>
</div><!-- .contact -->
        <div class="clr"></div>
    </div>
</div>

<div class="w">
    <div class="product-intro clearfix">
        <div class="preview-wrap">
            <div class="preview" id="preview">
                                    <div id="spec-n1" class="jqzoom main-img" data-big="1" clstag="shangpin|keycount|product|mainpic_fz">
                        <ul class="preview-btn J-preview-btn">
                                                                                                                <li>
                                <span class="video-icon J-video-icon" clstag="shangpin|keycount|product|picvideo" style="display:none"></span>
                            </li>
                                                    </ul>
                        <img id="spec-img" width="350" data-origin="//img13.360buyimg.com/n1/jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg" alt="荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏"/>
                                                                                                                           <div id="belt"></div>
                    </div>
                                                <div class="video" id="v-video" data-vu="500127490">
                    <div class="J-v-player"></div>
                    <a href="#none" class="close-video J-close hide" clstag="shangpin|keycount|product|closepicvideo"></a>
                </div>
                                    <script>
                        (function(doc, cfg) {
                            var img = doc.getElementById('spec-img');
                            var src = img.getAttribute('data-origin');
                            var nsz = 300;

                            if ((!cfg.wideVersion || !cfg.compatible) && !cfg.product.ctCloth) {
                                img.setAttribute('width', nsz);
                                /*img.setAttribute('height', nsz);*/
                                img.setAttribute('src', src.replace('s450x450', 's'+ nsz +'x' + nsz));
                            } else {
                                img.setAttribute('src', src);
                            }

                            if(cfg.product.ctCloth) {
                                if (!cfg.wideVersion || !cfg.compatible) {
                                    img.setAttribute('width', nsz);
                                }
                            }
                        })(document, pageConfig);
                    </script>
                    <div class="spec-list" clstag="shangpin|keycount|product|lunbotu_1">
                        <a id="spec-forward" href="javascript:;" class="arrow-prev"><i class="sprite-arrow-prev"></i></a>
                        <a id="spec-backward" href="javascript:;" class="arrow-next"><i class="sprite-arrow-next"></i></a>
                        <div id="spec-list" class="spec-items">
                            <ul class="lh">
                                                                                                                                                                                                <li  class='img-hover'><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg' data-url='jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg' data-img='1' width='50' height='50'></li>
                                                                <li ><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/121777/6/2122/484886/5ec27a37Eb1ce27c7/cfe6e3e6482b572c.jpg' data-url='jfs/t1/121777/6/2122/484886/5ec27a37Eb1ce27c7/cfe6e3e6482b572c.jpg' data-img='1' width='50' height='50'></li>
                                                                <li ><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/120414/33/2130/177459/5ec27a36E369ebf5c/42c7e0972b18c878.jpg' data-url='jfs/t1/120414/33/2130/177459/5ec27a36E369ebf5c/42c7e0972b18c878.jpg' data-img='1' width='50' height='50'></li>
                                                                <li ><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/113819/16/7319/71328/5ec27a37Eb37a95e9/4b53e325d49ef1dd.jpg' data-url='jfs/t1/113819/16/7319/71328/5ec27a37Eb37a95e9/4b53e325d49ef1dd.jpg' data-img='1' width='50' height='50'></li>
                                                                <li ><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/123399/27/2081/126919/5ec27a37E208530a6/febac8a84c2692a1.jpg' data-url='jfs/t1/123399/27/2081/126919/5ec27a37E208530a6/febac8a84c2692a1.jpg' data-img='1' width='50' height='50'></li>
                                                                <li ><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/121153/9/2143/465712/5ec27a37E9cb1c5dd/f030a7f8272abd01.jpg' data-url='jfs/t1/121153/9/2143/465712/5ec27a37E9cb1c5dd/f030a7f8272abd01.jpg' data-img='1' width='50' height='50'></li>
                                                                <li ><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/119305/30/7358/90692/5ec29d36Ed04efcf3/0c152bde1ecb5b26.jpg' data-url='jfs/t1/119305/30/7358/90692/5ec29d36Ed04efcf3/0c152bde1ecb5b26.jpg' data-img='1' width='50' height='50'></li>
                                                                <li ><img alt='荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏' src='//img13.360buyimg.com/n5/jfs/t1/117399/1/7576/96607/5ec39e98Ef99c103d/00262b4fec44ca7b.jpg' data-url='jfs/t1/117399/1/7576/96607/5ec39e98Ef99c103d/00262b4fec44ca7b.jpg' data-img='1' width='50' height='50'></li>
                                                                                            </ul>
                        </div>
                    </div>
                    <div class="preview-info">
                        <div class="left-btns">
                            <a class="follow J-follow" data-id="100013116298" href="#none" clstag="shangpin|keycount|product|guanzhushangpin_1">
                                <i class="sprite-follow-sku"></i><em>关注</em>
                            </a>
                            <a class="share J-share" href="#none" clstag="shangpin|keycount|product|share_1">
                                <i class="sprite-share"></i><em>分享</em>
                            </a>
                                                                                    <a class="compare J-compare J_contrast" id="comp_100013116298" data-sku="100013116298" href="#none" clstag="shangpin|keycount|product|jiaruduibi">
                                <i class="sprite-compare"></i><em>对比</em>
                            </a>
                                                    </div>
                        <div class="right-btns">
                            <a class="report-btn" href="//jubao.jd.com/index.html?skuId=100013116298" target="_blank" clstag="shangpin|keycount|product|jubao">举报</a>
                        </div>
                    </div>

                                    </div>
            </div>
            <div class="itemInfo-wrap">
                <div class="sku-name">
                                        <img src="//img13.360buyimg.com/devfe/jfs/t4636/72/1687629000/219/64a7daf7/58e44c0fN9f20107c.png" alt="当季新品" />
                                                            荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏                </div>
                        <div class="news">
            <div class="item hide" id="p-ad" clstag="shangpin|keycount|product|slogana" data-hook="hide"></div>
            <div class="item hide" id="p-ad-phone" clstag="shangpin|keycount|product|sloganb" data-hook="hide"></div>
        </div>

                                <div class="summary summary-first">
            <div class="summary-price-wrap">
                                    <div class="summary-price J-summary-price">
                                                <div class="dt">京 东 价</div>
                        <div class="dd">
                            <span class="p-price"><span>￥</span><span class="price J-p-100013116298"></span></span>
                                                                                                                                                                                                                                                                                    <a class="notice J-notify-sale" data-type="1" data-sku="100013116298" href="#none" clstag="shangpin|keycount|product|jiangjia_1">降价通知</a>
                                                                                    <div class="fans-price J-fans-price hide">
                                <span class="p-price-fans">
                                    <span class="price J-p-f-100013116298"></span>
                                </span>
                                <img src="//img30.360buyimg.com/devfe/jfs/t17683/96/2616723497/1348/5d49daba/5afe6d90Nc2d9965a.png" alt="fans" class="fans-icon">
                                <span class="text"></span>
                            </div>
                            
                                                        <!-- 高端品 限时特惠start，这段代码中的样式，是需要改的，请前端同学定义样式。还有用js代码，完成对应的需求 -->
                            <span class="J-xsth-sale" style="display: none;">
                                    <a href="#none" class="J-xsth-panel" clstag="shangpin|keycount|product|xianshitehui">限时特惠<s class="s-arrow">></s></a>
                                    <i class="sprite-question"></i>
                                </span>
                            <!-- 高端品 限时特惠end -->

                                                                                    
                                                                                                                                            <div class="plus-price J-plus-price hide" style="display: none;">
                                    <span class="p-price-plus">
                                        <span class="price J-p-p-100013116298"></span>
                                    </span>
                                <img src="//img10.360buyimg.com/da/jfs/t5731/317/890792506/848/391b9a15/59224a28N48552ed2.png" alt="plus" class="plus-icon">
                                <span class="text"><strong>PLUS会员</strong>专享价</span>
                                <a clstag="shangpin|keycount|product|whatisplus" href="//plus.jd.com/index" target="_blank">现在开通PLUS会员享限时特惠 >></a>
                            </div>
                                                                                    <div class="firm-price J-firm-price hide" style="display: none;">
                                <span class="p-price-firm">
                                    <span class="price J-p-f-100013116298"></span>
                                </span>
                                <img src="//img13.360buyimg.com/imagetools/jfs/t1/110281/5/12499/1441/5e97ccb1Ec6a0e0da/eb5c07ae3cb8647d.png" alt="企业价" class="firm-icon">
                            </div>
                                                                                    <div class="user-price J-user-price hide" style="display: none;">
                                    <span class="p-price-user">
                                        <span class="price J-p-s-100013116298"></span>
                                    </span>
                                <img src="//img14.360buyimg.com/devfe/jfs/t5728/113/4603623007/244/a159e46d/59535259N6eed475d.png" alt="sam's" class="sam-icon">

                                <span class="text">您购买此商品可享受专属价</span>

                                <i class="sprite-question"></i>
                            </div>
                                                    </div>
                    </div>

                    <!-- 分期用分区价格展示需求 start -->
                                        <!-- 分期用分区价格展示需求 end -->

                                        <div class="summary-info J-summary-info clearfix">
                        <div id="comment-count" class="comment-count item fl" clstag="shangpin|keycount|product|pingjiabtn_1">
                            <p class="comment">累计评价</p>
                            <a class="count J-comm-100013116298" href="#comment">0</a>
                        </div>
                                                <div id="buy-rate" class="buy-rate item fl hide">
                            <p>选购指数</p>
                            <a class="count" href="//help.jd.com/user/issue/236-1470.html" target="_blank"  clstag="shangpin|keycount|product|xuangouzhishu_100013116298">0</a>
                        </div>
                                            </div>
                                                                                                                        <div id="summary-quan" class="li p-choose hide" clstag="shangpin|keycount|product|lingquan"></div>
                                        <div id="J-summary-top" class="summary-top" clstag="shangpin|keycount|product|cuxiao">
                        <div id="summary-promotion" class="summary-promotion" data-hook="hide">
                            <div class="dt">促&#x3000;&#x3000;销</div>
                            <div class="dd J-prom-wrap p-promotions-wrap">
                                <div class="p-promotions">
                                    <ins id="prom-mbuy" data-url="https://cd.jd.com/qrcode?skuId=100013116298&location=3&isWeChatStock=2"></ins>
                                    <ins id="prom-car-gift"></ins>
                                    <ins id="prom-gift" clstag="shangpin|keycount|product|zengpin_1"></ins>
                                    <ins id="prom-fujian" clstag="shangpin|keycount|product|fujian_1"></ins>
                                    <ins id="prom"></ins>
                                    <ins id="prom-one"></ins>
                                    <ins id="prom-phone"></ins>
                                    <ins id="prom-phone-jjg"></ins>
                                    <ins id="prom-tips"></ins>
                                    <ins id="prom-quan"></ins>
                                    <div class="J-prom-more view-all-promotions" data-hook="hide">
                                        <span class="prom-sum">展开促销</span>
                                        <a href="#none" class="view-link"><i class="sprite-arr-close"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

                        <div class="summary p-choose-wrap">
             
                                <div id="summary-support" class="li hide">
                    <div class="dt">增值业务</div>
                    <div class="dd">
                        <ul class="choose-support lh">
                        </ul>
                    </div>
                </div>

                <div class="summary-stock" clstag="shangpin|keycount|product|quyuxuanze_1" >
                    <div class="dt">配 送 至</div>
                    <div class="dd">
                        <div class="store clearfix">
                            <div class="stock-address">
                                <div id="area1" class="ui-area-wrap">
                                    <div class="ui-area-text-wrap"><!--展示内容主体-->
                                        <div class="ui-area-text">--请选择--</div><!--显示被选中的地区-->
                                        <b></b><!--小箭头-->
                                    </div>
                                    <div class="ui-area-content-wrap"><!--弹出内容主体-->
                                        <div class="ui-area-tab"></div><!--省市区选择标签-->
                                        <div class="ui-area-content"></div><!--地区内容-->
                                    </div>
                                </div>
                            </div>
                            <div id="store-prompt" class="store-prompt"></div>
                            <div class="J-promise-icon promise-icon fl promise-icon-more" clstag="shangpin|keycount|product|promisefw_1">
                                <div class="title fl">支持</div>
                                <div class="icon-list fl">
                                    <ul></ul>
                                    <span class="clr"></span>
                                </div>
                            </div>
                            <div class="J-dcashDesc dcashDesc fl"></div>
                        </div>
                    </div>
                </div>
                                                <div id="summary-supply" class="li" style="display:none">
                    <div class="dt">&#x3000;&#x3000;</div>
                    <div class="dd">
                        <div id="summary-service" class="summary-service"  clstag="shangpin|keycount|product|fuwu_1"></div>
                    </div>
                </div>
                                                <div id="summary-weight" class="li" style="display:none">
                    <div class="dt">重&#x3000;&#x3000;量</div>
                    <div class="dd"></div>
                </div>
                                                                <div class="SelfAssuredPurchase li" id="J_SelfAssuredPurchase" style="display:none;"></div>
                                <div class="summary-line"></div>
             
                                                                                                   <div id="choose-attrs"  >
                                                                                <div id="choose-attr-1" class="li p-choose" data-type="尺寸" data-idx="0">
                        <div class="dt ">选择尺寸                                                </div>
                        <div class="dd">
                                                        <div class="item  selected  " data-sku="100013116298" data-value="荣耀智慧屏X1系列">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-荣耀智慧屏X1系列">
                                                                                                            <img data-img="1" src="//img13.360buyimg.com/n9/s40x40_jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg" width="40" height="40" alt="荣耀智慧屏X1系列"><i>荣耀智慧屏X1系列</i>
                                                                                                        </a>
                                                            </div>
                                                        <div class="item  " data-sku="100007006134" data-value="荣耀智慧屏 系列">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-荣耀智慧屏 系列">
                                                                                                            <img data-img="1" src="//img14.360buyimg.com/n9/s40x40_jfs/t1/119904/39/8367/181981/5f22a2a9Ef7e9d999/f8a54440c3482267.jpg" width="40" height="40" alt="荣耀智慧屏 系列"><i>荣耀智慧屏 系列</i>
                                                                                                        </a>
                                                            </div>
                                                        <div class="item  " data-sku="100004099019" data-value="荣耀智慧屏PRO系列">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-荣耀智慧屏PRO系列">
                                                                                                            <img data-img="1" src="//img14.360buyimg.com/n9/s40x40_jfs/t1/147082/27/4416/181867/5f27a004Eea371989/2b84790fb072312b.jpg" width="40" height="40" alt="荣耀智慧屏PRO系列"><i>荣耀智慧屏PRO系列</i>
                                                                                                        </a>
                                                            </div>
                                                                                </div>
                    </div>
                                                                                                    <div id="choose-attr-2" class="li p-choose" data-type="版本" data-idx="1">
                        <div class="dt ">选择版本                                                </div>
                        <div class="dd">
                                                        <div class="item  " data-sku="100007791251" data-value="X1 50“ 新品惠购">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-X1 50“ 新品惠购">
                                                                        X1 50“ 新品惠购                                                                    </a>
                                                            </div>
                                                        <div class="item  " data-sku="100007006134" data-value="55“ 超薄金属机身818旗舰芯片">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-55“ 超薄金属机身818旗舰芯片">
                                                                        55“ 超薄金属机身818旗舰芯片                                                                    </a>
                                                            </div>
                                                        <div class="item  " data-sku="100004099019" data-value="55“ 视频通话震撼音效炫彩灯效">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-55“ 视频通话震撼音效炫彩灯效">
                                                                        55“ 视频通话震撼音效炫彩灯效                                                                    </a>
                                                            </div>
                                                        <div class="item  selected  " data-sku="100013116298" data-value="X1 55“ 央视推荐">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-X1 55“ 央视推荐">
                                                                        X1 55“ 央视推荐                                                                    </a>
                                                            </div>
                                                        <div class="item  " data-sku="100005171625" data-value="55“  4G超大内存818旗舰芯片">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-55“  4G超大内存818旗舰芯片">
                                                                        55“  4G超大内存818旗舰芯片                                                                    </a>
                                                            </div>
                                                        <div class="item  " data-sku="100005172199" data-value="55“ 视频通话远场语音超大内存">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-55“ 视频通话远场语音超大内存">
                                                                        55“ 视频通话远场语音超大内存                                                                    </a>
                                                            </div>
                                                        <div class="item  " data-sku="100013150076" data-value="X1 65“ 超值之选">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-X1 65“ 超值之选">
                                                                        X1 65“ 超值之选                                                                    </a>
                                                            </div>
                                                                                </div>
                    </div>
                                                                                <div id="choose-results" class="li" style="display:none"><div class="dt">已选择</div><div class="dd"></div></div>
                                    </div>

                                                
                                                                                                <div id="choose-luodipei" class="choose-luodipei li" style="display:none">
                    <div class="dt">送装服务</div>
                    <div class="dd"></div>
                </div>
                                                                <div id="choose-suits" class="li choose-suits" style="display:none">
                    <div class="dt">套&#x3000;&#x3000;装</div>
                    <div class="dd clearfix"></div>
                </div>
                                <div id="choose-gift" class="choose-gift li"  style="display: none;">
                    <div class="dt">搭配赠品</div>
                    <div class="dd clearfix">
                        <div class="gift J-gift" clstag="shangpin|keycount|product|dapeizengpin">
                            <i class="sprite-gift J-popup"></i><span class="gift-tips">选择搭配赠品(共<em>0</em>个)</span>
                        </div>
                        <!--choosed-->
                        <div class="J-gift-selected hide">
                            <div class="gift choosed J-gift-choosed"></div>
                            <a href="#none" class="gift-modify J-popup" clstag="shangpin|keycount|product|zengpin-genggai">更改</a>
                        </div>
                    </div>
                </div>
                                                                                <div id="choose-service" class="li" data-hook="hide" style="display:none;">
                    <div class="dt" data-yb="new_yb_server"></div>
                    <div class="dd"></div>
                </div>
                                                                <div id="choose-service+" class="li" style="display:none;">
                    <div class="dt">京东服务</div>
                    <div class="dd"></div>
                </div>
                                                                                <div id="choose-baitiao" class="li choose-baitiao" style="display:none"></div>
                                <div id="choose-jincai" class="li choose-jincai" style="display:none">
                    <div class="dt">企业金采</div>
                    <div class="dd">
                        <div class="jincai-list J-jincai-list">
                            <div class="item">
                                <a href="#none">先采购，后付款</a>
                            </div>
                            <div class="bt-info-tips">
                                <a class="J-bt-tips question icon fl" href="#none">　</a>
                            </div>
                        </div>
                    </div>
                </div>
                                                                                                              <div class="summary-line"></div>
                                <div id="choose-btns" class="choose-btns clearfix" >
                                    <div class="choose-amount "  clstag="shangpin|keycount|product|goumaishuliang_1">
                        <div class="wrap-input">
                            <input class="text buy-num" onkeyup="setAmount.modify('#buy-num');" id="buy-num" value="1"  data-max="200"/>
                            <a class="btn-reduce" onclick="setAmount.reduce('#buy-num')" href="#none">-</a>
                            <a class="btn-add" onclick="setAmount.add('#buy-num')" href="#none">+</a>
                        </div>
                    </div>
                <!--<a id="choose-btn-gift" class="btn-special1 btn-lg" style="display:none;" href="//cart.gift.jd.com/cart/addGiftToCart.action?pid=100013116298&pcount=1&ptype=1" class="btn-gift" clstag="shangpin|keycount|product|选作礼物购买_1"><b></b>选作礼物购买</a>-->
                                                                                                                                    <a href="//cart.jd.com/gate.action?pid=100013116298&pcount=1&ptype=1" id="InitCartUrl" class="btn-special1 btn-lg "  onclick='log("product", "加入购物车_1", "100013116298")' >加入购物车</a>
                                                <a id="btn-baitiao" class="btn-special2 btn-lg" style="display:none;" onclick='log("product", "dabaitiaobutton_737_794_798", "100013116298")'>打白条</a>
                <a href="//jc.jd.com" target="_blank" id="btn-jincai" class="btn-special2 btn-lg" style="display: none;" clstag="shangpin|keycount|product|jincai_1">使用金采</a>
                                                                                                                    <a href="#none" id="btn-notify" class="J-notify-stock btn-special3 btn-lg notify-stock" style="display:none;" data-type="2" data-sku="100013116298" clstag="shangpin|keycount|product|daohuo_1">到货通知</a>
                                                                                                            </div>
                        <div id="local-tips" class="summary-tips hide">
                <div class="dt">本地活动</div>
                <div class="dd">
                    <ol class="tips-list clearfix"></ol>
                </div>
            </div>
                                                <div id="summary-tips" class="summary-tips" clstag="shangpin|keycount|product|wenxintishi_1" style="display: none">
                <div class="dt">温馨提示</div>
                <div class="dd">
                    <ol class="tips-list clearfix">
                    </ol>
                </div>
            </div>
                                                        </div>
            </div>
            <div id="track" class="track">
        <div class="extra-trigger">
            <a href="#none"><i class="sprite-extra"></i>更多商品信息</a>
        </div>
        <div class="extra">
                                                                        <div class="brand-logo" clstag="shangpin|keycount|product|dianpulogo">
                <a href='//honor.jd.com' target='_blank'>
                    <img src='//img30.360buyimg.com/popshop/jfs/t30451/261/1021356198/6313/6e0cd22a/5c04d2ffNfdd0d798.jpg' title='荣耀京东自营旗舰店'/>
                </a>
            </div>
                                                            <div class="track-tit">
                <h3></h3>
                <span></span>
            </div>
            <div class="track-con" data-rid="902029">
            </div>
            <div class="track-more">
                <a href="#none" class="J-prev sprite-up">上翻</a>
                <a href="#none" class="J-next sprite-down">下翻</a>
            </div>
        </div>
    </div>
    </div>
</div>


<div class="w">
    <div class="m m-content hide" id="similar">
        <div class="mt">
            <h3 class="fl">为你推荐</h3>
            <div class="extra">
                <div class="page-num"></div>
            </div>
        </div>
        <div class="mc">
            <a href="#none" class="arrow-prev disabled"><i class="sprite-arrow-prev"></i></a>
            <div class="list clearfix"></div>
            <a href="#none" class="arrow-next disabled"><i class="sprite-arrow-next"></i></a>
        </div>
    </div>
</div>



<div class="w">
    <div id="fittings" class="fittings ETab hide">
        <div class="tab-main large">
            <ul>
                <li data-tab="trigger" class="current" data-name="人气配件" onclick='log("gz_item", "gz_detail","02","tjpj_pjfl_人气配件","","main")'>人气配件</li>
            </ul>
            <div class="extra"></div>
        </div>
        <div class="tab-con J_fitting_con clearfix">
            <div class="master">
                <div class="p-list">
                    <div class="p-img">
                        <a href="//jd.com/" target="_blank">
                            <img data-img="1" src="//img14.360buyimg.com/n4/jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg" width="100" height="100" alt="荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏"/>
                        </a>
                    </div>
                    <div class="p-name">
                        <a href="//item.jd.com/100013116298.html" target="_blank">荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏</a>
                    </div>
                    <div class="p-price hide">
                        <input type="checkbox" data-sku="100013116298" id="inp-acc-master" checked/>
                        <label for="inp-acc-master"><strong class="J-p-100013116298">￥</strong></label>
                    </div>
                    <i class="plus">+</i>
                </div>
            </div>
            <div class="suits">
                <div class="switchable-wrap" data-tab="item">
                    <div class="btns">
                        <a href="javascript:void(0)" target="_self" class="prev-btn"></a>
                        <a href="javascript:void(0)" target="_self" class="next-btn"></a>
                    </div>
                    <div class="lh-wrap">
                        <ul class="lh clearfix"></ul>
                    </div>
                </div>
            </div>

            <div class="infos">
                <div class="selected">已选择<em class="J-selected-cnt">0</em>个配件</div>
                <div class="p-price">
                    <span>组合价</span>
                    <strong class="J_cal_jp">￥暂无报价</strong>
                </div>
                <div class="btn">
                    <a href="#none" class="btn-primary J-btn" target="_blank" onclick='log("gz_item", "gz_detail","02","tjpj_ycgm_ljgm", pageConfig.getAccSelectedSkus(),"main")'>立即购买</a>
                </div>
                                                <a href="//kong.jd.com/index?sku=100013116298&cid=798" target="_blank" class="acc-buy-center" onclick='log("gz_item", "gz_detail","02","tjpj_gdpj","","main")'>配件选购中心</a>
                                <i class="equal">=</i>
            </div>
        </div>
    </div>
</div>
<div class="w">
    </div>

<div class="w">
    <div class="aside">
                                <div class="m m-aside popbox" id="popbox">
            <div class="popbox-inner" data-fixed="pro-detail-hd-fixed">
    <div class="mt">
        <h3>
                        <a href="//honor.jd.com" target="_blank" title="荣耀京东自营旗舰店" clstag="shangpin|keycount|product|dianpuname2_荣耀京东自营旗舰店">荣耀京东自营旗舰店</a>
                                </h3>
                        <span class="arrow"></span>
            </div>
        <div class="mc">
        <div class="pop-score-summary">
            <div class="btns">
                <a href="//honor.jd.com" target="_blank" class="btn-def enter-shop J-enter-shop" clstag="shangpin|keycount|product|jindian2">
                    <i class="sprite-enter"></i>
                    <span>进店逛逛</span>
                </a>
                <a href="#none" class="btn-def follow-shop J-follow-shop" data-vid="1000000904" clstag="shangpin|keycount|product|guanzhu2">
                    <i class="sprite-follow"> </i>
                    <span>关注店铺</span>
                </a>
            </div>
        </div>
    </div>
    </div>
        </div>
                                
                        <div id="sp-search" class="m m-aside sp-search" clstag="shangpin|keycount|product|pop-03">
            <div class="mt">
                <h3>店内搜索</h3>
            </div>
            <div class="mc">
                <p class="sp-form-item1"><label for="sp-keyword">关键字：</label><span><input type="text" id="sp-keyword" onkeydown="javascript:if(event.keyCode==13){pageConfig.searchClick(1);}"></span></p>
                <p class="sp-form-item2"><label for="sp-price">价&#x3000;格：</label><span><input type="text" id="sp-price" onkeyup="changeSpPrice('sp-price');" onkeydown="javascript:if(event.keyCode==13){pageConfig.searchClick(1);}"/> 到 <input type="text" id="sp-price1" onkeyup="changeSpPrice('sp-price1');" onkeydown="javascript:if(event.keyCode==13){pageConfig.searchClick(1);}"/></span></p>
                <p class="sp-form-item3"><label for="">&#x3000;&#x3000;&#x3000;</label><span><input type="submit" value="搜索" id="btnShopSearch" data-url='//honor.jd.com/view_shop_search-394032.html' /></span></p>
            </div>
        </div>
                                <div id="sp-category" class="m m-aside sp-category" clstag="shangpin|keycount|product|pop-04">
            <div class="mt">
                <h3>店内分类</h3>
            </div>
            <div class="mc no-padding">
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13852011-1-0-20-1.html' target='_blank'>荣耀手机</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-13884314-1-0-20-1.html' target='_blank'>荣耀V系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13884315-1-0-20-1.html' target='_blank'>荣耀HONOR系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13884316-1-0-20-1.html' target='_blank'>荣耀X系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13884317-1-0-20-1.html' target='_blank'>荣耀Play系列</a></dd>
                                    </dl>
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13246122-1-0-20-1.html' target='_blank'>智慧屏</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-14518444-1-0-20-1.html' target='_blank'>荣耀智慧屏X1系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246123-1-0-20-1.html' target='_blank'>荣耀智慧屏</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13559652-1-0-20-1.html' target='_blank'>荣耀智慧屏4G版</a></dd>
                                    </dl>
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13246380-1-0-20-1.html' target='_blank'>笔记本</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-13552578-1-0-20-1.html' target='_blank'>MagicBook 14</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13552579-1-0-20-1.html' target='_blank'>MagicBook 15</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246381-1-0-20-1.html' target='_blank'>MagicBook 2019 锐龙版</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246382-1-0-20-1.html' target='_blank'>MagicBook Pro 锐龙版</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246383-1-0-20-1.html' target='_blank'>MagicBook 2019 英特尔</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246384-1-0-20-1.html' target='_blank'>MagicBook Pro 英特尔</a></dd>
                                    </dl>
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13246118-1-0-20-1.html' target='_blank'>平板电脑</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-14903226-1-0-20-1.html' target='_blank'>荣耀平板V6</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14903227-1-0-20-1.html' target='_blank'>荣耀平板6</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14903228-1-0-20-1.html' target='_blank'>荣耀平板5</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14903229-1-0-20-1.html' target='_blank'>荣耀畅玩平板2</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14903230-1-0-20-1.html' target='_blank'>配件</a></dd>
                                    </dl>
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13246053-1-0-20-1.html' target='_blank'>智能穿戴</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246054-1-0-20-1.html' target='_blank'>手环5系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246055-1-0-20-1.html' target='_blank'>手环4系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246056-1-0-20-1.html' target='_blank'>手表2系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246057-1-0-20-1.html' target='_blank'>手表1系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246058-1-0-20-1.html' target='_blank'>儿童手表小k2系列</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246059-1-0-20-1.html' target='_blank'>手环3系列</a></dd>
                                    </dl>
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13246351-1-0-20-1.html' target='_blank'>路由器</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-14590578-1-0-20-1.html' target='_blank'>荣耀路由3 AX3000</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14590579-1-0-20-1.html' target='_blank'>荣耀路由X3pro</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13690467-1-0-20-1.html' target='_blank'>荣耀猎人电竞路由</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246352-1-0-20-1.html' target='_blank'>荣耀路由Pro 2</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246353-1-0-20-1.html' target='_blank'>荣耀路由X2</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246354-1-0-20-1.html' target='_blank'>荣耀路由X2 增强版</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246355-1-0-20-1.html' target='_blank'>荣耀路由X2增强 Mesh版</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246357-1-0-20-1.html' target='_blank'>荣耀路由Pro</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246358-1-0-20-1.html' target='_blank'>荣耀路由Pro 游戏版</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246359-1-0-20-1.html' target='_blank'>荣耀分布式路由</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246360-1-0-20-1.html' target='_blank'>荣耀Wifi穿墙宝 双支装</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246361-1-0-20-1.html' target='_blank'>荣耀Wifi穿墙宝 单支装</a></dd>
                                    </dl>
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13246406-1-0-20-1.html' target='_blank'>手机伴侣</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246407-1-0-20-1.html' target='_blank'>音频耳机</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246408-1-0-20-1.html' target='_blank'>智能手环</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246409-1-0-20-1.html' target='_blank'>智能设备</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246410-1-0-20-1.html' target='_blank'>自拍杆/架</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246411-1-0-20-1.html' target='_blank'>充电器/线</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-13246412-1-0-20-1.html' target='_blank'>移动电源</a></dd>
                                    </dl>
                                <dl class=''>
                    <dt class=''><s></s><a href='//mall.jd.com/view_search-394032-13246450-1-0-20-1.html' target='_blank'>智能家居</a></dt>
                                        <dd><a href='//mall.jd.com/view_search-394032-14589204-1-0-20-1.html' target='_blank'>生活电器</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14589205-1-0-20-1.html' target='_blank'>个护健康</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14589206-1-0-20-1.html' target='_blank'>智能设备</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14589207-1-0-20-1.html' target='_blank'>灯饰照明</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14589208-1-0-20-1.html' target='_blank'>水具酒具</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14589209-1-0-20-1.html' target='_blank'>游戏设备</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14589210-1-0-20-1.html' target='_blank'>外设产品</a></dd>
                                        <dd><a href='//mall.jd.com/view_search-394032-14788810-1-0-20-1.html' target='_blank'>影音娱乐</a></dd>
                                    </dl>
                            </div>
        </div>
                <div class="m m-aside pop-hot" id="pop-hot">
            <div class="mc no-padding">
                <div class="ETab">
                    <div class="tab-main large">
                        <ul>
                            <li data-tab="trigger" class="current">店铺热销</li>
                            <li data-tab="trigger">热门关注</li>
                        </ul>
                    </div>
                    <div class="tab-con">
                        <div id="sp-hot-sale" data-tab="item" clstag="shangpin|keycount|product|dianpurexiao_2"></div>
                        <div id="sp-hot-fo" data-tab="item" class="hide" clstag="shangpin|keycount|product|remenguanzhu_2"></div>
                    </div>
                </div>
            </div>
        </div>

                <div class="m m-aside" id="sp-new" clstag="shangpin|keycount|product|dianpuxinpin_1"></div>

                        <div id="sp-ad" class="m m-aside hide">
        </div>

                                        <div id="miaozhen7886" class="m m-aside" clstag="shangpin|keycount|product|ad_1"></div>
        <div id="miaozhen10767" class="m m-aside" clstag="shangpin|keycount|product|ad_1"></div>
                                <div id="ad_market_1" class="m m-aside"></div>
            </div>
    <div class="detail">
                        <div class="ETab" id="detail">
            <div class="tab-main large" data-fixed="pro-detail-hd-fixed">
                <ul>
                    <li data-tab="trigger" data-anchor="#detail" class="current" clstag="shangpin|keycount|product|shangpinjieshao_1">商品介绍</li>
                                        <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|pcanshutab">规格与包装</li>
                                                            <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|ershouzhijian" style="display:none">质检报告</li>
                                                            <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|psaleservice">售后保障</li>
                                                            <li data-tab="trigger" data-offset="38" data-anchor="#comment" clstag="shangpin|keycount|product|shangpinpingjia_1">商品评价<s></s></li>
                                                                                <li style="display:none" data-tab="trigger" data-offset="38" data-anchor="#try-holder" clstag="shangpin|keycount|product|try-entry">京东试用<sup>new<b>◤</b></sup></li>
                </ul>
                <div class="extra">
                                        <div class="item addcart-mini">
                        <div class="J-addcart-mini EDropdown">
                            <div class="inner">
                                <div class="head" data-drop="head">
                                                                        <a id="InitCartUrl-mini" class="btn-primary" href="//cart.jd.com/gate.action?pid=100013116298&pcount=1&ptype=1" onclick='log("product", "gouwuchexuanfu_1", "100013116298")'>加入购物车</a>
                                                                    </div>
                                <div class="content hide" data-drop="content">
                                    <div class="mini-product-info">
                                        <div class="p-img fl">
                                            <img src="//img13.360buyimg.com/n4/jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg" data-img="1" width="100" height="100" />
                                        </div>
                                        <div class="p-info lh">
                                            <div class="p-name">荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏</div>
                                            <div class="p-price">
                                                <strong class="J-p-100013116298"></strong> <span>X <span class="J-buy-num"></span></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                                                            <div class="item nav-im">
                        <div class="J-im-btn" clstag="shangpin|keycount|product|dongdong_1"></div>
                    </div>
                                    </div>
            </div>
            <div class="tab-con">
                <div data-tab="item">
                    <div class="p-parameter">
                                                                        <ul id="parameter-brand" class="p-parameter-list">
                            <li title='华为（HUAWEI）'>品牌： <a href='//list.jd.com/list.html?cat=737,794,798&ev=exbrand_8557' clstag='shangpin|keycount|product|pinpai_1' target='_blank'>华为（HUAWEI）</a>
                                <!--a href="#none" class="follow-brand btn-def" clstag='shangpin|keycount|product|guanzhupinpai'><b>&hearts;</b>关注 -->
                            </li>
                        </ul>
                                                <ul class="parameter2 p-parameter-list">
                                <li title='华为LOK-350'>商品名称：华为LOK-350</li>
    <li title='100013116298'>商品编号：100013116298</li>
                         <li title='19.3kg'>商品毛重：19.3kg</li>
            <li title='中国大陆'>商品产地：中国大陆</li>
                                    <li title='55英寸'>屏幕尺寸：55英寸</li>
                  <li title='三级能效'>能效等级：三级能效</li>
                  <li title='全面屏，人工智能，教育电视，智慧屏，4K超清'>电视类型：全面屏，人工智能，教育电视，智慧屏，4K超清</li>
                  <li title='新品电视'>用户优选：新品电视</li>
                  <li title='10.0-8.0'>选购指数：10.0-8.0</li>
                  <li title='2.5m-3m（46-55英寸）'>观看距离：2.5m-3m（46-55英寸）</li>
                                          </ul>
                                                <p class="more-par">
                            <a href="#product-detail" class="J-more-param">更多参数<s class="txt-arr">&gt;&gt;</s></a>
                        </p>
                                            </div>
                    <div id="quality-life" class="quality-life" style="display:none" clstag="shangpin|keycount|product|pinzhishenghuo">
                        <div class="q-logo">
                            <img src="//img20.360buyimg.com/da/jfs/t2077/314/2192172483/11044/f861504a/56ca6792N64e5eafc.png" alt="品质生活"/>
                        </div>
                        <ul class="quality-icon">
                                                                                                                                            <li class="J-ql-iframe ql-ico-1" data-type="1" data-text="质量承诺" style="display:none" data-title="质量承诺" clstag="shangpin|keycount|product|zhijianchengnuo">
                                <a href="#none"><i></i><span>质量承诺</span></a>
                            </li>
                            <li class="ql-ico-5" data-type="5" data-text="耐久性标签" style="display:none" clstag="shangpin|keycount|product|naijiuxingbiaoqian">
                                <a href="#none"><i></i><span>耐久性标签</span></a>
                            </li>
                            <li class="ql-ico-3" data-type="3" data-text="吊牌" style="display:none" clstag="shangpin|keycount|product|diaopai">
                                <a href="#none"><i></i><span>吊牌</span></a>
                            </li>
                            <li class="ql-ico-4" data-type="4" data-text="质检报告" style="display:none" clstag="shangpin|keycount|product|zhijianbaogao">
                                <a href="#none"><i></i><span>质检报告</span></a>
                            </li>
                            <li class="ql-ico-2" data-type="2" data-text="CCC证书" style="display:none" clstag="shangpin|keycount|product|3czhengshu">
                                <a href="#none"><i></i><span>CCC证书</span></a>
                            </li>
                                                        <li class="fresh-ico-1" data-text="实时温控" data-type="v1" style="display:none" clstag="shangpin|keycount|product|shishiwenkong">
                                <a href="#none"><i></i><span class="J-fresh-wd fresh-wd"></span><span>实时温控</span></a>
                            </li>
                            <li class="fresh-ico-2" data-text="检验报告" data-type="v2" style="display:none" clstag="shangpin|keycount|product|jiancebaogao">
                                <a href="#none"><i></i><span>检验报告</span></a>
                            </li>
                        </ul>
                    </div>
                    <div id="suyuan-video"></div>
                                        <div id="J-detail-banner"></div>
                                                            <div id="activity_header" clstag="shangpin|keycount|product|activityheader"></div>
                                                            <div id="J-detail-pop-tpl-top-new" clstag="shangpin|keycount|product|pop-glbs">
                                            </div>

                    <div class="detail-content clearfix" data-name="z-have-detail-nav">
                        <div class="detail-content-wrap">
                                                                                    
                            <div class="detail-content-item">
                                                                <div id="J-detail-content">
                                    <div class="loading-style1"><b></b>商品介绍加载中...</div>                                </div><!-- #J-detail-content -->
                                                                                                <div id="activity_footer" clstag="shangpin|keycount|product|activityfooter"></div>
                                                            </div>
                        </div>
                                                <div id="J-detail-nav" class="detail-content-nav">
                            <ul id="J-detail-content-tab" class="detail-content-tab"></ul>
                                                                                </div>
                    </div>
                                        <div id="J-detail-pop-tpl-bottom-new" clstag="shangpin|keycount|product|pop-glbs">
                                            </div>

                    <div class="clb"></div>
                </div>
                                                <div data-tab="item" class="hide">
                                        <div class="Ptable">
            <div class="Ptable-item">
        <h3>交互设备</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>语音控制</dt><dd>支持</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>遥控类型</dt><dd>蓝牙遥控</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>语音输入</dt><dd>支持</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>核心参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>CPU核数</dt><dd>四核心</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>运行内存</dt><dd>2GB</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>操作系统</dt><dd>Harmony OS 1.0</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>CPU</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>电视智能系统的中央处理器，是电视运行速度的重要保证。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>鸿鹄818智慧芯片</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>智能电视</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>智能电视内置了智能操作系统（一般为安卓系统），可以连接互联网，通过系统内置的视频、音乐、游戏等软件提供丰富的内容，也可下载海量应用扩展更多的功能。新一代的智能电视已经发展到人工智能，可以语音操控、人机互动，让电视成为家庭的多媒体控制中心。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>是</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>GPU</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>电视智能系统的图像处理器，是电视画质及游戏性能的重要保证。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>4*Mali-G51</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>存储内存</dt><dd>16GB</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>外观设计</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>机身厚薄</dt><dd>69.9mm（最薄处10.4mm）</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>边框材质</dt><dd>塑胶</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>安装孔距</dt><dd>200*200</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>边框宽窄</dt><dd>以官网为准</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>端口参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>USB3.0接口</dt><dd>1</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>HDMI2.0接口</dt><dd>3</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>网络参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>连接方式</dt><dd>无线/网线</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>网络连接</dt><dd>支持有线&无线</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>规格参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>单屏重量（kg）</dt><dd>13.42</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>单屏尺寸（宽*高*厚）mm</dt><dd>1233.4mm（长）*715.23mm（宽）*69.9mm（厚）（最薄处10.4mm）</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>外包装尺寸（宽*高*厚）mm</dt><dd>1360mm（长）×160mm（宽）×860mm（高）</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>含底座重量（kg）</dt><dd>14.1</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>含外包装重量（kg）</dt><dd>19.3</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>含底座尺寸（宽*高*厚）mm</dt><dd>1233.4mm（长）*774.27mm（宽） *219.1 mm（厚）（最薄处10.4mm）</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>功耗参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>电源功率（w）</dt><dd>140W</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>待机功率（w）</dt><dd>小于0.5W</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>工作电压（v）</dt><dd>220v</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>USB支持格式</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>USB支持音频格式</dt><dd>MP3/MP4/3GP等</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>USB支持图片格式</dt><dd>PNG/JPG/BMP等</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>USB支持视频格式</dt><dd>AVI/MP4/MOV/MKV等</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>显示参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>HDR显示</dt><dd>支持</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>支持格式（高清）</dt><dd>2160p</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>屏幕尺寸</dt><dd>55英寸</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>屏幕比例</dt><dd>16:9</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>背光方式</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>背光源是位于液晶显电视背后的一种光源，主要分为侧入式和直下式； 侧入式背光源指的把LED背光放置在屏幕的侧面，通过导光板点亮屏幕。一般侧入式背光的电视更轻薄。 直下式背光源是把LED做成密集的点阵，放置在屏幕的背后，直接照射屏幕。一般色域更好，图像效果更自然，对漏光控制更好，但是机身稍厚。 在一般的电视上，两种背光方式在感官上并没有太大区别，无需作为选购的主要标准。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>直下式</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>扫描方式</dt><dd>逐行扫描</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>屏幕分辨率</dt><dd>超高清4K</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>音频参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>扬声器数量</dt><dd>4个</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>主体参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>上市时间</dt><dd>2020-05</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>产品颜色</dt><dd>幻夜黑</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>产品类型</dt><dd>全面屏电视；人工智能电视；大屏电视；4K超清电视；智慧屏电视</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>能效等级</dt><dd>三级能效</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>认证型号</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>认证型号：3C证书上的产品型号。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>LOK-350</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>产品品牌</dt><dd>华为（HUAWEI）</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>产品型号</dt><dd>LOK-350</dd>
                            </dl>
                              </dl>
      </div>
      </div>
                                        <div class="package-list">
                        <h3>包装清单</h3>
                        <p>包装箱标配：
1）整机 x 1；
2）底座 x 2；
3）螺丝 x 4；
4）语音遥控器 x 1；
5）快速入门 x 1；
6）AV转接线 x 1；
7）电源线 x 1；
8）保修卡 x 1；
9）7号电池 x 2；

温馨提示：不同批次包装清单会存在差异，请以实物为准。</p>
                    </div>
                </div>
                                                                <div data-tab="item" class="hide">
                    <!--质检报告-->
                </div>
                                                <div data-tab="item" class="hide">
                    <!--售后保障 家用电器展示一个图文的字段 -->
                </div>
                                                <div data-tab="item" class="hide">
                    <!--商品评价-->
                </div>
                                                                <div data-tab="item" class="hide"></div>
            </div>
        </div>

                        <div class="m m-content guarantee" id="guarantee">
                                    <div class="mt">
                       <h3>售后保障</h3>
                    </div>
                                                <div class="mc">
                    <div class="item-detail item-detail-copyright">
                                                <div class="serve-agree-bd">
    <dl>
                                                                
                
                        <dt>
            <i class="goods"></i>
            <strong>厂家服务</strong>
        </dt>
        <dd>
                                                                            本产品全国联保，享受三包服务，质保期为：整机一年<br/>
                                                                                                            本产品提供上门安装调试、提供上门检测和维修等售后服务，自收到商品之日起，如您所购买家电商品出现质量问题，请先联系厂家进行检测，凭厂商提供的故障检测证明，在“我的京东-客户服务-返修退换货”页面提交退换申请，将有专业售后人员提供服务。京东承诺您：30天内产品出现质量问题可退货，180天内产品出现质量问题可换货，超过180天按国家三包规定享受服务。<br />
                                                                                                        </dd>
                                <dt>
            <i class="goods"></i>
            <strong>京东承诺</strong>
        </dt>
        <dd>
                            京东平台卖家销售并发货的商品，由平台卖家提供发票和相应的售后服务。请您放心购买！<br />
                                        注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！
        </dd>
                                <dt>
            <i class="goods"></i><strong>
             正品行货             </strong>
        </dt>
                        <dd>京东商城向您保证所售商品均为正品行货，京东自营商品开具机打发票或电子发票。</dd>
                                                <dt><i class="unprofor"></i><strong>全国联保</strong></dt>
                <dd>
                    凭质保证书及京东商城发票，可享受全国联保服务（奢侈品、钟表除外；奢侈品、钟表由京东联系保修，享受法定三包售后服务），与您亲临商场选购的商品享受相同的质量保证。京东商城还为您提供具有竞争力的商品价格和<a href='//help.jd.com/help/question-892.html' target='_blank'>运费政策</a>，请您放心购买！
                    <br/><br/>注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！
                </dd>
                                <dt><i class="no-worries"></i><strong>无忧退货</strong></dt>
        <dd class="no-worries-text">
            客户购买京东自营商品7日内（含7日，自客户收到商品之日起计算），在保证商品完好的前提下，可无理由退货。（部分商品除外，详情请见各商品细则）
        </dd>
            </dl>
</div>
                                                <div id="state">
                            <strong>权利声明：</strong><br />京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。
                            <p><b>注：</b>本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。</p>
                                                        <br />
                            <strong>价格说明：</strong><br />
                            <p><b>京东价：</b>京东价为商品的销售价，是您最终决定是否购买商品的依据。</p>
                            <p><b>划线价：</b>商品展示的划横线价格为参考价，并非原价，该价格可能是品牌专柜标价、商品吊牌价或由品牌供应商提供的正品零售价（如厂商指导价、建议零售价等）或该商品在京东平台上曾经展示过的销售价；由于地区、时间的差异性和市场行情波动，品牌专柜标价、商品吊牌价等可能会与您购物时展示的不一致，该价格仅供您参考。</p>
                            <p><b>折扣：</b>如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。</p>
                            <p><b>异常问题：</b>商品促销信息以商品详情页“促销”栏中的信息为准；商品的具体售价以订单结算页价格为准；如您发现活动商品售价或促销信息有异常，建议购买前先联系销售商咨询。</p>

                                                <br />
                        <strong>能效标识说明：</strong><br />
                        <p>根据国家相关能效标识法规和标准的要求，京东自营在售商品的能效标识图样，将会逐步替换为新版能源效率标识贴；受能效标识标准变化影响，部分产品的新版和旧版能效标识，在能效等级、测试值等方面会有差异，但产品实际性能完全一样，并不影响购买和使用，加贴新版或旧版能效标识的商品会随机发放，请您放心购买；如有疑问，请在购买前通过咚咚或来电咨询。</p>
                                            </div>
                </div>
            </div>
                    </div>
                                        <div class="m m-content comment" id="comment">
            <div class="mt">
                <h3>商品评价</h3>
            </div>
            <div class="mc">
                <div class="J-i-comment i-comment clearfix"></div>
                <div class="J-comments-list comments-list ETab" >
                    <div class="tab-main small">
                        <ul>
                            <li data-tab="trigger" clstag="shangpin|keycount|product|allpingjia_1" class="current"><a href="javascript:;">全部评论<em>()</em></a></li>
                            <li data-tab="trigger" clstag="shangpin|keycount|product|shaipic"><a href="javascript:;">晒图<em>()</em></a></li>
                            <li data-tab="trigger" clstag="shangpin|keycount|product|haoping_1"><a href="javascript:;">好评<em>()</em></a></li>
                            <li data-tab="trigger" clstag="shangpin|keycount|product|zhongping_1"><a href="javascript:;">中评<em>()</em></a></li>
                            <li data-tab="trigger" clstag="shangpin|keycount|product|chaping_1"><a href="javascript:;">差评<em>()</em></a></li>
                            <li clstag="shangpin|keycount|product|sybg-bq" class="try-report-btn" style="display:none;"><a href="#try-report">试用报告<em>()</em></a></li>
                        </ul>
                        <div class="extra">
                            <div class="sort-select J-sort-select hide">
                                <div class="current"><span class="J-current-sortType">推荐排序</span><i></i></div>
                                <div class="others">
                                    <div class="curr"><span class="J-current-sortType">推荐排序</span><i></i></div>
                                    <ul>
                                        <li class="J-sortType-item" data-sorttype="5" clstag="shangpin|keycount|product|morenpaixu">推荐排序</li>
                                        <li class="J-sortType-item" data-sorttype="6" clstag="shangpin|keycount|product|shijianpaixu">时间排序</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-con">
                        <div id="comment-0" data-tab="item">全部评论</div>
                        <div id="comment-1" data-tab="item" class="hide"><div class="iloading">正在加载中，请稍候...</div></div>
                        <div id="comment-2" data-tab="item" class="hide"><div class="iloading">正在加载中，请稍候...</div></div>
                        <div id="comment-3" data-tab="item" class="hide"><div class="iloading">正在加载中，请稍候...</div></div>
                        <div id="comment-4" data-tab="item" class="hide"><div class="iloading">正在加载中，请稍候...</div></div>
                    </div>
                </div>
            </div>
        </div>
                        <div id="askAnswer" class="m m-content askAnswer hide">
            <div class="mt">
                <h3>商品问答</h3>
            </div>
            <div class="mc">
                                <div class="ask-wrap">
                    <i class="icon-dog"></i><span>心中疑惑就问问买过此商品的同学吧~</span><a href="#none" clstag="shangpin|keycount|product|woyaotiwen" class="J-btn-ask btn-ask">我要提问</a>
                </div>
                                <div class="askAnswer-list">
                </div>
            </div>
        </div>
                <div id="try-holder"></div>
                <div class="m m-content try-entry hide" id="try-entry">
            <div class="mt">
                <h3>试用</h3>
            </div>
            <div class="mc">
                <div class="try-product">
                    <div class="p-img">
                        <img src="//img11.360buyimg.com/n2/s100x100_jfs/t1/146019/39/5431/118947/5f380328E953a47ba/04471d81482d3a31.jpg" width="100" height="100" alt="">
                    </div>
                    <div class="p-name">荣耀智慧屏X1 55英寸LOK-350 2G+16G 8K解码开关机无广告远场语音4K超清人工智能液晶教育电视全面屏</div>
                    <div class="p-price">
                        <strong class="J-p-100013116298"></strong>
                    </div>
                    <div class="p-apply">
                        提供 <strong class="J-count"></strong> 份 | 已有 <strong class="J-a-count"></strong> 人申请
                    </div>
                </div>
                <div class="try-btn">
                    <p class="time-left J-time-left">
                        剩余 <strong></strong>天 <strong></strong>时 <strong></strong>分 <strong></strong>秒
                    </p>
                    <a href="//try.jd.com/{actid}.html&source=005" class="btn-primary"  target="_blank" clstag="shangpin|keycount|product|qushiyong" >去试用</a>
                </div>
            </div>
        </div>
        
        <div id="try-report" class="try-report"></div>
                                    </div>
    <div class="clb"></div>
</div>

<div style='display:none'>
        <a href='//www.jd.com/compare/100013116298-100013150076-0-0.html'>华为LOK-350和华为LOK-360哪个好</a>
        <a href='//www.jd.com/compare/100013116298-100008970470-0-0.html'>华为LOK-350和海信HZ43E3D哪个好</a>
        <a href='//www.jd.com/compare/100013116298-7185303-0-0.html'>华为LOK-350和创维43H5哪个好</a>
        <a href='//www.jd.com/compare/100013116298-100005228312-0-0.html'>华为LOK-350和小米L65M5-EA哪个好</a>
        <a href='//www.jd.com/compare/100013116298-100008828920-0-0.html'>华为LOK-350和小米L55M5-EX哪个好</a>
        <a href='//www.jd.com/compare/100013116298-100003852503-0-0.html'>华为LOK-350和小米L32M5-EC哪个好</a>
        <a href='//www.jd.com/compare/100013116298-8790549-0-0.html'>华为LOK-350和TCL32L2F哪个好</a>
    </div>
<div style='display:none' >
        <a href='https://yp.jd.com/737572b7f06d2e9e52f.html'>sharp彩电</a>
        <a href='https://yp.jd.com/737dad651f4d354755a.html'>58海信</a>
        <a href='https://yp.jd.com/737d634eae8fdfd7a59.html'>海信48寸平板电视</a>
        <a href='https://yp.jd.com/7371b72bb22b4c26ebe.html'>三星电视机65寸4k</a>
        <a href='https://yp.jd.com/73705a8676b4190d4d2.html'>安卓液晶电视55</a>
        <a href='https://www.jd.com/phb/7374b1c2d8faa00547c.html'>32吋液晶电视</a>
        <a href='https://www.jd.com/phb/7379a8e8e98d8adf926.html'>led智能电视机</a>
        <a href='https://www.jd.com/phb/7373f6ebb24211411a5.html'>noc液晶电视</a>
        <a href='https://www.jd.com/phb/7373f42823a66035aaf.html'>电视机55寸高清</a>
        <a href='https://www.jd.com/phb/73721a511dcfaf8992d.html'>无限电视</a>
    </div>
<!-- 主站品牌页 , 口碑、排行榜 SEO开始 -->
<div id='CBP_CRK' style='display:none'>
        <!-- 主站品牌页 开始 -->
            <a href='https://www.jd.com/pinpai/540440.html'>LKT</a>
        <a href='https://www.jd.com/pinpai/461356.html'>SCT</a>
        <a href='https://www.jd.com/pinpai/798-187025.html'>Lanking</a>
        <a href='https://www.jd.com/pinpai/798-182720.html'>创星</a>
        <a href='https://www.jd.com/pinpai/798-16538.html'>索尼（SONY）</a>
        <a href='https://www.jd.com/jiage/737da0b7de51ad05c67.html'>创维电视40</a>
        <a href='https://www.jd.com/jiage/737f6a418eb1a84419c.html'>超立体</a>
        <a href='https://www.jd.com/tupian/737ff5ad49f329c288a.html'>十堰恒通物流</a>
        <a href='https://www.jd.com/tupian/737077a6f9a5570bc0b.html'>夏讯电视新款</a>
        <a href='https://www.jd.com/xinkuan/737627a770e9761017d.html'>东芝曲面电视咋样</a>
        <a href='https://www.jd.com/xinkuan/73798950e04ceba8d3a.html'>海信（Hisense）HZ39E30D</a>
        <a href='https://www.jd.com/sptopic/73797a34aa74639d434.html'>海尔56寸高清电视</a>
        <a href='https://www.jd.com/sptopic/737e752a71dd779c09b.html'>6300ca</a>
        <a href='https://www.jd.com/sptopic/737d6ade282a96b2d7d.html'>创维电视55g6b</a>
        <a href='https://www.jd.com/hotitem/737c51fa136fafcc386.html'>海信电视55寸led</a>
        <a href='https://www.jd.com/hotitem/737bb0a8cb66bc65269.html'>电视机软屏</a>
        <a href='https://www.jd.com/hotitem/7375dd44ea35a0d5878.html'>荣事达高清电视</a>
        <a href='https://www.jd.com/jxinfo/9d0d7ca3b4a2a6e2.html'>康佳电视机39排行榜，康佳电视机39十大排名推荐</a>
        <a href='https://www.jd.com/jxinfo/40d3cfbac7683406.html'>电视tcl60英寸排行榜，电视tcl60英寸十大排名推荐</a>
        <a href='https://www.jd.com/jxinfo/632ab2ddbde1d5d6.html'>TCL曲面电视哪款好？TCL曲面电视怎么样好用吗？</a>
            <!-- 主站品牌页 结束 -->
    
        <!-- 排行榜 开始 -->
            <a href='//club.jd.com/rank/798/e4b88de5a4aae5a5bd_2.html'>不太好</a>
        <a href='//club.jd.com/rank/798/e7ae80e6b481e5a4a7e696b9e7be8ee8a782_2.html'>简洁大方美观</a>
        <a href='//club.jd.com/rank/798/e4bdbfe794a8e696b9e4bebf_2.html'>使用方便</a>
        <a href='//club.jd.com/rank/798/e680a7e4bbb7e6af94e8be83e9ab98_2.html'>性价比较高</a>
        <a href='//club.jd.com/rank/798/e7b3bbe7bb9fe6b581e79585e7a8b3e5ae9a_2.html'>系统流畅稳定</a>
        <a href='//club.jd.com/rank/798/e8b4a8e9878fe69c89e4bf9de99a9c_2.html'>质量有保障</a>
        <a href='//club.jd.com/rank/798/e69c8de58aa1e68081e5baa6e5a5bd_2.html'>服务态度好</a>
        <a href='//club.jd.com/rank/798/e59381e8b4a8e580bce5be97e4bfa1e8b596_2.html'>品质值得信赖</a>
        <a href='//club.jd.com/rank/798/e789a9e6b581e9809fe5baa6e5bfab_2.html'>物流速度快</a>
        <a href='//club.jd.com/rank/798/e5a49ae6aca1e8b4ade4b9b0_2.html'>多次购买</a>
        <a href='//club.jd.com/rank/798.html'>好评度</a>
            <!-- 排行榜 结束 -->
    
        <!-- 口碑 开始 -->
            <a href='//club.jd.com/koubei/757362e794b5e8a786.html'>usb电视</a>
        <a href='//club.jd.com/koubei/6c6364e794b5e8a786.html'>lcd电视</a>
        <a href='//club.jd.com/koubei/6c673364e794b5e8a786.html'>lg3d电视</a>
        <a href='//club.jd.com/koubei/3535e5afb8346be794b5e8a786.html'>55寸4k电视</a>
        <a href='//club.jd.com/koubei/e4b990e794b5e8a786.html'>乐电视</a>
        <a href='//club.jd.com/koubei/3332e5afb8346be794b5e8a786.html'>32寸4k电视</a>
        <a href='//club.jd.com/koubei/3635e5afb8346be794b5e8a786.html'>65寸4k电视</a>
        <a href='//club.jd.com/koubei/e9a39ee588a9e6b5a66c6564e794b5e8a786.html'>飞利浦led电视</a>
        <a href='//club.jd.com/koubei/6c6736353030e794b5e8a786.html'>lg6500电视</a>
        <a href='//club.jd.com/koubei/6c6736383030e794b5e8a786.html'>lg6800电视</a>
            <!-- 口碑 结束 -->
    </div>
<!-- 主站品牌页 , 口碑、排行榜 SEO结束 -->

<div id="footmark" class="w footmark"></div>
<div id="GLOBAL_FOOTER"></div>
<script>
        seajs.use('MOD_ROOT/main/main.js', function (App) {
        App.init(pageConfig.product);
    });


                function totouchbate() {
  var exp = new Date();
  exp.setTime(exp.getTime() + 30 * 24 * 60 * 60 * 1000);
  document.cookie = "pcm=2;expires=" + exp.toGMTString() + ";path=/;domain=jd.com";
    window.location.href="//item.m.jd.com/product/100013116298.html";
}
if(window.showtouchurl) {
  $("#GLOBAL_FOOTER").after("<div class='ac' style='padding-bottom:30px;'>你的浏览器更适合浏览触屏版&nbsp;&nbsp;&nbsp;&nbsp;<a href='#none' style='text-decoration:underline;' onclick='totouchbate()'>京东触屏版</a></div>");
} else {
  $("#GLOBAL_FOOTER").css("padding-bottom", "30px");
}
    seajs.use(['MISC/jdf/1.0.0/unit/globalInit/5.0.0/globalInit.js','MISC/jdf/1.0.0/unit/category/2.0.0/category.js'],function(globalInit,category){
        globalInit();
        category({type:'mini', mainId:'#categorys-mini', el:'#categorys-mini-main'});
    });
</script>
<script type="text/javascript">
    $(".Ptable-tips").mouseover(function(){
        $(this).find(".tips").show();
    });
    $(".Ptable-tips").mouseout(function(){
        $(this).find(".tips").hide();
    });
</script>


<img src="//jcm.jd.com/pre" width="0" height="0" style="display:none"/>
<script>
seajs.use('//wl.jd.com/wl.js');
var hashTag = window.location.hash
if(hashTag && hashTag.match(new RegExp('[\"\'\(\)]'))){
    var href = window.location.href
    window.location.href = href.substring(0,href.indexOf("#"))
}

(function(){
    var bp = document.createElement('script');
    bp.type = 'text/javascript';
    bp.async = true;
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
(function () {
    var jdwebm = document.createElement('script');
    jdwebm.type = 'text/javascript';
    jdwebm.async = true;
    jdwebm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'h5.360buyimg.com/ws_js/jdwebm.js?v=ProDetail';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(jdwebm, s);
})();
</script><div id="J-global-toolbar"></div>
<script>
/*
(function(cfg) {
    cfg.toolbarParam = {
        bars: {
            history: {
                enabled: false
            }
        }
    }
})(pageConfig);
    ;(function(cfg) {
        var sid = cfg.cat[2] === 832 ? '737542' : '992349';
        var phoneNetwork = cfg.phoneNetwork
            ? cfg.phoneNetwork.join(',')
            : '';

        var hallEnable = cfg.cat[2] === 655;
        var hallUrl = {
            url: '//ctc.jd.com/hall/index?',
            param: {
                sku: cfg.skuid,
                cat: cfg.cat.join(','),
                mode: phoneNetwork
            }
        };

        var ad_entry = { enabled: false };
        var isDecCat = cfg.cat[0] == 1620 || cfg.cat[0] == 9847 
                        || cfg.cat[0] == 9855 || cfg.cat[0] == 6196
                        
        if (isDecCat) {
            ad_entry = {
                enabled: true,
                id: "0_0_7209",
                startTime: +new Date(2017, 3, 1, 0, 0, 1) / 1000,
                endTime: +new Date(2017, 4, 3, 0, 0, 0) / 1000
            }
        }

        var isEleCat = cfg.cat[0] === 737
        if (isEleCat) {
            ad_entry = {
                enabled: true,
                id: "0_0_7860",
                startTime: +new Date(2017, 3, 11, 0, 0, 1) / 1000,
                endTime: +new Date(2017, 4, 8, 0, 0, 0) / 1000
            }
        }

        seajs.use(['//static.360buyimg.com/devfe/toolbar/1.0.0/js/main'], function(toolbar) {
            pageConfig.toolbar = new toolbar({
                pType: 'item',
                bars: {
                    hall: {
                        index: 0.5,
                        title: '营业厅',
                        login: true,
                        enabled: hallEnable,
                        iframe: hallUrl.url + $.param(hallUrl.param)
                    },
                    cart: {
                        enabled: true
                    },
                    coupon: {
                        index: 1.5,
                        enabled: true,
                        title: '优惠券',
                        login: true,
                        iframe: '//cd.jd.com/coupons?' + $.param({
                            skuId: cfg.skuid,
                            cat: cfg.cat.join(','),
                            venderId: cfg.venderId
                        })
                    },
                    jimi: {
                        iframe: '//jimi.jd.com/index.action?productId='+ cfg.skuid +'&source=jdhome'
                    }
                },
                links: {
                    feedback: {
                        href: '//surveys.jd.com/index.php?r=survey/index/sid/323814/newtest/Y/lang/zh-Hans'
                    },
                    top:{ anchor:"#" }
                },
                ad: ad_entry
            });
        });
    })(pageConfig.product)
*/
</script>        

</body>
</html>"""
shopid_pettern = re.compile(r'shopId:\'(\d*)\',')
venderid_pettern = re.compile(r'venderId:(\d*),')
brand_pettern = re.compile(r'brand: (\d*),')
skuids_pettern = re.compile(r'{.*?"skuId":(\d+).*?}')
shop_name_pettern = re.compile(r'target="_blank" title="(\S*?)" clstag="shangpin')
ziying_pettern = re.compile(r'<div class="contact fr clearfix">[\s]*?<div class="name goodshop EDropdown">[\s]*?<em class="u-jd">[\s]*?(\S*?)[\s]*?</em>[\s]*?</div>')
cat_pettern = re.compile(r'cat: \[([,\d]*)\],')
print(shopid_pettern.findall(src))
print(venderid_pettern.findall(src))
print(brand_pettern.findall(src))
print(skuids_pettern.findall(src))
print(shop_name_pettern.findall(src))
print(ziying_pettern.findall(src))
print(cat_pettern.findall(src))

class A:
    def adsdd(self):
        pass
print(A().adsdd.__name__)