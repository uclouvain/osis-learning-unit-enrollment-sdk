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
from osis_learning_unit_enrollment_sdk.model.disability_subtype_peps_enum import DisabilitySubtypePepsEnum
from osis_learning_unit_enrollment_sdk.model.enrollment import Enrollment
from osis_learning_unit_enrollment_sdk.model.enrollment_list import EnrollmentList
from osis_learning_unit_enrollment_sdk.model.error import Error
from osis_learning_unit_enrollment_sdk.model.sport_subtype_peps_enum import SportSubtypePepsEnum
from osis_learning_unit_enrollment_sdk.model.type_peps_enum import TypePepsEnum
