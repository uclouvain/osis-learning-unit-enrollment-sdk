"""
    Learning Unit Enrollment Service

    A set of API endpoints that allow you to get information about learning unit enrollment  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_learning_unit_enrollment_sdk
from osis_learning_unit_enrollment_sdk.model.student_specific_profile import StudentSpecificProfile
globals()['StudentSpecificProfile'] = StudentSpecificProfile
from osis_learning_unit_enrollment_sdk.model.enrollment import Enrollment


class TestEnrollment(unittest.TestCase):
    """Enrollment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnrollment(self):
        """Test Enrollment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Enrollment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
