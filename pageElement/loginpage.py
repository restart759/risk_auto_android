from comm.common import *
from pageElement.gesturepasswordPage import GesturePasswordPage


class Login(Common):
    username = '//android.widget.EditText[@text="请输入登录名"]'
    password = '//android.widget.TextView[@text="密码"]/../android.view.View[@index="4"]/android.widget.EditText'
    login_button = '//android.widget.TextView[@text="登录"]'
    gesture_pwd = '//android.view.View[@index="10"]/android.view.View'

    def login(self, user, pwd):
        time.sleep(5)
        if len(self.find_elements(self.username)) > 0:
            self.send_keys(self.username, user)
            self.send_keys(self.password, pwd)
            self.click(self.login_button)
            time.sleep(1)
        else:
            time.sleep(1.5)
        return GesturePasswordPage(self.driver)


