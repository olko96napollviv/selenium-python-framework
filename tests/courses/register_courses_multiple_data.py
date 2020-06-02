from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import StatusTTest
import unittest
import pytest
from ddt import ddt, data, unpack
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = StatusTTest(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4147 2024 1608 1817", "12/22", "325", "32423"), ("Learn Python 3 from scratch",
                                                                                        "4147 2024 1608 181", "09/22",
                                                                                        "546", "43648"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccEXP, ccCVV, ccZIP):
        self.courses.EnterCourseName(courseName)
        time.sleep(1)
        self.courses.SelectCourseToEnroll(courseName)
        time.sleep(2)
        self.courses.EnrollCourse(num=ccNum, exp=ccEXP, cvv=ccCVV, zip=ccZIP)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        time.sleep(1)
        self.driver.get("https://letskodeit.teachable.com/courses")
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        #self.driver.get("https://letskodeit.teachable.com/courses")
        #self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
        #self.driver.find_element_by_link_text("All Courses").click()
