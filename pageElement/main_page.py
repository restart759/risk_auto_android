from comm.common import *


class MainPage(Common):
    def close_gesture(self):
        setting_button = '//android.widget.TextView[contains(text,"您好")]/../android.view.View//android.widget.ImageView'
        self.click(setting_button)
