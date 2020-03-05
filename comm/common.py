from config.config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Common(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        ele = ''
        if '//' in element:
            try:
                ele = self.driver.find_element_by_xpath(element)
                logging.info("查找的元素存在 %s", element)
            except Exception as e:
                logging.error("uiautomator查找的元素不存在 %s %s", element, e)
        else:
            if ':id/' in element:
                # noinspection PyBroadException
                try:
                    ele = self.driver.find_element_by_id(element)
                except Exception as e:
                    logging.error("id查找的元素不存在 %s %s", element, e)
            elif 'android.widget' in element:
                # noinspection PyBroadException
                try:
                    ele = self.driver.find_element_by_class_name(element)
                except Exception as e:
                    logging.error("class_name查找的元素不存在 %s %s", element, e)
        return ele

    def find_elements(self, element):
        eles = ''
        if '//' in element:
            try:
                eles = self.driver.find_elements_by_xpath(element)
                logging.info("查找的元素存在 %s", element)
            except Exception as e:
                logging.error("uiautomator查找的元素不存在 %s %s", element, e)
        else:
            if 'android.widget' in element:
                try:
                    eles = self.driver.find_elements_by_class_name(element)
                except Exception as e:
                    logging.error("查找的元素不存在 %s %s", element, e)
            elif ':id/' in element:
                try:
                    eles = self.driver.find_elements_by_id(element)
                except Exception as e:
                    logging.error("查找的元素不存在 %s %s", element, e)
            elif '@text' in element:
                return self.driver.find_elements_by_xpath(element)

        return eles

    def click(self, element):
        cl = self.find_element(element)
        cl.click()

    def send_keys(self, element, keys):
        sk = self.find_element(element)
        sk.send_keys(keys)

    def wait_until_visible_app(self, element):
        if '//' in element:
            try:
                WebDriverWait(self.driver, 10, 5).until(lambda driver: driver.find_elements_by_xpath(element))
                logging.info("Wait until element with %s visible" % element)
            except Exception as e:
                logging.error("Failed to wait with %s" % e)
        else:
            if 'android.widget' in element:
                try:
                    WebDriverWait(self.driver, 10, 5).until(lambda driver: driver.find_elements_by_class_name(element))
                    logging.info("Wait until element with %s visible" % element)
                except Exception as e:
                    logging.error("Failed to wait with %s" % e)
            elif ':id/' in element:
                try:
                    WebDriverWait(self.driver, 10, 5).until(lambda driver: driver.find_element_by_id(element))
                    logging.info("Wait until element with %s visible" % element)
                except Exception as e:
                    logging.error("Failed to wait with %s" % e)

    def wait_until_visible_h5(self, element):
        if '=>' not in element:
            element = element
        else:
            element = element.split('=>')[1]
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, element)))
            logging.info("Wait until element with %s visible" % element)
        except NameError as e:
            logging.error("Failed to wait with %s" % e)

