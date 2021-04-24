#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from projects.autopkgcapture.core.core import AppWraper, weichat_xiaochengxu
import time


def test():
    wechat_andriod = {'app_id':1,
        'desired_capabilities':{
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    },'actions':[{'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/he6').click(), 'id':1, 'delay':10, 'desc':'点击搜索'},
                 {'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/bxz').send_keys('文件传输助手'), 'id':2, 'delay':10, 'desc':'输入搜索内容'},
                 {'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/ir3').click(), 'id':3, 'delay':10, 'desc':'点击搜索到的内容'},
                 {'function': lambda driver: driver.find_element_by_id('com.tencent.mm:id/auj').send_keys('hello'), 'id': 4,'delay': 10, 'desc': '输入文字'},
                 {'function': lambda driver: driver.find_element_by_id('com.tencent.mm:id/ay9').click(),'id': 5, 'delay': 10, 'desc': '打开表情'},
                 {'function': lambda driver: driver.find_element_by_id('com.tencent.mm:id/ur').click(),'id': 6, 'delay': 10, 'desc': '选择表情'},
                 {'function': lambda driver: driver.find_element_by_id('com.tencent.mm:id/ay5').click(),'id': 7, 'delay': 10, 'desc': '发送信息'},
                 ]}

    jd_wechat_andriod = {'app_id':3,
        'desired_capabilities':{
        'automationName': 'uiautomator2',
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": False,
        'chromeOptions': {'androidProcess':'com.tencent.mm:appbrand0'}
    },'actions':[{'function':weichat_xiaochengxu("京东购物"), 'id':1, 'delay':10, 'desc':'打开小程序京东购物'}]}

    app_infos = [
        {'app_id': 1, 'app_name': '淘宝', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.taobao.taobao",
             "appActivity": "com.taobao.tao.welcome.Welcome",
             "bundleId": "com.soyoung.qingyang.medical",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True,
             #'adbExecTimeout':200000
         }, 'actions': []},
        {'app_id': 2, 'app_name': '京东',
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.jingdong.app.mall",
             "appActivity": "com.jingdong.app.mall.main.MainActivity",
             "bundleId": "com.360buy.jdmobile",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id':3,'app_name':'高徒课堂','platform':"Android",
            'desired_capabilities':{
            "platformName": "Android",
            "platformVersion": "10.0",
            "deviceName": "Q7PRX18B21019283",
            "appPackage": "com.gaotu100.superclass",
            "appActivity": "com.gaotu100.superclass.activity.main.SplashActivity",
                "bundleId": "com.gaotu100.superclass",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        },'actions':[]},
        {'app_id':4,'app_name':'跟谁学','platform':"Android",
            'desired_capabilities':{
            "platformName": "Android",
            "platformVersion": "10.0",
            "deviceName": "Q7PRX18B21019283",
            "appPackage": "com.genshuixue.student",
            "appActivity": "com.genshuixue.student.ui.LauncherActivity",
                "bundleId": "com.bjhl.student",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        },'actions':[]},
        {'app_id': 5, 'app_name': '学而思网校', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.xueersi.parentsmeeting",
             "appActivity": "com.xueersi.parentsmeeting.module.home.LaunchActivity",
             "bundleId": "com.xueersi.wxjzh",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id':6,'app_name':'作业帮','platform':"Android",
            'desired_capabilities':{
            "platformName": "Android",
            "platformVersion": "10.0",
            "deviceName": "Q7PRX18B21019283",
            "appPackage": "com.baidu.homework",
            "appActivity": "com.baidu.homework.activity.init.InitActivity",
                "bundleId": "com.baidu.homework",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        },'actions':[]},
        {'app_id':7,'app_name':'作业帮直播课','platform':"Android",
            'desired_capabilities':{
            "platformName": "Android",
            "platformVersion": "10.0",
            "deviceName": "Q7PRX18B21019283",
            "appPackage": "com.zuoyebang.airclass",
            "appActivity": "com.baidu.homework.activity.init.InitActivity",
                "bundleId": "com.zuoyebang.student",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        },'actions':[]},
        {'app_id': 8, 'app_name': '猿辅导', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.yuantiku.tutor",
             "appActivity": "com.yuanfudao.tutor.activity.HomeActivity",
             "bundleId": "com.fenbi.tutor",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 9, 'app_name': '有道精品课', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.youdao.course",
             "appActivity": "com.youdao.course.activity.StartJumperActivity",
             "bundleId": "com.youdao.xuetang",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 10, 'app_name': '抖音', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.ugc.aweme",
             "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
             "bundleId": "com.ss.iphone.ugc.Aweme",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 11, 'app_name': '抖音极速版', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.ugc.aweme.lite",
             "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
             "bundleId": "com.ss.iphone.ugc.aweme.lite",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 12, 'app_name': '抖音火山版', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.ugc.live",
             "appActivity": "com.ss.android.ugc.live.main.MainActivity",
             "bundleId": "com.ss.iphone.ugc.Live",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 13, 'app_name': '快手', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.smile.gifmaker",
             "appActivity": "com.yxcorp.gifshow.HomeActivity",
             "bundleId": "com.jiangjia.gif",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 14, 'app_name': '快手极速版', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.kuaishou.nebula",
             "appActivity": "com.yxcorp.gifshow.HomeActivity",
             "bundleId": "com.kuaishou.nebula",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 15, 'app_name': '哔哩哔哩', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "tv.danmaku.bili",
             "appActivity": "tv.danmaku.bili.ui.splash.SplashActivity",
             "bundleId": "tv.danmaku.bilianime",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 16, 'app_name': '知乎', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.zhihu.android",
             "appActivity": "com.zhihu.android.app.ui.activity.LauncherActivity",
             "bundleId": "com.zhihu.ios",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 17, 'app_name': '微博', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.sina.weibo",
             "appActivity": "com.sina.weibo.SplashActivity",
             "bundleId": "com.sina.weibo",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 18, 'app_name': '拼多多', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.xunmeng.pinduoduo",
             "appActivity": "com.xunmeng.pinduoduo.ui.activity.MainFrameActivity",
             "bundleId": "com.xunmeng.pinduoduo",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 19, 'app_name': '美团', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.sankuai.meituan",
             "appActivity": "com.meituan.android.pt.homepage.activity.MainActivity",
             "bundleId": "com.meituan.imeituan",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 20, 'app_name': '嘀嘀出行', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             'udid':'R8PFLJHUZH5P7LNF',
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.sdu.didi.psnger",
             "appActivity": "com.didi.sdk.app.launch.splash.SplashActivity",
             "bundleId": "com.xiaojukeji.didi",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 21, 'app_name': '今日头条', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.article.news",
             "appActivity": "com.ss.android.article.news.activity.MainActivity",
             "bundleId": "com.ss.iphone.article.News",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 22, 'app_name': '汽车之家', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.cubic.autohome",
             "appActivity": "com.cubic.autohome.MainActivity",
             "bundleId": "com.autohome",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 23, 'app_name': '懂车帝', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.auto",
             "appActivity": "com.ss.android.auto.policy.AutoPrivacyActivity",
             "bundleId": "com.ss.ios.auto",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 24, 'app_name': '花小猪打车', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.huaxiaozhu.rider",
             "appActivity": "com.huaxiaozhu.sdk.app.launch.LauncherActivity",
             "bundleId": "com.huaxiaozhu.rider",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 25, 'app_name': '滴答出行', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.didapinche.booking",
             "appActivity": "com.didapinche.booking.home.activity.StartActivity",
             "bundleId": "com.didapinche.taxi",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 26, 'app_name': '贝壳找房', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.lianjia.beike",
             "appActivity": "com.lianjia.activity.MainActivity",
             "bundleId": "com.lianjia.beike",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 27, 'app_name': '安居客', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.anjuke.android.app",
             "appActivity": "com.anjuke.android.app.mainmodule.WelcomeActivity",
             "bundleId": "com.anjuke.anjuke",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 28, 'app_name': '叮咚买菜', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.yaya.zone",
             "appActivity": "com.yaya.zone.activity.SplashActivity",
             "bundleId": "com.mmbang.neighborhood",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 29, 'app_name': '每日优鲜', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "cn.missfresh.application",
             "appActivity": "cn.missfresh.module.main.view.SplashActivity",
             "bundleId": "cn.missfresh.application",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 30, 'app_name': '盒马', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.wudaokou.hippo",
             "appActivity": "com.wudaokou.hippo.launcher.splash.SplashActivity",
             "bundleId": "com.wdk.hmxs",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 31, 'app_name': '美团外卖', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.sankuai.meituan.takeoutnew",
             "appActivity": "com.sankuai.meituan.takeoutnew.ui.page.boot.WelcomeActivity",
             "bundleId": "com.meituan.itakeaway",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 32, 'app_name': '大众点评', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.dianping.v1",
             "appActivity": "com.dianping.v1.NovaMainActivity",
             "bundleId": "com.dianping.dpscope",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 33, 'app_name': '饿了么', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "me.ele",
             "appActivity": "me.ele.Launcher",
             "bundleId": "me.ele.ios.eleme ",
             "noReset": True,
             "automationName":"uiautomator2",
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 34, 'app_name': '京喜', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.jd.pingou",
             "appActivity": "com.jd.pingou.MainActivity",
             "bundleId": "com.360buy.jdpingou",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 35, 'app_name': '唯品会', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.achievo.vipshop",
             "appActivity": "com.achievo.vipshop.activity.LodingActivity",
             "bundleId": "com.vipshop.iphone",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 36, 'app_name': '淘宝特价版', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.taobao.litetao",
             "appActivity": "com.taobao.ltao.maintab.MainFrameActivity",
             "bundleId": "com.taobao.special",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 37, 'app_name': '天猫', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.tmall.wireless",
             "appActivity": "com.tmall.wireless.splash.TMSplashActivity",
             "bundleId": "com.taobao.tmall",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 38, 'app_name': '拼多多商家版', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.xunmeng.merchant",
             "appActivity": "com.xunmeng.merchant.ui.SplashActivity",
             "bundleId": "com.xunmeng.merchant",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 39, 'app_name': '爱彼迎', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.airbnb.android",
             "appActivity": "com.airbnb.android.feat.homescreen.HomeActivity",
             "bundleId": "com.airbnb.app",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 40, 'app_name': '携程', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "ctrip.android.view",
             "appActivity": "ctrip.business.splash.CtripSplashActivity",
             "bundleId": "ctrip.com",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 41, 'app_name': '飞猪', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.taobao.trip",
             "appActivity": "com.alipay.mobile.quinox.LauncherActivity",
             "bundleId": "com.taobao.travel",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 42, 'app_name': '新氧', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.youxiang.soyoungapp",
             "appActivity": "com.soyoung.module_main.ui.SplashActivity",
             "bundleId": "com.soyoung.qingyang.medical",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 43, 'app_name': '京东健康', 
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.jd.jdhealth",
             "appActivity": "com.jd.jdhealth.ui.activity.SplashActivity",
             "bundleId":"com.jd.jdhealth",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": False,
             'takesScreenshot':False,
         }, 'actions': []},
    ]

    devic_infos = [{'udid': 'R8PFLJHUZH5P7LNF','platformName': "Android","platformVersion": "10.0",'deviceName': 'oppo reno4 se',"server_port": "4723", 'restart_wifi':'false', 'mode':'usb','wifiudid':'192.168.50.111:5555','record_enable':True},
                   {'udid': 'Q7PRX18B21019283', 'platformName': "Android","platformVersion": "10.0",'deviceName': 'rongyao', "server_port": "4724", 'mode':'usb','wifiudid':'192.168.50.160:5555','record_enable':True},
                   {'udid': 'U4QSYDWC8X4LYDCM', 'platformName': "Android","platformVersion": "10.0",'deviceName': 'vivo icoo u3', "server_port": "4725", 'restart_wifi': 'false', 'mode':'usb','wifiudid':'192.168.50.120:5555','record_enable':True},
                   {'udid': 'd80f6d476f0aace3d4ebc0a10ba6b056bd7e9d3f', 'platformName': "iOS","platformVersion": "14.3",'deviceName': 'Jicheng的iPhoneX','record_enable':False}]
    import random
    app_infos = random.choices(app_infos)[0:31]
    for devic_info in devic_infos[:-1]:
        try:
            for app_info in app_infos[:]:
                app = AppWraper(app_info, devic_info=devic_info)
                app.run()
        except:
            import traceback
            traceback.print_exc()
            pass



for epoch in range(10000):
    test()
