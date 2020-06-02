from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import StatusTTest
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = StatusTTest(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.EnterCourseName("JavaScript")
        self.courses.SelectCourseToEnroll("JavaScript for beginners")
        self.courses.EnrollCourse(num="4147 2024 1508 117", exp="12/22", cvv="325", zip="32423")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")