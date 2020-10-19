#coding=utf-8

from appium import webdriver


def appium_desired():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'oppo reno 4'

    #下面两行为在输入框中输入中文生效
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'

    desired_caps['appPackage'] = 'com.business.eglobal'
    desired_caps['appActivity'] = 'com.business.eglobal.ui.activity.other.SplashActivity'
    desired_caps['noReset'] = 'True'
    desired_caps["autoGrantPermissions"]='True'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver

if __name__ == '__main__':
    appium_desired()
