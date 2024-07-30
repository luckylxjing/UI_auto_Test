# -*- coding: utf-8 -*-
"""
Created on 2024/7/3 11:10
@author: lixj 
需求:
"""
class BaseAction:

    def __init__(self,driver):
        self.driver = driver


    #查找元素的方法
    def find_el(self,feature):
        return self.driver.find_element(*feature)

    #查找多个元素的方法
    def find_els(self,feature):
        return self.driver.find_elements(*feature)

    #点击元素的方法
    def click(self,feature):
        return self.find_el(feature).click()
    #输入的方法
    def input(self,feature,content):
        return self.find_el(feature).send_keys(content)

    #清除元素的方法
    def clear(self,feature):
        return self.find_el(feature).clear()

    #切换iframe方法
    def switch_to(self,frame_feature):
        return self.driver.switch_to.frame(self.find_el(frame_feature))

    #切换回去
    def switch_to_default(self,frame_feature):
        return self.driver.switch_to.default_content()

    def switch_window(self):
        handlers = self.driver.window_handles
        return  self.driver.switch_to.window(handlers[-1])