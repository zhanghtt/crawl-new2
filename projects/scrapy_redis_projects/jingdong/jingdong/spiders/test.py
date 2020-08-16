#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
product_pettern = re.compile(r'(product: \{[\s\S]*?\};)')

src = """<!DOCTYPE HTML>
<html lang="zh-CN">
<head>
    <!--yushou-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>【海信60E3F】海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源【行情 报价 价格 评测】-京东</title>
    <meta name="keywords" content="Hisense60E3F,海信60E3F,海信60E3F报价,Hisense60E3F报价"/>
    <meta name="description" content="【海信60E3F】京东JD.COM提供海信60E3F正品行货，并包括Hisense60E3F网购指南，以及海信60E3F图片、60E3F参数、60E3F评论、60E3F心得、60E3F技巧等信息，网购海信60E3F上京东,放心又轻松" />
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="mobile-agent" content="format=xhtml; url=//item.m.jd.com/product/100007300763.html">
    <meta http-equiv="mobile-agent" content="format=html5; url=//item.m.jd.com/product/100007300763.html">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <link rel="canonical" href="//item.jd.com/100007300763.html"/>
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
                                <link rel="stylesheet" type="text/css" href="//static.360buyimg.com/item/unite/1.0.102/components/??default/common/common.css,default/main/main.css,default/address/address.css,default/prom/prom.css,default/colorsize/colorsize.css,default/buytype/buytype.css,default/pingou/pingou.css,default/track/track.css,default/suits/suits.css,default/baitiao/baitiao.css,default/buybtn/buybtn.css,default/crumb/crumb.css,default/fittings/fittings.css,default/detail/detail.css,default/contact/contact.css" />
        <link rel="stylesheet" type="text/css" href="//static.360buyimg.com/item/unite/1.0.102/components/??default/popbox/popbox.css,default/preview/preview.css,default/info/info.css,default/imcenter/imcenter.css,default/jdservice/jdservice.css,default/vehicle/vehicle.css,default/poprent/poprent.css,default/jdservicePlus/jdservicePlus.css,default/jdserviceF/jdserviceF.css" />
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
                            'buybtn',
                            'pingou',
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
                            'vehicle'                        ],
                            imageAndVideoJson: {"mainVideoId":"208690205"},
                skuid: 100007300763,
        skuMarkJson: {"isxg":false,"isJDexpress":false,"isrecyclebag":false,"isSds":false,"isSopJSOLTag":false,"isyy":false,"isPOPDistribution":false,"isSopUseSelfStock":false,"isGlobalPurchase":false,"NosendWMS":false,"isOripack":false,"ispt":false,"unused":false,"pg":false,"isSopWareService":false,"isTimeMark":false,"presale":false},
        name: '海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源',
        skuidkey:'D783039EDF72F11EC2C5B187B569C542',
        href: '//item.jd.com/100007300763.html',
        src: 'jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg',
                     imageList: ["jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg","jfs/t1/115458/20/7603/248989/5ec4ac5dE44355ef8/8ee8971fc65581aa.jpg","jfs/t1/116103/7/7465/279371/5ec340b5E4e6ce00c/15467aed1a5d3efe.jpg","jfs/t1/127531/22/2139/146329/5ec340b5Ecb3029ea/1402a215f850faea.jpg","jfs/t1/122819/32/2119/29369/5ec340b7E0083c727/d3f92961cecea9d6.jpg","jfs/t1/120000/9/2129/126830/5ec340bdE6f67ee5b/7ddc12a5c7b98f4c.jpg","jfs/t1/114640/28/7324/90205/5ec340bdEa755a676/5da479f20da8fcd7.jpg","jfs/t1/137579/30/4682/104953/5f2cbdb7E8a140af5/f68b5e5b5cd23240.jpg","jfs/t1/139687/7/4723/60700/5f2cbdb7E4bafed01/0844754e749f2c27.jpg","jfs/t1/143700/25/4772/112584/5f2cbdbeEff43d1a0/8b7a2cff6e9f8854.jpg"],
                cat: [737,794,798],
        forceAdUpdate: '8271',
        brand: 7888,
        pType: 1,
        isClosePCShow: false,
                venderId:1000324421,
        shopId:'1000324421',
        shopSwitch:true,
                        specialAttrs:["YuShou","Customize-0","thwa-1","isFlashPurchase-0","sfkc-0","isFzxp-0","isOverseaPurchase-0","is7ToReturn-1","isCanUseDQ-1","fxg-0","isCanUseJQ-1"],
        recommend : [0,1,2,3,4,5,6,7,8,9],
        easyBuyUrl:"//easybuy.jd.com/skuDetail/newSubmitEasybuyOrder.action",
        qualityLife: "//c.3.cn/qualification/info?skuId=100007300763&pid=100007300763&catId=798",
        addToCartUrl: "//cart.jd.com/gate.action?pid=100007300763&pcount=1&ptype=1",
                colorSize: [{"skuId":100007637459,"尺寸":"ULED超画质社交新品-65E9F"},{"skuId":100006060267,"尺寸":"ULED量子点社交新品-65E8D"},{"skuId":100007167317,"尺寸":"高配游戏电视新品-65E75F"},{"skuId":100003525291,"尺寸":"3+32G超音画全面屏-65E7D"},{"skuId":100007338003,"尺寸":"3+32G社交电视新品-65E5F"},{"skuId":100003525293,"尺寸":"MEMC防抖超薄全面屏-65E5D"},{"skuId":100006254938,"尺寸":"MEMC全面屏爆品-65E3D-PRO"},{"skuId":100007826441,"尺寸":"4K超薄悬浮全面屏新品-65E3F"},{"skuId":8748165,"尺寸":"4K智慧AI纤薄爆品-65E3A"},{"skuId":100007300763,"尺寸":"4K超薄全面屏爆品-60E3F"}],        warestatus: 1,         tips: [{"order":2,"tip":"请完成预约后及时抢购！"}],                desc: '//cd.jd.com/description/channel?skuId=100007300763&mainSkuId=100007300763&charset=utf-8&cdn=2',
                /**/
                 /**/
                                                isYuYue: true,                        isBookMvd4Baby: false,        twoColumn: false,                mainSkuId:'100007300763',        isPop:false,
        addComments:true,
        foot: '//dx.3.cn/footer?type=common_config2',
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
                  window.location.href = "//item.m.jd.com/product/100007300763.html"+(paramIndex>0?location.href.substring(paramIndex,location.href.length):'');
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
                    window.location.href = "//item.m.jd.com/product/100007300763.html"+(paramIndex>0?location.href.substring(paramIndex,location.href.length):'');
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
    <script src="//misc.360buyimg.com/??jdf/lib/jquery-1.6.4.js,jdf/1.0.0/unit/base/1.0.0/base.js,jdf/1.0.0/ui/ui/1.0.0/ui.js"></script>
    <script type="text/JSConfig" id="J_JSConfig">
        {
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
}    </script>
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
<body version="140120" class="clothing yuyue  yyp cat-1-737 cat-2-794 cat-3-798 cat-4- item-100007300763 JD JD-1">
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
<!--shortcut end-->            <link rel="stylesheet" type="text/css" href="//misc.360buyimg.com/??jdf/1.0.0/unit/global-header/1.0.0/global-header.css,jdf/1.0.0/unit/shoppingcart/2.0.0/shoppingcart.css">
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
                url = '//mall.jd.com/advance_search-' + 1627957 + '-' + pageConfig.product.venderId + '-' + pageConfig.product.shopId + '-0-0-0-1-1-24.html';
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
</div>        <div id="shop-head"><div class="layout-area J-layout-area" >
		<div class="layout layout-auto J-layout" name="通栏布局（100%）" id="226656519" prototypeId="20" area="" layout_name="insertLayout" >
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





<div onclick="log('shop_03','mall_03','1000324421','19268','630128')" class="fn-clear  sh-brand-wrap-630128" modeId="19268" instanceId="226656521" module-name="new_shop_signs" style="margin-bottom:0px;;margin-bottom: 0px" origin="0" moduleTemplateId="630128"
          >
    <div class="mc" style=";">
		
        
        
		
<div class="sh-brand-wrap">
    <div class="sh-hot-container">
        <div class="sh-hot-content">
            <div class="J_ShopSignImg d-img-wrap"><img src="//img10.360buyimg.com/cms/jfs/t1/127595/18/8813/89181/5f28ba80E74fec47a/24b259ede937282a.jpg" data-size="1920,110"></div><a hot-box-name="热区1" hot-box-index="1" class="hot-link" px="358.8,0.0,196.0,101.3" href="//mall.jd.com/index-1000324421.html" style="top:0.00%;left:18.69%;width:10.21%;height:92.09%" target="_blank"></a><a hot-box-name="热区2" hot-box-index="2" class="hot-link" px="676.0,1.7,235.8,106.3" href="//item.jd.com/100013129894.html" style="top:1.55%;left:35.21%;width:12.28%;height:96.64%" target="_blank"></a><a hot-box-name="热区3" hot-box-index="3" class="hot-link" px="935.1,1.7,214.3,106.3" href="//item.jd.com/100011790176.html" style="top:1.55%;left:48.70%;width:11.16%;height:96.64%" target="_blank"></a><a hot-box-name="热区4" hot-box-index="4" class="hot-link" px="1177.6,1.7,169.4,106.3" href="//item.jd.com/100011951812.html" style="top:1.55%;left:61.33%;width:8.82%;height:96.64%" target="_blank"></a><a hot-box-name="热区5" hot-box-index="5" class="hot-link" px="1381.9,10.0,181.0,98.0" href="//item.jd.com/100007497487.html" style="top:9.09%;left:71.97%;width:9.43%;height:89.09%" target="_blank"></a>
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
        var base_url = "//mall.jd.com/view_search" +  "-1627957" + "-1000324421" + "-1000324421"   + "-0-1-0-0-1-1-24.html";
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
        var base_url = "//mall.jd.com/view_search" +  "-1627957" + "-1000324421" + "-1000324421"   + "-0-1-0-0-1-1-24.html";
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
            var base_url = "//mall.jd.com/view_search" +  "-1627957" + "-1000324421" + "-1000324421"   + "-0-1-0-0-1-1-24.html";
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
            url+="?sysName=mall.jd.com&venderId=" +"1000324421";
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





<div onclick="log('shop_03','mall_03','1000324421','18169','922476')" class="fn-clear  sh-head-menu-922476" modeId="18169" instanceId="226656524" module-name="shop_link" style="margin-bottom:0px;;margin-bottom: 0px" origin="0" moduleTemplateId="922476"
          >
    <div class="mc" style=";">
		
        
        
		<div style="height: 40px;overflow: hidden;">
    <div class="j-module" module-function="autoCenter" module-param="{}">
        <div class="userDefinedArea" style="width:1912px" data-title="">
            <div style="height:40px;overflow:hidden;">
	<div class="j-module" module-function="autoCenter" module-param="{}">
		<div class="userDefinedArea" style="width:1920px;margin-left:-8.5px;" data-title="">
<style type="text/css" >
#shop-head .user-nav{ height: 40px; width: 1200px; z-index:7;cursor:pointer; position: absolute; left: 50%;margin-left:-600px; background-color: #009ea1;}
#shop-head .user-menuB-placeholder{ height:40px; width:1200px; overflow:hidden;z-index:1; top: 0; }
#shop-head .user-menuB-list{ width: 1200px; height: 40px; float: left; position: absolute; top: 0px; z-index: 6;}
#shop-head .user-menuB-list li{ height:40px; width: auto; margin-right: 30px; top: 0; z-index: 7; float:left; text-align: left; font-size: 14px; color: #fff; line-height: 40px;}
#shop-head .user-menuB-list .user-menuB-link{ text-decoration: none; color: #fff!important; font-size: 14px; font-family: 微软雅黑; display: block; position: relative; z-index: 1; transition: all 0.5s;}
#shop-head .user-menuB-list .user-line{width:28px;height:4px;background:aqua; opacity: 0.9; border-radius:28px;top:31px; transform: translate(15px,0); position: absolute; transition:all 0.5s ease-in-out;}
#shop-head .user-menuB-list li:hover .user-menuB-link{color: aqua!important;}
#shop-head .user-menuB-list li.show .user-menuB-link{color: aqua!important;}
#shop-head .user-menuB-list li:nth-child(1).show ~ .user-line{transform: translate(15px,0);}
#shop-head .user-menuB-list li:nth-child(2).show ~ .user-line{ width: 56px; transform: translate(73px,0);}
#shop-head .user-menuB-list li:nth-child(3).show ~ .user-line{ width: 56px; transform: translate(159px,0);}
#shop-head .user-menuB-list li:nth-child(4).show ~ .user-line{ width: 56px; transform: translate(245px,0);}
#shop-head .user-menuB-list li:nth-child(5).show ~ .user-line{ width: 70px; transform: translate(331px,0);}
#shop-head .user-menuB-list li:nth-child(6).show ~ .user-line{ width: 56px; transform: translate(431px,0);}
#shop-head .user-menuB-list li:nth-child(7).show ~ .user-line{ width: 56px; transform: translate(517px,0);}
#shop-head .user-menuB-list li:nth-child(8).show ~ .user-line{ width: 56px; transform: translate(603px,0);}
#shop-head .user-menuB-list li:nth-child(9).show ~ .user-line{ width: 56px; transform: translate(689px,0);}
#shop-head .user-menuB-list li:nth-child(10).show ~ .user-line{ width: 56px; transform: translate(775px,0);}
#shop-head .user-menuB-list li:nth-child(11).show ~ .user-line{ width: 56px; transform: translate(861px,0);}
#shop-head .user-menuB-list li:nth-child(12).show ~ .user-line{ width: 56px; transform: translate(947px,0);}
#shop-head .user-list{display: none;position: absolute;left: 0;top: 40px;right: 0;z-index: 7;padding: 20px 40px;border: 1px solid #bebab0;background-color: rgba(247, 242, 234, 0.9);}
#shop-head .user-mover:hover .user-list{ display:block; }
#shop-head .user-list .user-pannel{ float:left; padding: 0; display: inline;}
#shop-head .user-list .user-sub-tittle{margin-bottom: 13px;height: 54px;line-height: 54px;border-bottom: dashed 1px #c9c9c9;padding: 0 20px;}
#shop-head .user-list .user-sub-tit-link{font-size: 14px;font-weight: bold;color: #333;line-height: 24px;display: inline-block;height: 24px;padding: 0 10px;border-radius: 12px;min-width: 74px; transition:0.5s;}
#shop-head .user-list .user-sub-tit-link:hover{ color:#F3171A;}
#shop-head .user-list .user-sub-list{ padding:0 20px;}
#shop-head .user-list ul{ list-style:none; margin: 0; padding: 0;}
#shop-head .user-list .user-leaf{font-size: 12px;height: 26px;line-height: 26px;}
#shop-head .user-list .user-leaf-link{ transition:0.5s;}
#shop-head .user-list .user-leaf-link:hover{ color:#F3171A;}
#shop-head .user-all-goods{clear: both;padding-left: 20px;}
#shop-head .user-all-goods-link{font-weight: bold;padding-left: 20px;border: solid 1px #666;border-radius: 12px;height: 24px;line-height: 24px;padding: 0 10px;}
#shop-head .user-nav-search{ height: 22px; width: 125px; border: none; position: absolute; right: 10px; top:9px; border-radius: 10px; background: #4e4545;}
#shop-head .user-nav-txt{ height: 22px; line-height: 22px; outline: none; border: none; background: #fff; padding: 0; color: #000; text-indent: 10px; border-radius: 10px 0 0 10px; font-size: 12px; position: absolute; width: 100px;}
#shop-head .user-nav-bt{ height: 22px; width: 25px;outline: none; border: none; background:url(//img13.360buyimg.com/cms/jfs/t1/7484/14/10472/284/5c22ee7bE7e3448ea/bbe1a3192dfb9446.png) no-repeat 3px 3px; padding: 0; position: absolute; cursor: pointer;left: 100px;border-radius: 0 10px 10px 0;}
   </style>
			<div style="width:1920px;height:40px;background:#009ea1;">
				<div class="j-module user-nav" module-function="slideHtml" module-param="{'imgArea':'.user-menuB-placeholder','imgNode':'.user-menuB-placeholder li','tabArea':'.user-menuB-list','tabNode':'.user-menuB-list li','subFunction':'moveEffect','eventType':'mouseenter','timer':'100'}">
					<div class="user-menuB-placeholder-box" style="margin:0px auto;">
						<ul class="user-menuB-placeholder" style="margin:0px auto;">
							<li style="float:left;" class="">
							</li>
						</ul>
					</div>
					<ul class="user-menuB-list">
						<li class="">
							<a class="user-menuB-link" style="font-weight:bold;color:#FFFFFF;margin-left:15px;" href="//mall.jd.com/index-1000324421.html" target="_self" clstag="jshopmall|keycount|1000324421|xdpdh">首页</a> 
						</li>
						<li class="user-mover show">
							<a class="user-menuB-link" style="color:#FFFFFF;" href="#" target="_self" clstag="jshopmall|keycount|1000324421|xdpdhqbfl">全部分类<span class="arrow"></span></a> 
							<div class="user-list">
								<dl class="user-pannel" style="height:276px;">
									<dt class="user-sub-tittle" clstag="jshopmall|keycount|1000324421|xdpdhqbfl1">
										<a href="//mall.jd.com/view_search-1627957-14230988-99-1-24-1.html" target="_blank" class="user-sub-tit-link">海信电视</a> 
									</dt>
									<dd class="user-sub-list">
										<div class="user-leaf-list">
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14445532-99-1-24-1.html" target="_blank" class="user-leaf-link">游戏电视新品</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230989-99-1-24-1.html" target="_blank" class="user-leaf-link">AI声控</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230991-99-1-24-1.html" target="_blank" class="user-leaf-link">全面屏电视</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230990-99-1-24-1.html" target="_blank" class="user-leaf-link">超薄电视</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230992-99-1-24-1.html" target="_blank" class="user-leaf-link">社交电视</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230993-99-1-24-1.html" target="_blank" class="user-leaf-link">4K HDR</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230994-99-1-24-1.html" target="_blank" class="user-leaf-link">ULED超画质</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230995-99-1-24-1.html" target="_blank" class="user-leaf-link">OLED电视</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230996-99-1-24-1.html" target="_blank" class="user-leaf-link">70-75英寸</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230997-99-1-24-1.html" target="_blank" class="user-leaf-link">58-65英寸</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230998-99-1-24-1.html" target="_blank" class="user-leaf-link">55英寸</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14230999-99-1-24-1.html" target="_blank" class="user-leaf-link">50英寸</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14231000-99-1-24-1.html" target="_blank" class="user-leaf-link">43英寸</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14231001-99-1-24-1.html" target="_blank" class="user-leaf-link">32-40英寸</a> 
											</div>
										</div>
									</dd>
								</dl>
								<dl class="user-pannel">
									<dt class="user-sub-tittle" clstag="jshopmall|keycount|1000324421|xdpdhqbfl2">
										<a href="//mall.jd.com/view_search-1627957-14243826-99-1-24-1.html" target="_blank" class="user-sub-tit-link">海信空调</a> 
									</dt>
									<dd class="user-sub-list">
										<div class="user-leaf-list">
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243827-99-1-24-1.html" target="_blank" class="user-leaf-link">新风空调</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243828-99-1-24-1.html" target="_blank" class="user-leaf-link">新一级能效</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14244147-99-1-24-1.html" target="_blank" class="user-leaf-link">爆款推荐</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243829-99-1-24-1.html" target="_blank" class="user-leaf-link">线下同款</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243831-99-1-24-1.html" target="_blank" class="user-leaf-link">小卧室（约10-16㎡）</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243830-99-1-24-1.html" target="_blank" class="user-leaf-link">大卧室（约15~22㎡）</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243832-99-1-24-1.html" target="_blank" class="user-leaf-link">小客厅（约20~32㎡）</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243833-99-1-24-1.html" target="_blank" class="user-leaf-link">大客厅（约28~45㎡）</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243836-99-1-24-1.html" target="_blank" class="user-leaf-link">挂机空调</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243837-99-1-24-1.html" target="_blank" class="user-leaf-link">柜机空调</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243834-99-1-24-1.html" target="_blank" class="user-leaf-link">变频空调</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14243835-99-1-24-1.html" target="_blank" class="user-leaf-link">定频空调</a> 
											</div>
										</div>
									</dd>
								</dl>
								<dl class="user-pannel">
									<dt class="user-sub-tittle" clstag="jshopmall|keycount|1000324421|xdpdhqbfl3">
										<a href="//mall.jd.com/view_search-1627957-14232470-99-1-24-1.html" target="_blank" class="user-sub-tit-link">海信冰箱</a> 
									</dt>
									<dd class="user-sub-list">
										<div class="user-leaf-list">
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234989-99-1-24-1.html" target="_blank" class="user-leaf-link">新品推荐</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234990-99-1-24-1.html" target="_blank" class="user-leaf-link">店长热荐</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234991-99-1-24-1.html" target="_blank" class="user-leaf-link">镜面玻璃系列</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234992-99-1-24-1.html" target="_blank" class="user-leaf-link">对开门</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234993-99-1-24-1.html" target="_blank" class="user-leaf-link">十字对开</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234994-99-1-24-1.html" target="_blank" class="user-leaf-link">法式多门</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234995-99-1-24-1.html" target="_blank" class="user-leaf-link">三门</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234996-99-1-24-1.html" target="_blank" class="user-leaf-link">两门</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234997-99-1-24-1.html" target="_blank" class="user-leaf-link">单门/迷你</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234998-99-1-24-1.html" target="_blank" class="user-leaf-link">风冷无霜</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14234999-99-1-24-1.html" target="_blank" class="user-leaf-link">变频节能</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14235000-99-1-24-1.html" target="_blank" class="user-leaf-link">智能WiFi控</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14235001-99-1-24-1.html" target="_blank" class="user-leaf-link">食神系列</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14235002-99-1-24-1.html" target="_blank" class="user-leaf-link">厨房冰箱</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14235003-99-1-24-1.html" target="_blank" class="user-leaf-link">客厅冰箱</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14235004-99-1-24-1.html" target="_blank" class="user-leaf-link">办公室冰箱</a> 
											</div>
										</div>
									</dd>
								</dl>
								<dl class="user-pannel">
									<dt class="user-sub-tittle" clstag="jshopmall|keycount|1000324421|xdpdhqbfl4">
										<a href="//mall.jd.com/view_search-1627957-14235577-99-1-24-1.html" target="_blank" class="user-sub-tit-link">海信洗衣机</a> 
									</dt>
									<dd class="user-sub-list">
										<div class="user-leaf-list">
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14235578-99-1-24-1.html" target="_blank" class="user-leaf-link">纤薄系列</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14236054-99-1-24-1.html" target="_blank" class="user-leaf-link">迷你/宝宝专用</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14236055-99-1-24-1.html" target="_blank" class="user-leaf-link">洗烘一体专区</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14236056-99-1-24-1.html" target="_blank" class="user-leaf-link">滚筒专区</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14236057-99-1-24-1.html" target="_blank" class="user-leaf-link">波轮专区</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14236058-99-1-24-1.html" target="_blank" class="user-leaf-link">电机包修12年</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14236059-99-1-24-1.html" target="_blank" class="user-leaf-link">宿舍/租房神器</a> 
											</div>
										</div>
									</dd>
								</dl>
								<dl class="user-pannel">
									<dt class="user-sub-tittle" clstag="jshopmall|keycount|1000324421|xdpdhqbfl5">
										<a href="//mall.jd.com/view_search-1627957-14096407-99-1-24-1.html" target="_blank" class="user-sub-tit-link">海信冷柜</a> 
									</dt>
									<dd class="user-sub-list">
										<div class="user-leaf-list">
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096658-99-1-24-1.html" target="_blank" class="user-leaf-link">店长热荐</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096659-99-1-24-1.html" target="_blank" class="user-leaf-link">新品推荐</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096660-99-1-24-1.html" target="_blank" class="user-leaf-link">家用冰柜</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14261545-99-1-24-1.html" target="_blank" class="user-leaf-link">客厅冰柜</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096661-99-1-24-1.html" target="_blank" class="user-leaf-link">变温柜-一机多用</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096662-99-1-24-1.html" target="_blank" class="user-leaf-link">双温柜-冷藏/冷冻</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096663-99-1-24-1.html" target="_blank" class="user-leaf-link">立式冷冻柜</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096664-99-1-24-1.html" target="_blank" class="user-leaf-link">商用冰柜</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096665-99-1-24-1.html" target="_blank" class="user-leaf-link">商用冷藏展示柜</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14096726-99-1-24-1.html" target="_blank" class="user-leaf-link">冰吧/酒柜</a> 
											</div>
										</div>
									</dd>
								</dl>
								<dl class="user-pannel">
									<dt class="user-sub-tittle" clstag="jshopmall|keycount|1000324421|xdpdhqbfl6">
										<a href="//mall.jd.com/view_search-1627957-14470784-99-1-24-1.html" target="_blank" class="user-sub-tit-link">海信净化除湿</a> 
									</dt>
									<dd class="user-sub-list">
										<div class="user-leaf-list">
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14470785-99-1-24-1.html" target="_blank" class="user-leaf-link">爆款净化除湿</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14470846-99-1-24-1.html" target="_blank" class="user-leaf-link">家用除湿机</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14470847-99-1-24-1.html" target="_blank" class="user-leaf-link">商用除湿机</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14470848-99-1-24-1.html" target="_blank" class="user-leaf-link">空气净化器</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14470849-99-1-24-1.html" target="_blank" class="user-leaf-link">家用新风系统</a> 
											</div>
											<div class="user-leaf">
												<a href="//mall.jd.com/view_search-1627957-14470850-99-1-24-1.html" target="_blank" class="user-leaf-link">商用新风系统</a> 
											</div>
										</div>
									</dd>
								</dl>
								<div class="user-all-goods">
									<a target="_blank" href="//mall.jd.com/view_search-1627957-0-99-1-24-1.html" class="all-goods-link">查看所有商品</a> 
								</div>
							</div>
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh1">
							<a class="user-menuB-link" target="_blank" href="//mall.jd.com/view_search-1627957-1000324421-1000324421-0-1-0-0-1-1-24.html?keyword=%25E6%25B5%25B7%25E4%25BF%25A1%25E7%2594%25B5%25E8%25A7%2586&amp;isGlobalSearch=1">海信电视</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh2">
							<a class="user-menuB-link" target="_blank" href="//mall.jd.com/view_search-1627957-1000324421-1000324421-0-1-0-0-1-1-24.html?keyword=%25E6%25B5%25B7%25E4%25BF%25A1%25E7%25A9%25BA%25E8%25B0%2583&amp;isGlobalSearch=1">海信空调</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh3">
							<a class="user-menuB-link" target="_blank" href="//pro.jd.com/mall/active/4Cq6rWivtPgy1ExNQBGXzbhBy2tq/index.html">海信冰箱</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh4">
							<a class="user-menuB-link" target="_blank" href="//pro.jd.com/mall/active/4T5p8BaDoT8AypXjRvyQfDJDRKtv/index.html">海信洗衣机</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh5">
							<a class="user-menuB-link" target="_blank" href="//pro.jd.com/mall/active/4M5PVocXfMQ6CsQVkFfkjPeZ3hMF/index.html">海信冷柜</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh10">
							<a class="user-menuB-link" target="_blank" href="//pro.jd.com/mall/active/3kDzunJ4rhPnnh5KNtAHAXZmaZGa/index.html">净化除湿</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh6">
							<a class="user-menuB-link" target="_blank" href="//mall.jd.com/index-1000164921.html">VIDAA电视</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh7">
							<a class="user-menuB-link" target="_blank" href="//mall.jd.com/index-1000000900.html">科龙空调</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh8">
							<a class="user-menuB-link" target="_blank" href="//mall.jd.com/index-1000002241.html">容声冰箱</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh9">
							<a class="user-menuB-link" target="_blank" href="//mall.jd.com/index-1000001978.html">海信手机</a> 
						</li>
						<li class="" clstag="jshopmall|keycount|1000324421|xdpdh11">
							<a class="user-menuB-link" target="_blank" href="//pro.jd.com/mall/active/3RmivHoTx4gKTRmWsB7moAKgBfy/index.html">中奖公示</a> 
						</li>
					</ul>
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
	</div></div>
    
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
                            <a href='//list.jd.com/list.html?cat=737,794,798&ev=exbrand_7888' clstag="shangpin|keycount|product|mbNav-4">海信（Hisense）</a>
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
                        <div class="item ellipsis" title="海信60E3F">海信60E3F</div>
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
                                                <a href="//mall.jd.com/index-1000324421.html?from=pc" target="_blank" title="海信京东自营旗舰店" clstag="shangpin|keycount|product|dianpuname1">海信京东自营旗舰店</a>
                                            </div>
                </div>
                                <div class="item hide J-im-item">
                    <div class="J-im-btn" clstag="shangpin|keycount|product|dongdong_1"></div>
                </div>
                <div class="item hide J-jimi-item">
                    <div class="J-jimi-btn" clstag="shangpin|keycount|product|jimi_1"></div>
                </div>
                                <div class="item">
                    <div class="follow J-follow-shop" data-vid="1000324421" clstag="shangpin|keycount|product|guanzhu">
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
                                <div class="qr-code J-m-qrcode" data-url="https://cd.jd.com/qrcode?skuId=100007300763&location=3&isWeChatStock=2">
                                    <div class="J-m-wrap"></div>
                                    <p>手机下单</p>
                                </div>
                            </div>
                                                        <div class="btns">
                                                                <a href="//mall.jd.com/index-1000324421.html?from=pc" target="_blank" class="btn-def enter-shop J-enter-shop" clstag="shangpin|keycount|product|jindian1">
                                    <i class="sprite-enter"></i><span>进店逛逛</span>
                                </a>
                                <span class="separator">|</span>
                                <a href="#none" class="btn-def follow-shop J-follow-shop" data-vid="1000324421" clstag="shangpin|keycount|product|guanzhu1">
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
                    <img id="spec-img" width="350" data-origin="//img13.360buyimg.com/n1/jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg" alt="海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源"/>
                                                                                                                        <div id="belt"></div>
                </div>
                                        <div class="video" id="v-video" data-vu="208690205">
                            <div class="J-v-player"></div>
                            <span class="video-icon J-video-icon" clstag="shangpin|keycount|product|picvideo"></span>
                            <a href="#none" class="close-video J-close hide" clstag="shangpin|keycount|product|closepicvideo"></a>
                        </div>
                                    <script>
                        (function(doc, cfg) {
                            var img = doc.getElementById('spec-img');
                            var src = img.getAttribute('data-origin');
                            var nsz = 300;

                            if ((!cfg.wideVersion || !cfg.compatible) && !cfg.product.ctCloth) {
                                img.setAttribute('width', nsz);
                                img.setAttribute('height', nsz);
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
                                                                                                                                                                        <li  class='img-hover'><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg' data-url='jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/115458/20/7603/248989/5ec4ac5dE44355ef8/8ee8971fc65581aa.jpg' data-url='jfs/t1/115458/20/7603/248989/5ec4ac5dE44355ef8/8ee8971fc65581aa.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/116103/7/7465/279371/5ec340b5E4e6ce00c/15467aed1a5d3efe.jpg' data-url='jfs/t1/116103/7/7465/279371/5ec340b5E4e6ce00c/15467aed1a5d3efe.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/127531/22/2139/146329/5ec340b5Ecb3029ea/1402a215f850faea.jpg' data-url='jfs/t1/127531/22/2139/146329/5ec340b5Ecb3029ea/1402a215f850faea.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/122819/32/2119/29369/5ec340b7E0083c727/d3f92961cecea9d6.jpg' data-url='jfs/t1/122819/32/2119/29369/5ec340b7E0083c727/d3f92961cecea9d6.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/120000/9/2129/126830/5ec340bdE6f67ee5b/7ddc12a5c7b98f4c.jpg' data-url='jfs/t1/120000/9/2129/126830/5ec340bdE6f67ee5b/7ddc12a5c7b98f4c.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/114640/28/7324/90205/5ec340bdEa755a676/5da479f20da8fcd7.jpg' data-url='jfs/t1/114640/28/7324/90205/5ec340bdEa755a676/5da479f20da8fcd7.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/137579/30/4682/104953/5f2cbdb7E8a140af5/f68b5e5b5cd23240.jpg' data-url='jfs/t1/137579/30/4682/104953/5f2cbdb7E8a140af5/f68b5e5b5cd23240.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/139687/7/4723/60700/5f2cbdb7E4bafed01/0844754e749f2c27.jpg' data-url='jfs/t1/139687/7/4723/60700/5f2cbdb7E4bafed01/0844754e749f2c27.jpg' data-img='1' width='54' height='54'></li>
                                                                        <li ><img alt='海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源' src='//img13.360buyimg.com/n5/jfs/t1/143700/25/4772/112584/5f2cbdbeEff43d1a0/8b7a2cff6e9f8854.jpg' data-url='jfs/t1/143700/25/4772/112584/5f2cbdbeEff43d1a0/8b7a2cff6e9f8854.jpg' data-img='1' width='54' height='54'></li>
                                                                                                </ul>
                        </div>
                    </div>
                    <div class="preview-info">
                        <div class="left-btns">
                            <a class="follow J-follow" data-id="100007300763" href="#none" clstag="shangpin|keycount|product|guanzhushangpin_1">
                                <i class="sprite-follow-sku"></i><em>关注</em>
                            </a>
                                                                                                                <a class="compare J-compare J_contrast" id="comp_100007300763" data-sku="100007300763" href="#none" clstag="shangpin|keycount|product|jiaruduibi">
                                <i class="sprite-compare"></i><em>对比</em>
                            </a>
                                                    </div>
                        <div class="right-btns">
                            <a class="report-btn" href="//jubao.jd.com/index.html?skuId=100007300763" target="_blank" clstag="shangpin|keycount|product|jubao">举报</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="itemInfo-wrap">
                <div class="sku-name">
                                                            海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源                </div>
                                <div class="news">
                    <div class="item hide" id="p-ad"></div>
                    <div class="item hide" id="p-ad-phone"></div>
                </div>

                <div id="yuyue-banner" class="activity-banner">
    <div class="activity-type">
        <i class="sprite-yy"></i><strong>预约抢购</strong>
    </div>
    <div class="activity-message">
        <span class="item J-item-1"><i class="sprite-person"></i><em class="J-count">0</em>人预约</span>
        <span class="item J-item-2 hide"><i class="sprite-time"></i><span class="J-text">剩余</span><em class="J-time"></em></span>
    </div>
</div>

                                <div class="summary summary-first">
    <div class="summary-price-wrap">
        <div class="summary-price J-summary-price">
                            <div class="dt">京 东 价</div>
                <div class="dd">
                    <span class="p-price"><span>￥</span><span class="price J-p-100007300763"></span></span>
                    <em class="yy-category J-yy-category hide"></em>
                </div>

                    </div>

        <div class="summary-info">
                        <span class="J-yuyue-tips pingou-tips"><a class="count J-tips" href="#none">预约说明</a></span>
                    </div>
                <div id="summary-quan" class="li p-choose hide" clstag="shangpin|keycount|product|lingquan" style="display: none"></div>
        <div id="J-summary-top" class="summary-top" clstag="shangpin|keycount|product|cuxiao">
            <div id="summary-promotion" class="hide summary-promotion">
                <div class="dt">促&#x3000;&#x3000;销</div>
                <div class="dd J-prom-wrap p-promotions-wrap">
                    <div class="p-promotions">
                        <ins id="prom-mbuy" data-url="https://cd.jd.com/qrcode?skuId=100007300763&location=3&isWeChatStock=2"></ins>
                        <ins id="prom-gift" clstag="shangpin|keycount|product|zengpin_1"></ins>
                        <ins id="prom-fujian" clstag="shangpin|keycount|product|fujian_1"></ins>
                        <ins id="prom"></ins>
                        <ins id="prom-one"></ins>
                        <ins id="prom-phone"></ins>
                        <ins id="prom-phone-jjg"></ins>
                        <ins id="prom-tips"></ins>
                        <ins id="prom-quan"></ins>
                        <div class="J-prom-more view-all-promotions">
                            <span class="prom-sum">展开促销</span>
                            <a href="#none" class="view-link"><i class="sprite-arr-close"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>


    </div>
</div>                                <div class="summary p-choose-wrap">
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
                                                            <div id="summary-yushou-ship" class="summary-yushou-ship li" style="display:none">
                        <div class="dt">发货时间</div>
                        <div class="dd"></div>
                    </div>
                                                            <div id="summary-weight" class="li" style="display: none;">
                        <div class="dt">重&#x3000;&#x3000;量</div>
                        <div class="dd"></div>
                    </div>
                                                                                <div class="SelfAssuredPurchase li" id="J_SelfAssuredPurchase" style="display:none;"></div>
                                        <div class="summary-line"></div>

                                        <div id="choose-attrs">
                                                                                                <div id="choose-attr-1" class="li p-choose" data-type="尺寸" data-idx="0">
                            <div class="dt ">选择尺寸                                                        </div>
                            <div class="dd">
                                                                <div class="item  " data-sku="100007637459" data-value="ULED超画质社交新品-65E9F">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-ULED超画质社交新品-65E9F">
                                                                                                                                    <img data-img="1" src="//img14.360buyimg.com/n9/s40x40_jfs/t1/120291/2/9797/189621/5f367eeaEa5d41cd4/2120936b14db4e88.jpg" width="40" height="40" alt="ULED超画质社交新品-65E9F"><i>ULED超画质社交新品-65E9F</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="100006060267" data-value="ULED量子点社交新品-65E8D">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-ULED量子点社交新品-65E8D">
                                                                                                                                    <img data-img="1" src="//img12.360buyimg.com/n9/s40x40_jfs/t1/140891/12/5610/241868/5f37f42dE207b48c1/0fda89019efea6a4.jpg" width="40" height="40" alt="ULED量子点社交新品-65E8D"><i>ULED量子点社交新品-65E8D</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="100007167317" data-value="高配游戏电视新品-65E75F">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-高配游戏电视新品-65E75F">
                                                                                                                                    <img data-img="1" src="//img12.360buyimg.com/n9/s40x40_jfs/t1/121518/9/9705/189727/5f37f4c5E3fa8b02a/75409abe87849591.jpg" width="40" height="40" alt="高配游戏电视新品-65E75F"><i>高配游戏电视新品-65E75F</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="100003525291" data-value="3+32G超音画全面屏-65E7D">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-3+32G超音画全面屏-65E7D">
                                                                                                                                    <img data-img="1" src="//img11.360buyimg.com/n9/s40x40_jfs/t1/142358/22/5510/291661/5f37f556E6b7b9906/61c51ad9001a5f1d.jpg" width="40" height="40" alt="3+32G超音画全面屏-65E7D"><i>3+32G超音画全面屏-65E7D</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="100007338003" data-value="3+32G社交电视新品-65E5F">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-3+32G社交电视新品-65E5F">
                                                                                                                                    <img data-img="1" src="//img13.360buyimg.com/n9/s40x40_jfs/t1/121129/1/9834/215020/5f37f51fEa0ce9d77/c1e397fd123026d6.jpg" width="40" height="40" alt="3+32G社交电视新品-65E5F"><i>3+32G社交电视新品-65E5F</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="100003525293" data-value="MEMC防抖超薄全面屏-65E5D">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-MEMC防抖超薄全面屏-65E5D">
                                                                                                                                    <img data-img="1" src="//img13.360buyimg.com/n9/s40x40_jfs/t1/148811/29/5594/252933/5f37f5b7E240e397a/1fa16a8c0ca763d6.jpg" width="40" height="40" alt="MEMC防抖超薄全面屏-65E5D"><i>MEMC防抖超薄全面屏-65E5D</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="100006254938" data-value="MEMC全面屏爆品-65E3D-PRO">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-MEMC全面屏爆品-65E3D-PRO">
                                                                                                                                    <img data-img="1" src="//img13.360buyimg.com/n9/s40x40_jfs/t1/148884/28/5540/146586/5f3682efE05b715ba/0946b0a29da627ca.jpg" width="40" height="40" alt="MEMC全面屏爆品-65E3D-PRO"><i>MEMC全面屏爆品-65E3D-PRO</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="100007826441" data-value="4K超薄悬浮全面屏新品-65E3F">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-4K超薄悬浮全面屏新品-65E3F">
                                                                                                                                    <img data-img="1" src="//img11.360buyimg.com/n9/s40x40_jfs/t1/150298/7/5145/197142/5f3398c2Ecaa2fed0/a0a302a8521b892b.jpg" width="40" height="40" alt="4K超薄悬浮全面屏新品-65E3F"><i>4K超薄悬浮全面屏新品-65E3F</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  " data-sku="8748165" data-value="4K智慧AI纤薄爆品-65E3A">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-4K智慧AI纤薄爆品-65E3A">
                                                                                                                                    <img data-img="1" src="//img10.360buyimg.com/n9/s40x40_jfs/t1/111190/28/14985/155439/5f3682a6E1792f29d/6d0a15cf4069ce0c.jpg" width="40" height="40" alt="4K智慧AI纤薄爆品-65E3A"><i>4K智慧AI纤薄爆品-65E3A</i>
                                                                                                                        </a>
                                                                    </div>
                                                                <div class="item  selected  " data-sku="100007300763" data-value="4K超薄全面屏爆品-60E3F">
                                    <b></b>
                                                                        <a href="#none" clstag="shangpin|keycount|product|yanse-4K超薄全面屏爆品-60E3F">
                                                                                                                                    <img data-img="1" src="//img13.360buyimg.com/n9/s40x40_jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg" width="40" height="40" alt="4K超薄全面屏爆品-60E3F"><i>4K超薄全面屏爆品-60E3F</i>
                                                                                                                        </a>
                                                                    </div>
                                                                                            </div>
                        </div>
                                                                        <div id="choose-results" class="li" style="display:none"><div class="dt">已选择</div><div class="dd"></div></div>
                                            </div>

                                                                                                                                            <div id="choose-type" class="li" style="display:none;">
                        <div class="dt">购买方式</div>
                        <div class="dd clearfix"> </div>
                    </div>
                    <div id="choose-type-hy" class="li" style="display:none;">
                        <div class="dt">合约类型</div>
                        <div class="dd clearfix"> </div>
                    </div>
                    <div id="choose-type-suit" class="li" style="display:none;">
                        <div class="dt">合约套餐</div>
                        <div class="dd clearfix">
                            <div class="item J-suit-trigger" clstag="shangpin|keycount|product|taocanleixing">
                                <i class="sprite-selected"></i>
                                <a href="#none" title="选择套餐与资费">选择套餐与资费</a>
                            </div>
                            <div class="fl" style="padding-top:5px;">
                                <span class="J-suit-tips hide">请选择套餐内容</span>
                                <span class="J-suit-resel J-suit-trigger hl_blue hide" href="#none">重选</span>
                            </div>
                        </div>
                    </div>
                    <div id="btype-tip" style="display:none;">&#x3000;您选择的地区暂不支持合约机销售！</div>

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

                                                            <div id="choose-service" class="li" style="display:none;">
                        <div class="dt" data-yb="new_yb_server"></div>
                        <div class="dd"></div>
                    </div>
                                                                                <div id="choose-service+" class="li" style="display:none;">
                        <div class="dt">京东服务</div>
                        <div class="dd"></div>
                    </div>
                                                                                                                                                                <div class="summary-line"></div>
                                        <div id="choose-btns" class="choose-btns clearfix">
                                            <div class="choose-amount" clstag="shangpin|keycount|product|goumaishuliang_1">
                            <div class="wrap-input">
                                <input class="text buy-num" onkeyup="setAmount.modify('#buy-num');" id="buy-num" value="1" data-max="200" />
                                <a class="btn-reduce" onclick="setAmount.reduce('#buy-num')" href="javascript:;">-</a>
                                <a class="btn-add" onclick="setAmount.add('#buy-num')" href="javascript:;">+</a>
                            </div>
                        </div>
                                                                        <div class="mobile-only clearfix J-mobile-only" style="display:none;">
                            <div class="qrcode fl" data-url="https://cd.jd.com/qrcode?skuId=100007300763&location=2&isWeChatStock=2"></div>
                            <div class="text lh">仅支持手机扫码参与抽签<br/>扫一扫，立即参与</div>
                        </div>
                                                <!--<a id="choose-btn-gift" class="btn-special1 btn-lg" style="display:none;" href="//cart.gift.jd.com/cart/addGiftToCart.action?pid=100007300763&pcount=1&ptype=1" class="btn-gift" clstag="shangpin|keycount|product|选作礼物购买_1"><b></b>选作礼物购买</a>-->
                                                <a href="#none" id="btn-reservation" onclick='log("product", "btn1-立即预约-yuyue", "100007300763")' class="btn-special1 btn-lg" style="display:none;">
                            立即预约                        </a>
                                                                                                                        <a id="btn-baitiao" class="btn-special2 btn-lg" style="display:none;" clstag="shangpin|keycount|product|dabaitiaobutton_737_794_798">打白条</a>
                                                                                                <span class="yuyue-share J-yuyue-share" clstag="shangpin|keycount|product|share-yuyue"><i class="sprite-share"></i>分享</span>
                                                                                                <!--<a href="#none" id="btn-notify" class="J-notify-stock btn-def btn-lg" style="display:none;" data-type="2" data-sku="100007300763" clstag="shangpin|keycount|product|daohuo_1">到货通知</a> -->
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
                                <a href='//mall.jd.com/index-1000324421.html?from=pc' target='_blank'>
                                    <img src='//img30.360buyimg.com/popshop/jfs/t1/106339/26/18608/12120/5e95789bE393595b8/e3855b83258cddbe.jpg' title='海信京东自营旗舰店'/>
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
    <div id="yuyue-process" class="yy-process">
        <h3>预约抢购流程</h3>
        <div class="item item1">
            <i class="sprite-yy-step1"></i>
            <dl>
                <dt>1.等待预约</dt>
                <dd class="J-step1">预约即将开始</dd>
            </dl>
            <span class="sprite-arrow"></span>
        </div>
        <div class="item item2">
            <i class="sprite-yy-step2"></i>
            <dl>
                <dt>2.预约中</dt>
                <dd class="J-step2">-</dd>
            </dl>
            <span class="sprite-arrow"></span>
        </div>
        <div class="item item3">
            <i class="sprite-yy-step3"></i>
            <dl>
                <dt>3.等待抢购</dt>
                <dd class="J-step3">抢购即将开始</dd>
            </dl>
        </div>
        <div class="item item4">
            <i class="sprite-yy-step4"></i>
            <dl>
                <dt>4.抢购中</dt>
                <dd class="J-step4">-</dd>
            </dl>
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
                                <img data-img="1" src="//img14.360buyimg.com/n4/jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg" width="100" height="100" alt="海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源"/>
                            </a>
                        </div>
                        <div class="p-name">
                            <a href="//item.jd.com/100007300763.html" target="_blank">海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源</a>
                        </div>
                        <div class="p-price hide">
                            <input type="checkbox" data-sku="100007300763" id="inp-acc-master" checked/>
                            <label for="inp-acc-master"><strong class="J-p-100007300763">￥</strong></label>
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
                        <a href="#none" class="btn-primary J-btn"  onclick='log("gz_item", "gz_detail","02","tjpj_ycgm_ljgm", pageConfig.getAccSelectedSkus(),"main")'>立即购买</a>
                    </div>
                                                                <a href="//kong.jd.com/index?sku=100007300763&cid=798" target="_blank" class="acc-buy-center" onclick='log("gz_item", "gz_detail","02","tjpj_gdpj","","main")'>配件选购中心</a>
                                        <i class="equal">=</i>
                </div>
            </div>
        </div>
    </div>
                <div class="w">
        <div class="aside">
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

<div class="m m-aside yuyue-reco hide" id="yuyue-reco">
    <div class="mt"><h3>火热预约</h3></div>
    <div class="mc" clstag="shangpin|keycount|product|side-reco-yuyue"></div>
</div>
<div class="m m-aside" id="view-view" clstag="shangpin|keycount|product|seemore_1"></div>

<div id="miaozhen7886" class="m m-aside" clstag="shangpin|keycount|product|ad_1"></div>
<div id="miaozhen10767" class="m m-aside" clstag="shangpin|keycount|product|ad_1"></div>
<div id="sp-ad" class="m m-aside hide">
</div>

<div id="ad_market_1" class="m m-aside"></div>
        </div>
        <div class="detail">
                        <div class="ETab" id="detail">
                <div class="tab-main large" data-fixed="pro-detail-hd-fixed">
                    <ul>
                        <li data-tab="trigger" data-anchor="#detail" class="current" clstag="shangpin|keycount|product|shangpinjieshao_1">商品介绍</li>
                                                <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|pcanshutab">规格与包装</li>
                                                <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|psaleservice">售后保障</li>
                        <li data-tab="trigger" data-offset="38" data-anchor="#comment" clstag="shangpin|keycount|product|shangpinpingjia_1">商品评价<s></s></li>
                                                
                                                <li data-tab="trigger" data-anchor="#detail" id="pingou-rules-tab" clstag="shangpin|keycount|product|notice-yuyue">
                            预约说明
                        </li>
                                            </ul>
                    <div class="extra">
                        <div class="item addcart-mini">
                            <div class="J-addcart-mini EDropdown">
                                <div class="inner">
                                    <div class="head" data-drop="head">
                                                                                <a id="btn-reservation-mini" class="btn-primary" style="display:none;" href="#none" onclick='log("product", "btn2-立即预约-yuyue", "100007300763")'>
                                            立即预约                                        </a>
                                                                            </div>
                                    <div class="content hide" data-drop="content">
                                        <div class="mini-product-info">
                                            <div class="p-img fl">
                                                <img src="//img13.360buyimg.com/n4/jfs/t1/128105/3/9469/200006/5f368247E7cfca402/9d8a94fd1d2b55ce.jpg" data-img="1" width="100" height="100" />
                                            </div>
                                            <div class="p-info lh">
                                                <div class="p-name">海信（Hisense）60E3F 60英寸 4K超清 HDR 智慧语音 DTS音效 超薄悬浮全面屏 液晶平板电视机 教育资源</div>
                                                <div class="p-price">
                                                    <strong class="J-p-100007300763"></strong> <span>X <span class="J-buy-num"></span></span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="tab-con">
                    <div data-tab="item">
                        <div class="p-parameter">
                                                                                    <ul id="parameter-brand" class="p-parameter-list">
                                <li title='海信（Hisense）'>品牌： <a href='//list.jd.com/list.html?cat=737,794,798&ev=exbrand_7888' clstag='shangpin|keycount|product|pinpai_1' target='_blank'>海信（Hisense）</a>
                                    <!-- href="#none" clstag='shangpin|keycount|product|guanzhupinpai' class="follow-brand btn-def"><b>&hearts;</b>关注-->
                                </li>
                            </ul>
                                                        <ul class="parameter2 p-parameter-list">
                                    <li title='海信60E3F'>商品名称：海信60E3F</li>
    <li title='100007300763'>商品编号：100007300763</li>
                         <li title='21.0kg'>商品毛重：21.0kg</li>
            <li title='中国大陆'>商品产地：中国大陆</li>
                                    <li title='58-60英寸'>屏幕尺寸：58-60英寸</li>
                  <li title='三级能效'>能效等级：三级能效</li>
                  <li title='线上专供'>产品渠道：线上专供</li>
                  <li title='新品电视'>用户优选：新品电视</li>
                  <li title='全面屏，人工智能，教育电视，超薄，4K超清'>电视类型：全面屏，人工智能，教育电视，超薄，4K超清</li>
                  <li title='3m-3.5m（56-65英寸）'>观看距离：3m-3.5m（56-65英寸）</li>
                  <li title='10.0-8.0'>选购指数：10.0-8.0</li>
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
                        <div id="J-detail-banner"></div>                                                                        <div id="activity_header" clstag="shangpin|keycount|product|activityheader"></div>
                                                                        <div id="J-detail-pop-tpl-top-new" clstag="shangpin|keycount|product|pop-glbs">
                                                    </div>

                        <div class="detail-content clearfix" data-name="z-have-detail-nav">
                            <div class="detail-content-wrap">
                                                                                                
                                <div class="detail-content-item">
                                                                        <div id="J-detail-content">
                                        <div class="loading-style1"><b></b>商品介绍加载中...</div>                                    </div><!-- #J-detail-content -->
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
        <h3>端口参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>USB2.0接口</dt><dd>2</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>HDMI2.0接口</dt><dd>2</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>USB支持格式</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>USB支持音频格式</dt><dd>aac.flac.mp3.wav</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>USB支持图片格式</dt><dd>JPEG/PNG/BMP</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>USB支持视频格式</dt><dd>.avi .mpg .ts .mkv .mp4 .flv .mov .rm .rmvb</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>规格参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>单屏重量（kg）</dt><dd>14.5</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>外包装尺寸（宽*高*厚）mm</dt><dd>1501×920×149</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>单屏尺寸（宽*高*厚）mm</dt><dd>1353×780×74</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>含底座重量（kg）</dt><dd>14.7</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>含外包装重量（kg）</dt><dd>21</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>含底座尺寸（宽*高*厚）mm</dt><dd>1353×843×291</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>功耗参数</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>电源功率（w）</dt><dd>145</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>待机功率（w）</dt><dd><0.5W</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>工作电压（v）</dt><dd>220v</dd>
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
                                  <dt>运行内存</dt><dd>1.5GB</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>操作系统</dt><dd>Android 9</dd>
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
                  <dd>ARM Cortex A53*4 MAX1.4GHz</dd>
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
                  <dd> 2核Mali-G52</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>存储内存</dt><dd>8GB</dd>
                            </dl>
                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>外观设计</h3>
        <dl>
                                  <dl class="clearfix" style="margin:0">
                                  <dt>底座材料</dt><dd>全塑</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>机身厚薄</dt><dd>最薄处厚度8.56mm</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>安装孔距</dt><dd>300*200</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>边框材质</dt><dd>塑料</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>边框宽窄</dt><dd>边框宽度(上/左右/下)0/0/19.8mm</dd>
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
                                  <dt>产品颜色</dt><dd>黑色</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>产品类型</dt><dd>全面屏电视；人工智能电视；大屏电视；超薄电视；4K超清电视</dd>
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
                  <dd>60E3F</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>产品品牌</dt><dd>海信（Hisense）</dd>
                            </dl>
                                              <dl class="clearfix" style="margin:0">
                                  <dt>产品型号</dt><dd>60E3F</dd>
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
                                  <dt>屏幕尺寸</dt><dd>60英寸</dd>
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
                                              <dl class="clearfix" style="margin:0">
                                  <dt>刷屏率</dt><dd>60HZ</dd>
                            </dl>
                              </dl>
      </div>
      </div>
                                                <div class="package-list">
                            <h3>包装清单</h3>
                            <p>使用说明书*1，遥控器*1，音视频转接线*1 ,底座组件A*1，底座组件B*1，螺钉*4,7号电池*2</p>
                        </div>
                    </div>
                                                            <div data-tab="item" class="hide">
                        <!--售后保障-->
                    </div>
                    <div data-tab="item" class="hide">
                        <!--商品评价-->
                    </div>
                                        
                                            <div data-tab="item" class="hide">
    <!--拼购/预售说明-->
    <div class="pingou-rules">
            <h3>预约规则：</h3>
        <ol>
            <li>1、部分商品预约成功后才有抢购资格，预约成功后，请关注抢购时间及时抢购，货源有限，先抢先得！</li>
            <li>2、部分商品在预约期间抢购时间未定，我们会在商品开抢前通过Push通知提醒您，请在设置中选择允许通知，以免错过抢购时间。</li>
            <li>3、对于预约成功享优惠的商品，预约用户可获得优惠券或专属优惠。优惠券在抢购开始后使用，使用时间以优惠券有效期为准；专属优惠在抢购开始后，点击“立即抢购”将商品加入购物车，可在购物车查看优惠，若抢购时间结束，优惠自动失效。</li>
            <li>4、查看预约商品请至“我的京东”-“我的预售”-“我的预约”进行查看。</li>
            <li>5、如果提供赠品，赠品赠送顺序按照预约商品购买成功时间来计算，而不是预约成功时间。</li>
            <li>6、如您对活动有任何疑问，请联系客服咨询。</li>
        </ol>
        </div>
</div>                                    </div>
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
                                                                            本产品全国联保，享受三包服务，质保期为：1年质保<br/>
                                                                                                            本产品提供上门安装调试、提供上门检测和维修等售后服务，自收到商品之日起，如您所购买家电商品出现质量问题，请先联系厂家进行检测，凭厂商提供的故障检测证明，在“我的京东-客户服务-返修退换货”页面提交退换申请，将有专业售后人员提供服务。京东承诺您：30天内产品出现质量问题可退货，180天内产品出现质量问题可换货，超过180天按国家三包规定享受服务。<br />
                                                                                    您可以查询本品牌在各地售后服务中心的联系方式，<a target='_blank' href='http://www.hisense.com'>请点击这儿查询......</a><br/><br/>
            品牌官方网站：<a target='_blank' href='http://www.hisense.com'>http://www.hisense.com</a><br/>
                                    售后服务电话：400-611-1111                                </dd>
                                <dt>
            <i class="goods"></i>
            <strong>京东承诺</strong>
        </dt>
        <dd>
                            京东平台卖家销售并发货的商品，由平台卖家提供发票和相应的售后服务。请您放心购买！<br />
                                        注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！
        </dd>
                                <dt>
            <i class="goods"></i><strong>正品行货</strong>
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
                                    <!--<div id="askAnswer" class="m m-content askAnswer hide">
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
            </div>-->
                        <div id="try-report" class="try-report"></div>
                        <div class="m m-content consult" id="consult">
                <div class="mt">
                    <h3 class="fl">购买咨询</h3>

                    <div class="extra">
                        <div class="item">
                                                                                    <a href="//club.jd.com/allconsultations/100007300763-1-1.html#form1" target="_blank" class="btn-primary">发表咨询</a>
                                                    </div>
                        <div class="item">
                            <div class="J-jimi-btn" clstag="shangpin|keycount|product|consult12"></div>
                        </div>
                        <div class="item">
                            <div class="J-im-btn" clstag="shangpin|keycount|product|consult11"></div>
                        </div>
                    </div>
                </div>
                <div class="mc">
                    <div class="ETab consult">
                        <div class="tab-main small">
                            <ul>
                                <li data-tab="trigger" class="current" clstag="shangpin|keycount|product|consult01">全部</li>
                                <li data-tab="trigger" clstag="shangpin|keycount|product|consult02">商品咨询</li>
                                <li data-tab="trigger" clstag="shangpin|keycount|product|consult03">库存配送</li>
                                <li data-tab="trigger" clstag="shangpin|keycount|product|consult04">支付</li>
                                <li data-tab="trigger" clstag="shangpin|keycount|product|consult05">发票保修</li>
                                <li data-tab="trigger" style="display:none"></li>
                            </ul>
                        </div>
                        <div class="tab-con">
                            <div class="search">
                                <p>温馨提示：因每位咨询者购买情况、咨询时间等不同，以下回复对咨询者3天内有效，其他网友仅供参考。</p>
                                <div class="search-from">
                                    <input id="txbReferSearch" class="s-text" type="text" placeholder="输入关键词" />
                                    <button id="btnReferSearch" clstag="shangpin|keycount|product|consult09"><i></i>搜索</button>
                                </div>
                                <div data-tab="item" class="search-list">
                                    <div class="loading-style1"><b></b>加载中，请稍候...</div>
                                </div>
                                <div data-tab="item" class="search-list hide">
                                    <div class="loading-style1"><b></b>加载中，请稍候...</div>
                                </div>
                                <div data-tab="item" class="search-list hide">
                                    <div class="loading-style1"><b></b>加载中，请稍候...</div>
                                </div>
                                <div data-tab="item" class="search-list hide">
                                    <div class="loading-style1"><b></b>加载中，请稍候...</div>
                                </div>
                                <div data-tab="item" class="search-list hide">
                                    <div class="loading-style1"><b></b>加载中，请稍候...</div>
                                </div>
                                <div data-tab="item" class="search-list hide">
                                    <div class="loading-style1"><b></b>加载中，请稍候...</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
                                                        </div>
        <div class="clb"></div>
    </div>
        
    <div id="placeholder-floatnav-stop"></div>

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
    
                <div id="GLOBAL_FOOTER"></div>
        <script>
                seajs.use('MOD_ROOT/main/main.js', function (App) {
            App.init(pageConfig.product);
        });


                                function totouchbate() {
  var exp = new Date();
  exp.setTime(exp.getTime() + 30 * 24 * 60 * 60 * 1000);
  document.cookie = "pcm=2;expires=" + exp.toGMTString() + ";path=/;domain=jd.com";
    window.location.href="//item.m.jd.com/product/100007300763.html";
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
</script>        <div id="J-global-toolbar"></div>
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