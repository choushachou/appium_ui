# coding=utf-8
from util.excel_util import ExcelUtil
from keywordappium.actionMethod import ActionMethod
import sys, os

path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(path)


class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil()
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):

                is_run = handle_excel.get_col_value(i, 3)
                if is_run == "yes":
                    print(i)
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    #handle_value = handle_excel.get_col_value(i, 6)

                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_resutl = handle_excel.get_col_value(i, 8)
                    self.run_method(method, i,6,send_value)
                    if except_resutl != '':
                        except_value = self.get_result_value(except_resutl)
                        result = self.run_method(except_result_method,i,8, except_value[1])
                        if result:
                            handle_excel.write_value(i, 'pass')
                        else:
                            handle_excel.write_value(i, 'fail')
                    else:
                        pass

    # 获取预期结果值
    def get_result_value(self, data):
        return data.split('>')

    # 运行操作
    def run_method(self,method,row,col,send_value=''):
        global result
        if method == 'click_element':
            result = self.action_method.click_element(row,col)
        elif method =='sleep_time':
            result = self.action_method.sleep_time(send_value)
        elif method == 'element_send_keys':
            result = self.action_method.element_send_keys(row,col,send_value)
        elif method == 'open_appium':
            result = self.action_method.open_appium()
        elif method == 'get_element':
            result = self.action_method.get_element(row,col)
        else:
            result =self.action_method.close_appium()
        return result



    # def run_method(self, method, row,send_value=''):
    #     method_value = getattr(self.action_method, method)
    #     if send_value == '':
    #         result = method_value(row)
    #     else:
    #         result = method_value(row,send_value)
    #
    #     return result


if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
