#!/usr/bin/env python#
# -*- coding:utf-8 -*-

from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()

def auto_buy(username, password, purchase_list_time):
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "打开登陆界面")
    # driver.get("https://passport.jd.com/new/login.aspx")
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "开始填写账号密码")
    # driver.find_element_by_link_text("账户登录").click()
    # driver.find_element_by_name("loginname").send_keys(username)
    # driver.find_element_by_name("nloginpwd").send_keys(password)
    # driver.find_element_by_id("loginsubmit").click()
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "手动拼图验证")
    # time.sleep(10)  #此处睡眠时间用来手动拼图验证
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"登陆成功")
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "等待时间到达抢购时间：",purchase_list_time, "......")
    driver.get("https://open.weixin.qq.com/connect/qrconnect?appid=wx827225356b689e24&state=302695155070867FD0D631EEE91C7A3B2A9D4861059D2E263070DA831C58356F1744F565B8D886AB05394481DC11E75F&redirect_uri=https%3A%2F%2Fqq.jd.com%2Fnew%2Fwx%2Fcallback.action%3Fview%3Dnull%26uuid%3De1c397c3821c4b6eafe002d743f64431&response_type=code&scope=snsapi_login#wechat_redirect")
    while True:
        count = 0
        try:
            count += 1
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "开始第 %s 次抢购......"%count)
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "打开商品页面")
            driver.get("https://item.jd.com/100014530230.html")  # 打开商品页面
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "抢购")
            driver.find_element_by_link_text("抢购").click()  # 立即抢购
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "点击去结算")
            driver.find_element_by_link_text("去结算").click()  # 去结算
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "点击提交订单")
            # time.sleep(5)   #提交订单前必须等待几秒【感觉跟电脑性能快慢有关，不卡的电脑可以适当降低尝试】
            driver.find_element_by_id('order-submit').click()  # 提交订单
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "订单提交成功,请前往订单中心待付款付款")
        except Exception as e:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "抢购出现异常，重新抢购: ", e)
        time.sleep(0.001)

purchase_list_time = [
    "2020-12-02 17:24:00",
]
auto_buy('账号', '密码', purchase_list_time)