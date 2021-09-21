# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_learning_unit_enrollment_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_learning_unit_enrollment_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_enrollment_sdk.model.enrollment import Enrollment
from osis_learning_unit_enrollment_sdk.model.error import Error
from osis_learning_unit_enrollment_sdk.model.paginated_enrollment_list import PaginatedEnrollmentList
from osis_learning_unit_enrollment_sdk.model.paginated_enrollment_list_all_of import PaginatedEnrollmentListAllOf
from osis_learning_unit_enrollment_sdk.model.paging import Paging
from osis_learning_unit_enrollment_sdk.model.student_specific_profile import StudentSpecificProfile
from osis_learning_unit_enrollment_sdk.model.subtype_enum import SubtypeEnum
from osis_learning_unit_enrollment_sdk.model.type_peps_enum import TypePepsEnum
