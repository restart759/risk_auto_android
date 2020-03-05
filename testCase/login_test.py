import time
from comm.appDriver import AppDriver
from pageElement.loginpage import Login
import unittest


class LoginPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = AppDriver().app_driver()

    def test_login(self):
        user = 'admin'
        pwd = '111111'
        Login(self.driver).login(user, pwd).gesture_set()


if __name__ == '__main__':
    unittest.main()
