from selenium import webdriver
from pages.home.Login_page import Login_page
import unittest
import pytest
from utilities.teststatus import StatusTTest



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = Login_page(self.driver)
        self.ts = StatusTTest(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login(password="uvudavybu")

        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_valid_login", result2, "Login was not successful")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("olko96napol@gmail.com", "uvudavyb")
        result = self.lp.verifyLoginFail()
        assert result == True



