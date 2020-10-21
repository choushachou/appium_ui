# coding=utf-8
from util.excel_util import ExcelUtil
from keywordappium.actionMethod import ActionMethod
import sys, os
import traceback
from util.user_log import UserLog
path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(path)
log = UserLog()
logging=log.get_log()
class KeywordCase:
    def run_main(self):
        global a
        self.action_method = ActionMethod()
        a =self.action_method
        handle_excel = ExcelUtil()
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(2, case_lines):

                is_run = handle_excel.get_col_value(i, 4)
                if is_run == "yes":
                    try:
                        logging.info(i)
                        method = handle_excel.get_col_value(i, 5)
                        send_value = handle_excel.get_col_value(i, 6)
                        self.run_method(method, i,7,send_value)
                        except_result_method = handle_excel.get_col_value(i, 8)
                        except_resutl = handle_excel.get_col_value(i, 9)
                        if except_resutl != None:
                            except_value = self.get_result_value(except_resutl)

                            result = self.run_method(except_result_method,i,9, except_value)
                            if result:
                                handle_excel.write_value(i, 10,'pass')
                            else:
                                handle_excel.write_value(i, 10,'fail')
                                a.screen_picture(i)
                        else:
                            pass
                    except Exception as e:
                        log.get_log().error(traceback.format_exc())
                        log.close_handle()

    # 获取预期结果值
    def get_result_value(self, data=None):
        if data == None:
            return None
        else:

            return data.split('>')[1]


    # 运行操作
    def run_method(self,method,row,col,send_value=None):
        global result
        action = self.action_method
        if method == 'click_element':
            result = action.click_element(row,col)
        elif method =='sleep_time':
            result = action.sleep_time(send_value)
        elif method == 'element_send_keys':
            result = action.element_send_keys(row,col,send_value)
        elif method == 'open_appium':
            result = action.open_appium()
        elif method == 'get_element':
            result = action.get_element(row,col)
        else:
            result =action.close_appium()
        return result


if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
