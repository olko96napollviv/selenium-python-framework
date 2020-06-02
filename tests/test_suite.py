import unittest
from tests.home.login_test import LoginTests
from tests.courses.register_courses_cvs_data import RegisterCoursesTests

#Get all tests from the test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTests)

#Create test suite combinding all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)