from comm.common import *
from pageElement.customer_authorize import CustomerAuthorize


class MainPage(Common):
    def close_gesture(self):
        setting_button = '//android.widget.TextView[contains(text,"您好")]/../android.view.View//android.widget.ImageView'
        self.click(setting_button)
        self.back()
        return MainPage(self.driver)

    def authorize(self):
        authorize = '//android.widget.TextView[@text="借款人授权"]'
        self.click(authorize)
        return CustomerAuthorize(self.driver)

    def register(self):
        register = '//android.widget.TextView[@text="借款人注册"]'
        self.click(register)

    def apply(self):
        apply = '//android.widget.TextView[@text="借款申请"]'
        self.click(apply)

    def outing(self):
        outing = '//android.widget.TextView[@text="申请件外访"]'
        self.click(outing)

    def apply_offline_assign(self):
        offline_assign = '//android.widget.TextView[@text="申请件线下签约"]'
        self.click(offline_assign)

    def coop_company_assign(self):
        coop_company_assign = '//android.widget.TextView[@text="合作商签约"]'
        self.click(coop_company_assign)

