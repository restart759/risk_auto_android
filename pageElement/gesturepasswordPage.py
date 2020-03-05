from comm.common import *
from appium.webdriver.common.touch_action import TouchAction
import time
from pageElement.main_page import MainPage


class GesturePasswordPage(Common):
    gesture_pwd = '//android.view.View[@index="10"]/android.view.View'
    press_gesture = '//android.widget.TextView[contains(text,"手势密码")]'

    def gesture_set(self):
        set_gesture = '手势密码'
        login_gesture = '欢迎'
        main_page = '主页'
        sources = self.driver.page_source
        # list_pwd = self.find_elements(self.gesture_pwd)
        # TouchAction(self.driver).press(list_pwd[0]).move_to(list_pwd[0]).move_to(list_pwd[1]).wait(100).move_to(
        #     list_pwd[2]).wait(100).move_to(list_pwd[4]).release().perform()
        # time.sleep(1)
        if set_gesture in sources:
            logging.info('Set gesture password!')
            while len(self.find_elements(self.gesture_pwd)) > 0:
                list_pwd = self.find_elements(self.gesture_pwd)
                try:
                    TouchAction(self.driver).press(list_pwd[0]).move_to(list_pwd[0]).wait(100).move_to(list_pwd[3]).\
                        wait(100).move_to(list_pwd[6]).wait(100).move_to(list_pwd[7]).release().perform()
                    time.sleep(1)
                except IndexError:
                    logging.info('failed to set gesture password!')
        elif login_gesture in sources:
            logging.info('Set login gesture password!')
            while len(self.find_elements(self.gesture_pwd)) > 0:
                list_pwd = self.find_elements(self.gesture_pwd)
                TouchAction(self.driver).press(list_pwd[0]).move_to(list_pwd[0]).move_to(list_pwd[1]).wait(100).move_to(
                    list_pwd[2]).wait(100).move_to(list_pwd[4]).release().perform()
                time.sleep(1)
        elif main_page in sources:
            logging.info('no need login gesture!')

        return MainPage(self.driver)
