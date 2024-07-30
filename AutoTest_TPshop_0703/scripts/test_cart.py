# -*- coding: utf-8 -*-
"""
Created on 2024/7/4 10:05
@author: lixj 
需求:  购物车--测试页面
"""
import logging
import time
import pytest
from base.base_analyze import analyze_data
from page.goods_detail_page import GoodsDetailPage
from page.goods_search_page import GoodsSearchPage
from page.index_page import IndexPage
from page.login_page import LoginPage
from utils.driver_utils import DriverUtils


class TestCart:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.index_page = IndexPage(self.driver)
        self.goods_search_page = GoodsSearchPage(self.driver)
        self.goods_detail_page = GoodsDetailPage(self.driver)
        self.driver.get("http://192.168.10.139/")

    def teardown(self):
        time.sleep(3)
        DriverUtils.quit_driver()



    def test_cart(self):
        self.index_page.input_keywords("小米手机5")
        self.index_page.click_search_btn()
        logging.info("search with 小米手机5")
        self.goods_search_page.click_add_to_cart_btn()
        self.goods_detail_page.click_add_to_cart_btn()
        time.sleep(5)
        logging.info("with 5s for page display")
        assert "添加成功"  ==  self.goods_detail_page.get_result()


































