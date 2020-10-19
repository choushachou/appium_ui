#coding=utf-8
import time
import xlrd
from xlutils.copy import copy
import os
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        path=os.path.abspath(os.path.join(os.getcwd(),".."))+"\config\keyword.xls"
        if excel_path == None:
            #self.excel_path = r"G:\pythonselenium3lianxi\shuju2\config\keyword.xls"
            self.excel_path = path
        else:
            self.excel_path = excel_path
        if index ==None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]


    #获取excel数据，按照每行一个list，添加到一个人的list里面
    def get_data(self):
        result=[]
        rows = self.get_lines()
        if rows != None:
            for i in range(1,rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None
    #获取行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >=1:
            return rows
        return None


    #获取单元格的数据
    def get_col_value(self,row,col):
        if self.get_lines() > row:
            data = self.table.cell(row,col).value
            return data
        return None
    #写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)
        time.sleep(1)
if __name__ == '__main__':
    a=ExcelUtil().get_col_value(7,7)
    print(a)
