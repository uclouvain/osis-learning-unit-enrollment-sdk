"""
    Learning Unit Enrollment Service

    A set of API endpoints that allow you to get information about learning unit enrollment  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_learning_unit_enrollment_sdk
from osis_learning_unit_enrollment_sdk.api.enrollment_api import EnrollmentApi  # noqa: E501


class TestEnrollmentApi(unittest.TestCase):
    """EnrollmentApi unit test stubs"""

    def setUp(self):
        self.api = EnrollmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enrollments_list(self):
        """Test case for enrollments_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
