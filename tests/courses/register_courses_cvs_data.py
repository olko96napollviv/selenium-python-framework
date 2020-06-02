from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import Navigation_page
from utilities.teststatus import StatusTTest
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = StatusTTest(self.driver)
        self.nav = Navigation_page(self.driver)
    def setUp(self):
        self.nav.navigateToPractice()
        time.sleep(2)
        self.nav.navigateToALlCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/jobster/Documents/LetsKodeIt/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, CourseName, ccNum, ccEXP, ccCVV, ccZIP):
        self.courses.EnterCourseName(CourseName)
        time.sleep(1)
        print("**" * 20)
        print("***")
        lp = CourseName
        print(lp)
        print("***")
        print("**" * 20)

        self.courses.SelectCourseToEnroll(CourseName)
        self.courses.EnrollCourse(num=ccNum, exp=ccEXP, cvv=ccCVV, zip=ccZIP)
        result = self.courses.verifyEnrollFailed()
        self.driver.get("https://letskodeit.teachable.com/courses")
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
