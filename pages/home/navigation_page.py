from selenium.webdriver.common.by import By
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class Navigation_page(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _my_courses = "All Courses"
    _all_courses = "My Courses"
    _pracrice = "Practice"
    _user_icon = "//a[@data-toggle='dropdown']"


    def navigateToALlCourses(self):
        self.elementClick(locator=self._all_courses,locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses,locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._pracrice,locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_icon,locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)

