from comm.common import *
from appium.webdriver.common.touch_action import TouchAction
import time


class GesturePasswordPage(Common):
    gesture_pwd = '//android.view.View[@index="10"]/android.view.View'
    press_gesture = '//android.widget.TextView[@text="请输入手势密码"]'

    def first_set(self):
        set_gesture = '请输入手势密码'
        sources = self.driver.page_source
        list_pwd = self.find_elements(self.gesture_pwd)
        TouchAction(self.driver).press(list_pwd[0]).move_to(list_pwd[0]).move_to(list_pwd[1]).wait(100).move_to(
            list_pwd[2]).wait(100).move_to(list_pwd[4]).release().perform()
        time.sleep(1)
        if set_gesture in sources:
            while len(self.find_elements(self.press_gesture)) > 0:
                list_pwd = self.find_elements(self.gesture_pwd)
                TouchAction(self.driver).press(list_pwd[0]).move_to(list_pwd[0]).move_to(list_pwd[1]).wait(100).move_to(
                    list_pwd[2]).wait(100).move_to(list_pwd[4]).release().perform()
                time.sleep(1)
