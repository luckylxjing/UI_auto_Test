# -*- coding: utf-8 -*-
"""
Created on 2024/7/4 8:12
@author: lixj 
需求:商品搜索页
"""
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class GoodsSearchPage(BaseAction):
    #加入购物车按钮 （目的：为了跳转到商品详情）
    add_to_cart_btn = By.CSS_SELECTOR,".p-btn >a:nth-child(1)"

    #点击加入购物车按钮
    def click_add_to_cart_btn(self):
        return self.click(self.add_to_cart_btn)