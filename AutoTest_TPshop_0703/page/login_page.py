# -*- coding: utf-8 -*-
"""
Created on 2024/7/4 8:13
@author: lixj 
需求:登录页
"""
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 用户名  输入框
    username_input = By.ID, "username"
    # 密码 输入框
    password_input = By.ID, "password"
    # 验证码 输入框
    verify_code_input = By.ID, "verify_code"
    # 登录 按钮
    login_btn = By.NAME, "sbtbutton"
    # 输入用户名
    def input_username(self, content):
        return self.input(self.username_input, content)
    # 输入密码
    def input_password(self, content):
        return self.input(self.password_input, content)
    # 输入验证码
    def input_verify_code(self, content):
        return self.input(self.verify_code_input, content)
    # 点击登录按钮
    def click_login_btn(self):
        return self.click(self.login_btn)


