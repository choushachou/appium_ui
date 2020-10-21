#coding = utf - 8
from lianxi.qidong import appium_desired
from util.find_elem import FindElement
import time
import os
class ActionMethod():
    def __init__(self):
        self.driver=appium_desired()


    def open_appium(self):
        #appium_desired()
        self.__init__()


    #定位元素
    def get_element(self,row,col):
        find_e = FindElement(self.driver,row,col)
        element = find_e.get_method_value(row,col)
        return element

    #输入元素
    def element_send_keys(self,row,col,value):
        ele = self.get_element(row,col)
        ele.send_keys(value)

    #点击元素
    def click_element(self,row,col):
        self.get_element(row,col).click()

    #dengdai
    def sleep_time(self,value=None):
        if value== None:
            values = 1
        else:
            values = int(value)
        time.sleep(values)
    #关闭appium
    def close_appium(self):
        self.driver.close_app()

    #截图
    def screen_picture(self,row):
        file_path = os.path.abspath(os.path.join(os.getcwd(),"..")) + "\\config\\" + "picture\\"+'第'+str(row)+'行' + ".png"
        self.driver.save_screenshot(file_path)
