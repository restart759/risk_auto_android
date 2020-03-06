from comm.common import Common
from pageElement.choose_loan_type import ChooseLoanType


class NewApply(Common):
    def search(self, name='', id_no=''):
        customer_name = '//android.widget.EditText[@text="请输入借款人姓名"]'
        customer_id = '//android.widget.EditText[@text="请输入借款人身份证"]'
        search_button = '//android.widget.TextView[@text="查询"]'

        if len(name) > 0:
            self.send_keys(customer_name, name)
        elif len(id_no) > 0:
            self.send_keys(customer_id, id_no)
        self.click(search_button)

    def new_apply(self):
        new_button = '//android.widget.TextView[@text="新建"]'

        self.click(new_button)
        return ChooseLoanType(self.driver)
