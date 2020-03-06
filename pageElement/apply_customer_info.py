from comm.common import Common
from pageElement.apply_info import ApplyInfo
from pageElement.apply_customer_id_image import UploadIdImage


class ApplyCustomerInfo(Common):
    def customer_info(self, name='', id_no=''):
        customer_name = '//android.widget.EditText[@text="请输入借款人姓名"]'
        customer_id = '//android.widget.EditText[@text="请输入借款人身份证"]'

        upload_id_image = '请上传借款人身份证正反面'
        apply_info_page = '填写申请件'
        sources = self.driver.page_source
        if len(name) > 0 and len(id_no) > 0:
            self.send_keys(customer_name, name)
            self.send_keys(customer_id, id_no)
            self.next()
            if upload_id_image in sources:
                return UploadIdImage(self.driver)
            elif apply_info_page in sources:
                return ApplyInfo(self.driver)
