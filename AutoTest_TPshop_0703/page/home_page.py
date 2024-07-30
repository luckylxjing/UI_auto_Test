# -*- coding: utf-8 -*-
"""
Created on 2024/7/4 8:12
@author: lixj 
需求：登录成功后，我的商城-页面
"""
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):
    #待付款页面
    to_be_pay_link =By.XPATH,"//*[text()='待付款']"
    #立即支付按钮
    pay_btn =By.CSS_SELECTOR,".ps_lj"

    #点击待付款链接
    def click_to_be_pay_link(self):
        return self.click(self.to_be_pay_link)
    #点击立即支付按钮
    def click_pay_btn(self):
        return self.click(self.pay_btn)