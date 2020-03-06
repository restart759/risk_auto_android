from comm.common import Common
from pageElement.apply_customer_info import ApplyCustomerInfo


class ApplyInfo(Common):
    def customer_info_go(self):
        customer_info_go = '//android.widget.TextView[@text="借款人信息"]/../android.widget.TextView[@text="开始填写"]'

        self.click(customer_info_go)
        return ApplyCustomerInfo(self.driver)

    def loan_info_go(self):
        loan_info_go = '//android.widget.TextView[@text="借款基本信息"]/../android.widget.TextView[@text="开始填写"]'

        self.click(loan_info_go)
        return ApplyInfo(self.driver)

    def house_info_go(self):
        house_info_go = '//android.widget.TextView[@text="房产信息"]/../android.widget.TextView[@text="开始填写"]'

        self.click(house_info_go)
        return ApplyInfo(self.driver)

    def contact_info_go(self):
        contact_info_go = '//android.widget.TextView[@text="共签人信息"]/../android.widget.TextView[@text="开始填写"]'

        self.click(contact_info_go)
        return ApplyInfo(self.driver)

    def buyer_info_go(self):
        buyer_info_go = '//android.widget.TextView[@text="买房人信息"]/../android.widget.TextView[@text="开始填写"]'

        self.click(buyer_info_go)
        return ApplyInfo(self.driver)

    def image_info_go(self):
        image_info_go = '//android.widget.TextView[@text="影像信息"]/../android.widget.TextView[@text="开始填写"]'

        self.click(image_info_go)
        return ApplyInfo(self.driver)

    def loan_info(self):

    def contact_info(self):

    def buyer_info(self):

    def gq_house_info(self):

    def gq_image_info(self):

    def fd_house_info(self):

    def fd_image_info(self):
