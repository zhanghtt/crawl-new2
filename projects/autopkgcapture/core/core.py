#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, unittest
from appium import webdriver
import socket
import uuid


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


class App:
    def __init__(self, app_info, appium_server_url="http://localhost:4723/wd/hub"):
        self.delay_time = 3
        self.app_info = app_info
        self.desired_caps = app_info['desired_capabilities']
        self.actions = app_info['actions']
        self.appium_server_url = appium_server_url
        self.driver = None
        self.dns_proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dns_proxy_socket.settimeout(100000)

    def setup(self):
        pass

    def cleanup(self):
        pass

    def change_action(self, atcion):
        #self.dns_proxy_socket.sendto(atcion.encode('ascii'), ('localhost',10053))
        self.dns_proxy_socket.sendto(atcion.encode('utf8'), ('localhost', 10053))

    def start_app(self):
        print("start app: id {}, name {}".format(self.app_info['app_id'],self.app_info['app_name']))
        self.change_action("app_{}_action_-1_{}_{}_{}_{}".format(self.app_info['app_id'], str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName']))#open app id is 0
        self.driver = webdriver.Remote(self.appium_server_url, self.desired_caps)
        time.sleep(30)
        self.change_action("None")

    def close_app(self):
        self.change_action("app_{}_action_-2_{}_{}_{}_{}".format(self.app_info['app_id'], str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName']))#close app id is -2
        webdriver.quit()
        time.sleep(30)
        self.change_action("None")

    def go_action(self, action):
        if action['function'].__name__ != "weichat_xiaochengxu":
            self.change_action("app_{}_action_{}_{}_{}_{}_{}".format(self.app_info['app_id'], str(action['id']), str(uuid.uuid1()),self.app_info['app_name'],self.app_info['platform'],self.desired_caps['deviceName']))  # open app id is -1
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


print(weichat_xiaochengxu.__name__)
