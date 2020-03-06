from comm.common import Common


class CustomerAuthorize(Common):
    def customer_authorize(self, name, id_no, mobile):
        customer_name = '//android.widget.EditText[@text="请输入借款人姓名"]'
        customer_id = '//android.widget.EditText[@text="请输入借款人身份证"]'
        customer_mobile = '//android.widget.EditText[@text="请输入借款人手机号"]'
        submit_button = '//android.widget.TextView[@text="提交"]'

        self.send_keys(customer_name, name)
        self.send_keys(customer_id, id_no)
        self.send_keys(customer_mobile, mobile)
        self.click(submit_button)

