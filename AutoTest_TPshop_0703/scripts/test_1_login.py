# -*- coding: utf-8 -*-
"""
Created on 2024/7/4 9:42
@author: lixj 
需求:  测试页面-登录页
"""
import logging
import time

import pytest

from base.base_analyze import analyze_data
from page.index_page import IndexPage
from page.login_page import LoginPage
from utils.driver_utils import DriverUtils


class TestLogin:

    def setup(self):

        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.driver.get("http://192.168.10.139/")

    def teardown(self):
        time.sleep(3)
        DriverUtils.quit_driver()


    @pytest.mark.parametrize("params",analyze_data("login_data.json"))
    def test_login(self,params):
        self.index_page.click_login_link()
        #logging.info("login in {} {} {}".format((params["username"], params["password"], params["verify_code"])))
        self.login_page.input_username(params["username"])
        self.login_page.input_password(params["password"])
        self.login_page.input_verify_code(params["verify_code"])
        self.login_page.click_login_btn()
        #登录成功需要时间，暂停几秒等页面跳转
        logging.info("wait 5s for page display")
        time.sleep(5)
        print(params["msg"])
        assert params["msg"] in self.driver.title

































