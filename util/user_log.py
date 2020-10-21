#coding:utf-8
import logging
import os
import datetime
import traceback
class UserLog():
    def __init__(self):

        #DEBUG < INFO < WARNING < ERROR < CRITICAL
        #except Exception as e:

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        #os.path.abspath(__file__) #获得当前文件路径
        # 获得上上级路径
        base_dir = os.path.abspath(os.path.join(os.getcwd(),"..")) + "\\config\\"+"logs\\"
        #log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log" #年月日格式输出
        log_name = base_dir+"\\" +log_file
        #print(log_name)
        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')#log输出的位置及路径及名称
        #self.file_handle.setLevel(logging.INFO) #等级为info
        self.file_handle.setLevel(logging.INFO)  # 等级为DEBUG
        #文件中按一定格式输出
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s --->%(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        # 控制台输出日志
        self.consle = logging.StreamHandler()
        self.consle.setFormatter(formatter)
        self.logger.addHandler(self.consle)
        #except Exception as e:
        #self.logger.debug(traceback.format_exc())



    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)  # 将log流关闭
        # logging.debug(8999999)
        self.file_handle.close()


if __name__ == '__main__':
    user = UserLog()
    log=user.get_log()
    log.debug(111)
    log.info(2225645645)
    #log.error(da)
    try:
        log.error(da)
    except Exception as e:
        log.info(traceback.format_exc())
    user.close_handle()
