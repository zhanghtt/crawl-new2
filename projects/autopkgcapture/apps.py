#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from projects.autopkgcapture.core.core import App,weichat_xiaochengxu
import time
apps = [{'app_id':1,
        'desired_capabilities':{
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.taobao.taobao",
        "appActivity": "com.taobao.tao.welcome.Welcome",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    },'actions':[]},
        {'app_id': 2,
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.jingdong.app.mall",
             "appActivity": "com.jingdong.app.mall.main.MainActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
{'app_id':1,
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
                 ]},
{'app_id':3,
        'desired_capabilities':{
        'automationName': 'uiautomator2',
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        'chromeOptions': {'androidProcess':'com.tencent.mm:appbrand0'}
    },'actions':[{'function':weichat_xiaochengxu("京东购物"), 'id':1, 'delay':5, 'desc':'点击搜索'}]}
        ]
def test():
    taobao_andriod = {'app_id':1,'app_name':'淘宝','platform':"Android",
        'desired_capabilities':{
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.taobao.taobao",
        "appActivity": "com.taobao.tao.welcome.Welcome",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    },'actions':[]}
    jd_andriod = {'app_id':2,'app_name':'京东','platform':"Android",
        'desired_capabilities':{
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.jingdong.app.mall",
        "appActivity": "com.jingdong.app.mall.main.MainActivity",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    },'actions':[]}
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

    apps = [
        {'app_id': 1, 'app_name': '淘宝', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.taobao.taobao",
             "appActivity": "com.taobao.tao.welcome.Welcome",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 2, 'app_name': '京东', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.jingdong.app.mall",
             "appActivity": "com.jingdong.app.mall.main.MainActivity",
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
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        },'actions':[]},
        {'app_id': 5, 'app_name': '学而思网校', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.xueersi.parentsmeeting",
             "appActivity": "com.xueersi.parentsmeeting.module.home.LaunchActivity",
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
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        },'actions':[]},
        {'app_id': 8, 'app_name': '猿辅导', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.yuantiku.tutor",
             "appActivity": "com.yuanfudao.tutor.activity.HomeActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 9, 'app_name': '有道精品课', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.youdao.course",
             "appActivity": "com.youdao.course.activity.StartJumperActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 10, 'app_name': '抖音', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.ugc.aweme",
             "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 11, 'app_name': '抖音极速版', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.ugc.aweme.lite",
             "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 12, 'app_name': '抖音火山版', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.ugc.live",
             "appActivity": "com.ss.android.ugc.live.main.MainActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 13, 'app_name': '快手', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.smile.gifmaker",
             "appActivity": "com.yxcorp.gifshow.HomeActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 14, 'app_name': '快手极速版', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.kuaishou.nebula",
             "appActivity": "com.yxcorp.gifshow.HomeActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 15, 'app_name': '哔哩哔哩', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "tv.danmaku.bili",
             "appActivity": "tv.danmaku.bili.ui.splash.SplashActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 16, 'app_name': '知乎', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.zhihu.android",
             "appActivity": "com.zhihu.android.app.ui.activity.LauncherActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 17, 'app_name': '微博', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.sina.weibo",
             "appActivity": "com.sina.weibo.SplashActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 18, 'app_name': '拼多多', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.xunmeng.pinduoduo",
             "appActivity": "com.xunmeng.pinduoduo.ui.activity.MainFrameActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 19, 'app_name': '美团', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.sankuai.meituan",
             "appActivity": "com.meituan.android.pt.homepage.activity.MainActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 20, 'app_name': '嘀嘀出行', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.sdu.didi.psnger",
             "appActivity": "com.didi.sdk.app.launch.splash.SplashActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
        {'app_id': 21, 'app_name': '今日头条', 'platform': "Android",
         'desired_capabilities': {
             "platformName": "Android",
             "platformVersion": "10.0",
             "deviceName": "Q7PRX18B21019283",
             "appPackage": "com.ss.android.article.news",
             "appActivity": "com.ss.android.article.news.activity.MainActivity",
             "noReset": True,
             "unicodeKeyboard": True,
             "resetKeyboard": True
         }, 'actions': []},
    ]
    try:
        for app_info in apps:
            app = App(app_info)
            app.run()
    except:
        import traceback
        traceback.print_exc()
        pass

test()