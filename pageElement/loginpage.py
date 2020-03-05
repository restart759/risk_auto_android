from comm.common import *
from pageElement.gesturepasswordPage import GesturePasswordPage
from appium.webdriver.common.touch_action import TouchAction


class Login(Common):
    username = '//android.widget.EditText[@text="请输入登录名"]'
    password = '//android.widget.TextView[@text="密码"]/../android.view.View[@index="4"]/android.widget.EditText'
    login_button = '//android.widget.TextView[@text="登录"]'
    gesture_pwd = '//android.view.View[@index="10"]/android.view.View'

    def login(self, user, pwd):
        time.sleep(5)
        login_p = '账号密码登录'
        press_gesture = '欢迎'
        sources = self.driver.page_source
        if login_p in sources:
            self.send_keys(self.username, user)
            self.send_keys(self.password, pwd)
            self.click(self.login_button)
            time.sleep(1)
            return GesturePasswordPage(self.driver)
        elif press_gesture in sources:
            list_pwd = self.find_elements(self.gesture_pwd)
            TouchAction(self.driver).press(list_pwd[0]).move_to(list_pwd[0]).move_to(list_pwd[1]).wait(100).move_to(
                list_pwd[2]).wait(100).move_to(list_pwd[4]).release().perform()
            time.sleep(1)

