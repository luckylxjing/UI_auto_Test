# -*- coding: utf-8 -*-
"""
Created on 2024/7/4 8:13
@author: lixj 
需求: 下订单页面
"""
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class OrderPage(BaseAction):
    # 提交订单按钮
    submit_btn = By.CLASS_NAME,"Sub-orders"

    #点击提交订单按钮
    def click_submit_btn(self):
        return self.click(self.submit_btn)
