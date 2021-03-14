#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from projects.autopkgcapture.core.core import App

def get_size(driver):
    x_y = driver.get_window_size()
    return (x_y['width'], x_y['height'])

def swip_down(driver, t=1):
    screen = get_size(driver)
    driver.swipe(screen[0]*0.5,screen[1]*0.25,screen[0]*0.5,screen[1]*0.75, t)

def test():
    taobao_andriod = {'app_id':2,
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
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    },'actions':[{'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/he6').click(), 'id':1, 'delay':5, 'desc':'点击搜索'},
                 {'function': lambda driver: driver.find_element_by_id('com.tencent.mm:id/il2').click(), 'id': 2, 'delay': 5, 'desc': '点击搜索'},
                 {'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/bxz').send_keys('京东'), 'id':3, 'delay':10, 'desc':'输入搜索内容'},
                 {'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/ir3').click(), 'id':4, 'delay':10, 'desc':'点击搜索到的内容'},
                 ]}

    jd_wechat_andriod = {'app_id':4,
        'desired_capabilities':{
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Q7PRX18B21019283",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    },'actions':[{'function':lambda driver: driver.find_element_by_id('com.tencent.mm:id/dtx').click(), 'id': 2, 'delay': 5, 'desc': '点击搜索'},
                 {'function':lambda driver: driver.find_element_by_id('com.tencent.mm:id/dvz').click(), 'id': 2, 'delay': 5, 'desc': '点击搜索'},
                 {'function': lambda driver: driver.find_element_by_id('com.tencent.mm:id/d8').click(), 'id': 2, 'delay': 5, 'desc': '点击搜索'},
                 {'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/ipm').send_keys('京东'), 'id':3, 'delay':10, 'desc':'输入搜索内容'},
                 {'function':lambda driver : driver.find_element_by_id('com.tencent.mm:id/ir3').click(), 'id':4, 'delay':10, 'desc':'点击搜索到的内容'},
                 ]}
    app = App(jd_wechat_andriod)
    app.run()

test()