from appium import webdriver
from config.config import *

countA = 1


class AppDriver(object):

    def app_driver(self):
        global driver, countA
        # appium启动服务只运行一次
        if countA == 1:
            # 启动appium服务
            os.system('start startAppiumServer.bat')
        countA = countA + 1
        # 所有的test运行前运行一次
        desired_caps = {}
        desired_caps['platformName'] = platformName
        # desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['unicodeKeyboard'] = 'True'  # 使用unicode方式发送字符
        desired_caps['resetKeyboard'] = 'True'  # 隐藏键盘
        desired_caps['noReset'] = 'True'  # 如果app存在,不再重新安装
        desired_caps['app'] = app
        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            logging.info('driver加载成功 %s', self.driver)
        except Exception as e:
            logging.info('driver加载失败 %s', e)
        return self.driver

    # @classmethod
    # def tearDownClass(cls):
    #     # 关闭浏览器驱动
    #     cls.driver.quit()
    #     # cls.driver.close()
    #     # 获取测试用例个数,如果执行完，就stop appium
    #     caseCount = runSet.set_suite().countTestCases()
    #     if countA == caseCount + 1:
    #         cls.driver.removeApp("io.appium.android.ime");
    #         # 关闭appium服务
    #         os.system('start stopAppiumServer.bat')


# if __name__ == "__main__":
#     AppDriver().setUpClass()
