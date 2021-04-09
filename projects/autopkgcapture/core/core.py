#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, unittest
from appium import webdriver
import socket
import uuid
from urllib3.util.retry import MaxRetryError
import wda


def swipe_down(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)


def weichat_xiaochengxu(applabel):
    def run(driver, app, action):
        swipe_down(driver)
        time.sleep(5)
        app.change_action("app_{}_action_{}_{}".format(app.app_info['app_id'], str(action['id']),
                                                        str(uuid.uuid1())))  # open app id is -1
        driver.find_element_by_android_uiautomator('text("{}")'.format(applabel)).click()
    run.__name__ = "weichat_xiaochengxu"
    return run

class IOSApp:
    def __init__(self, app_info, devic_info, **kwargs):
        self.delay_time = 3
        self.app_info = app_info
        self.devic_info = devic_info
        self.desired_caps = app_info['desired_capabilities']
        self.desired_caps['deviceName'] = devic_info['deviceName']
        self.desired_caps['udid'] = devic_info['wifiudid']
        self.actions = app_info['actions']
        self.driver = wda.Client("http://localhost:8100")
        self.session = None
        self.dns_proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dns_proxy_socket.settimeout(100000)

    def setup(self):
        pass

    def cleanup(self):
        pass

    def change_action(self, atcion):
        if self.devic_info.get('record_enable') == True:
            self.dns_proxy_socket.sendto(atcion.encode('utf8'), ('localhost', 10053))

    def start_app(self):
        print("start app: id {}, name {}".format(self.app_info['app_id'],self.app_info['app_name']))
        self.change_action("app_{}_action_-1_{}_{}_{}_{}_{}".format(self.app_info['app_id'], str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName'],self.desired_caps['udid']))#open app id is 0
        self.session = self.driver.session(self.desired_caps['bundleId'])
        time.sleep(30)
        self.change_action("None")

    def close_app(self):
        self.change_action("app_{}_action_-2_{}_{}_{}_{}_{}".format(self.app_info['app_id'], str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName'],self.desired_caps['udid']))#close app id is -2
        self.session.close()
        time.sleep(30)
        self.change_action("None")

    def go_action(self, action):
        if action['function'].__name__ != "weichat_xiaochengxu":
            self.change_action("app_{}_action_{}_{}_{}_{}_{}_{}".format(self.app_info['app_id'], str(action['id']), str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName'],self.desired_caps['udid']))  # open app id is -1
            action['function'](self.driver)
            time.sleep(action['delay'])
            self.change_action("None")
        elif action['function'].__name__ == "weichat_xiaochengxu":
            action['function'](self.driver, self, action)
            time.sleep(action['delay'])
            self.change_action("None")

    def run(self):
        self.start_app()
        for action in self.actions:
            self.go_action(action)
        self.close_app()


class AndriodApp:

    def __init__(self, app_info, devic_info):
        self.delay_time = 3
        self.app_info = app_info
        self.devic_info = devic_info
        self.desired_caps = app_info['desired_capabilities']
        self.desired_caps['deviceName'] = devic_info['deviceName']
        if 'mode' in devic_info and devic_info.get('mode') == 'wifi':
            self.desired_caps['udid'] = devic_info['wifiudid']
        else:
            self.desired_caps['udid'] = devic_info['udid']
        self.actions = app_info['actions']
        self.appium_server_url = "http://localhost:{}/wd/hub".format(devic_info['server_port'])
        self.driver = None
        self.dns_proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dns_proxy_socket.settimeout(100000)
        if 'restart_wifi' in devic_info and devic_info.get('restart_wifi') == 'true' or devic_info.get('restart_wifi') == 'True' or devic_info.get('restart_wifi') == True:
            self.restart_wifi()

    def setup(self):
        pass

    def restart_wifi(self):
        os.system('adb -s {} shell "svc wifi disable"'.format(self.desired_caps['udid']))
        time.sleep(3)
        os.system('adb -s {} shell "svc wifi enable"'.format(self.desired_caps['udid']))
        time.sleep(3)

    def cleanup(self):
        pass

    def change_action(self, atcion):
        if self.devic_info.get('record_enable') == True:
            self.dns_proxy_socket.sendto(atcion.encode('utf8'), ('localhost', 10053))

    def start_app(self):
        print("start app: id {}, name {}".format(self.app_info['app_id'],self.app_info['app_name']))
        self.change_action("app_{}_action_-1_{}_{}_{}_{}_{}".format(self.app_info['app_id'], str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName'],self.desired_caps['udid']))#open app id is 0
        self.driver = webdriver.Remote(self.appium_server_url, self.desired_caps)
        time.sleep(30)
        self.change_action("None")

    def close_app(self):
        self.change_action("app_{}_action_-2_{}_{}_{}_{}_{}".format(self.app_info['app_id'], str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName'],self.desired_caps['udid']))#close app id is -2
        webdriver.quit()
        time.sleep(30)
        self.change_action("None")

    def go_action(self, action):
        if action['function'].__name__ != "weichat_xiaochengxu":
            self.change_action("app_{}_action_{}_{}_{}_{}_{}_{}".format(self.app_info['app_id'], str(action['id']), str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName'],self.desired_caps['udid']))  # open app id is -1
            action['function'](self.driver)
            time.sleep(action['delay'])
            self.change_action("None")
        elif action['function'].__name__ == "weichat_xiaochengxu":
            action['function'](self.driver, self, action)
            time.sleep(action['delay'])
            self.change_action("None")

    def run(self):
        self.start_app()
        for action in self.actions:
            self.go_action(action)
        self.close_app()

    def close_app(self):
        self.driver.quit()


class AppWraper:
    def __init__(self, app_info, devic_info):
        if app_info['desired_capabilities']["platformName"].lower() == "ios":
            self.app = IOSApp(app_info, devic_info)
        elif app_info['desired_capabilities']["platformName"].lower() == "android":
            self.app = AndriodApp(app_info, devic_info)

    def run(self):
        self.app.run()

print(weichat_xiaochengxu.__name__)
