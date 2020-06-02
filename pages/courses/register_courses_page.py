import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class  RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ###############
    ##LOCATORS#####
    ###############

    _search_box = "search-courses"
    _search_course_icon = "search-course-button"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "//div[@class='course-listing-title']"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@class='InputElement is-empty Input Input--empty']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _zip_field = "postal"
    _terms_agree = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"
    _enroll_error_message = "//div[@class='payment-error-box only-on-mobile']"

    ############################
    #####ELEMENT INTERACTIONS###
    ############################

    def EnterCourseName(self, name):
        self.sendKeys(name,locator=self._search_box)
        self.elementClick(locator=self._search_course_icon)

    def SelectCourseToEnroll(self, CourseName):
        self.elementClick(locator=self._course.format(CourseName),locatorType="xpath")

    def ClickEnrollButton(self):
        self.elementClick(locator=self._enroll_button)


    def enterCreditNum(self, num):
        #self.switchToFrame(name="__privateStripeFrame9")
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCreditExp(self, exp):
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCreditCVV(self, cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        self.SwitchFrameByIndex(self._zip_field, locatorType="name")
        self.sendKeys(zip, locator=self._zip_field, locatorType="name")
        self.switchToDefaultContent()

    def clickAgree(self):
        self.elementClick(locator=self._terms_agree)

    def ClickEnrollSubmit(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")
        time.sleep(2)

    def EnterCreditInfor(self, num, exp, cvv, zip):
        self.enterCreditNum(num)
        self.enterCreditExp(exp)
        self.enterCreditCVV(cvv)
        self.enterZip(zip)

    def EnrollCourse(self, num="", exp="", cvv="", zip=""):
        self.ClickEnrollButton()
        self.webScroll(direction="down")
        self.EnterCreditInfor(num, exp, cvv, zip)
        self.clickAgree()
        self.ClickEnrollSubmit()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

    # def verifyEnrollFailed(self):
    #     result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
    #                             info="Enroll Button")
    #     return not result















