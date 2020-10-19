
from util.excel_util import ExcelUtil
class FindElement():
    def __init__(self):
        #self.driver = driver
        self.excel = ExcelUtil()
    def get_key(self):
        re=[]
        case_lines = self.excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                handle = self.excel.get_col_value(i, 6)
                re.append(handle)
        print(re)
if __name__ == '__main__':
    a=FindElement()
    a.get_key()