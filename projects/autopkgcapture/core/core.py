#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, unittest
from appium  import webdriver
import socket


class ActionStrategy:
    def __init__(self):
        pass


class App:
    def __init__(self, desired_caps, strategy_list=None, appium_server_url="http://localhost:4723/wd/hub"):
        self.delay_time=3
        self.desired_caps = desired_caps
        self.strategy_list = strategy_list
        self.appium_server_url = appium_server_url
        self.driver = None
        self.dns_proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dns_proxy_socket.settimeout(100000)

    def setup(self):
        pass

    def cleanup(self):
        pass

    def change_action(self, atcion):
        self.dns_proxy_socket.sendto(atcion.encode('ascii'), ('localhost',10053))

    def start_app(self):
        self.setup()
        self.change_action("start_app")
        self.driver = webdriver.Remote(self.appium_server_url, self.desired_caps)
        time.sleep(3)
        self.change_action("None")
        self.cleanup()

    def close_app(self):
        self.driver.quit()

    def run(self):
        pass


def test():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 设备系统
    desired_caps['platformVersion'] = '10.0'  # 设备系统版本
    desired_caps['deviceName'] = 'Q7PRX18B21019283'  # 设备名称
    # desired_caps['app'] = PATH(r"E:\tests\GuoYuB2B_2.1.apk")
    desired_caps['appPackage'] = 'com.taobao.taobao'
    desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
    # desired_caps['app']='C:\\Users\\admin\\Downloads\\com.taobao.taobao_V9.21.1.apk'
    desired_caps['noReset'] = 'True'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    app = App(desired_caps)
    app.start_app()

test()