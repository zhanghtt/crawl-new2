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
    taobao_andriod = {'app_id':1,
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
    jd_andriod = {'app_id':2,
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
        "resetKeyboard": True,
        'chromeOptions': {'androidProcess':'com.tencent.mm:appbrand0'}
    },'actions':[{'function':weichat_xiaochengxu("京东购物"), 'id':1, 'delay':5, 'desc':'打开小程序京东购物'}]}

    app = App(jd_wechat_andriod)
    app.run()

test()