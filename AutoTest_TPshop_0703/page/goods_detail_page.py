# -*- coding: utf-8 -*-
"""
Created on 2024/7/4 8:12
@author: lixj 
需求: 商品详情页
"""

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):
    #加入购物车按钮
    add_to_cart_btn =By.ID, "join_cart"
    #iframe
    cart_iframe = By.CSS_SELECTOR,"[id*='layui-layer-iframe']"
    #添加成功
    result = By.CSS_SELECTOR,".conect-title span"


    #点击加入购物车
    def click_add_to_cart_btn(self):
        return self.click(self.add_to_cart_btn)
    #获取弹出窗结果
    def get_result(self):
        #切换到iframe中，再获取结果
        self.switch_to(self.cart_iframe)
        return self.find_el(self.result).text
