from comm.common import Common
from pageElement.apply_info import ApplyInfo


class ChooseLoanType(Common):
    def choose_loan_type(self, loan_type, sub_type):
        fd = '//android.widget.TextView[@text="房抵"]/../android.view.View[1]'
        gq = '//android.widget.TextView[@text="过桥"]/../android.view.View[1]'

        if loan_type == '房抵':
            self.click(fd)
        elif sub_type == '过桥':
            self.click(gq)
        return ApplyInfo(self.driver)
