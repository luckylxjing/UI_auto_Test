# -*- coding: utf-8 -*-
"""
Created on 2024/7/2 18:24
@author: lixj
获取/关闭浏览器驱动的类
"""
import logging

from selenium import webdriver


class DriverUtils:
    __driver =  None #不能被外部调用
    __switch = False  #开关 默认是关着的
    # @classmethod 的作用是可以通过 类名.方法名  来调用这个方法
    #获取浏览器驱动
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            logging.info("create chrome driver!")
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()  # 窗口最大化
            cls.__driver.implicitly_wait(10)  # 隐式等待10秒
        else:
            logging.info("use existed chrome driver!")
        return cls.__driver



    #关闭浏览器驱动
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__switch is False:
            logging.info("quit chrome driver")
            cls.__driver.quit()
            cls.driver =  None
        else:
            logging.info("chrome driver is still alive")


    @classmethod
    def set_switch(cls,switch):
        cls.__switch = switch
