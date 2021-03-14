#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, unittest
from appium  import webdriver
import socket


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
        self.dns_proxy_socket.sendto(atcion.encode('ascii'), ('localhost',10053))

    def start_app(self):
        self.change_action("app_{}_action_-1".format(self.app_info['app_id']))#open app id is 0
        self.driver = webdriver.Remote(self.appium_server_url, self.desired_caps)
        self.driver.find
        time.sleep(20)
        self.change_action("None")

    def close_app(self):
        self.change_action("app_{}_action_-2".format(self.app_info['app_id']))#close app id is -2
        webdriver.quit()
        time.sleep(20)
        self.change_action("None")

    def go_action(self, action):
        self.change_action("app_{}_action_{}".format(self.app_info['app_id'], str(action['id'])))  # open app id is -1
        print(action)
        action['function'](self.driver)
        time.sleep(action['delay'])
        self.change_action("None")

    def run(self):
        self.start_app()
        for action in self.actions:
            self.go_action(action)
        self.close_app()

    def close_app(self):
        self.driver.quit()

