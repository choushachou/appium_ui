#coding=utf-8

from util.excel_util import ExcelUtil
class FindElement():
    def __init__(self,driver,row,col):

        self.row = row
        self.col = col
        self.driver = driver
        self.excel = ExcelUtil()
    def get_key(self,col):

        re=[]
        case_lines = self.excel.get_lines()
        if case_lines:
            for row in range(1, case_lines):

                handle = self.excel.get_col_value(row, self.col)
                re.append(handle)
        return re
    def get_method_value(self,row,col):
        self.row =row
        self.col = col
        row=int(self.row)
        handle= self.get_key(self.col)[row-1]
        by = handle.split(">")[0]
        value = handle.split('>')[1]
        try:
            if by =='id':
                return self.driver.find_element_by_id(value)
            elif by =='android_uiautomator':
                return self.driver.find_element_by_android_uiautomator(value)
            elif by =="xpath":
                return self.driver.find_element_by_xpath(value)
            elif by =='accessibility_id':
                return self.driver.find_element_by_accessibility_id(value)
        except:
            return None