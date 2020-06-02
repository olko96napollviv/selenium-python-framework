
import time
import utilities.custom_logger as cl
import logging
from pages.home.navigation_page import Navigation_page
from base.basepage import BasePage

class Login_page(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = Navigation_page(driver)

    #Locators
    _login_link = "Login"
    _email_field  = "user_email"
    _password_field = "user_password"
    _login_button = "commit"


    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")

    def EnterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def EnterPassword(self, password):
        self.sendKeys(password, self._password_field)
        time.sleep(2)
    def clickLoginbutton(self):
        self.elementClick(self._login_button,locatorType="name")

    def login(self, email="", password=""):

        self.clickLoginLink()
        self.EnterEmail(email)
        self.EnterPassword(password)
        self.clickLoginbutton()
        time.sleep(2)
    def verifyLoginSuccess(self):
        result = self.isElementPresent("//*[@id='navbar']//a[@href='/current_user/profile']",
                                       locatorType="xpath")
        return result
    def verifyLoginFail(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        self.elementClick(locator="//a[@href='/sign_out']", locatorType="xpath")



