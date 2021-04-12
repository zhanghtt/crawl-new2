#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome(executable_path='D:\chromedriver\chromedriver.exe')


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在10秒内完成扫码")
    time.sleep(10)
    # 这里写你需要抢购商品的链接地址
    driver.get(
        "https://detail.tmall.com/item.htm?id=617607737003&ut_sk=1.XMl41x6wReEDAIRpLR4%20IIoV_21380790_1589203479975.Copy.1&sourceType=item&price=0.1&suid=9AD81F3B-3DAF-4E1F-AA08-D92F62C692B6&un=94620f5f027c8264af3e4a851c15f467&share_crt_v=1&spm=a2159r.13376460.0.0&sp_tk=4oKkWFNnTjFMaDdPekvigqQ=&cpp=1&shareurl=true&short_name=h.V9t8CDT&sm=84d143&app=chrome")
    time.sleep(1)


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > buytime:
            if driver.find_element_by_link_text("立即购买"):
                driver.find_element_by_link_text("立即购买").click()
                break
        time.sleep(0.0001)
    while True:
        try:
            if driver.find_element_by_link_text("提交订单"):
                driver.find_element_by_link_text("提交订单").click()
        except:
            time.sleep(1)
        print(now)
        time.sleep(0.0001)


if __name__ == "__main__":
    login()
    # buy("2020-05-12 10:00:00.000000")
    buy("2020-05-12 15:00:00.000000")