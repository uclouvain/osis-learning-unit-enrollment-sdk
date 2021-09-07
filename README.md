# osis-learning-unit-enrollment-sdk
A set of API endpoints that allow you to get information about learning unit enrollment

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.5

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_learning_unit_enrollment_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_learning_unit_enrollment_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_learning_unit_enrollment_sdk
from pprint import pprint
from osis_learning_unit_enrollment_sdk.api import enrollment_api
from osis_learning_unit_enrollment_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_enrollment_sdk.model.enrollment_list import EnrollmentList
from osis_learning_unit_enrollment_sdk.model.error import Error
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit_enrollment
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_enrollment_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit_enrollment"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'


# Enter a context with an instance of the API client
with osis_learning_unit_enrollment_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enrollment_api.EnrollmentApi(api_client)
    acronym = "LABCD1234" # str | The learning unit acronym
year = 2021 # int | The learning unit academic year
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    try:
        api_response = api_instance.enrollments_list(acronym, year, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_enrollment_sdk.ApiException as e:
        print("Exception when calling EnrollmentApi->enrollments_list: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/learning_unit_enrollment*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EnrollmentApi* | [**enrollments_list**](docs/EnrollmentApi.md#enrollments_list) | **GET** /enrollments/ | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [DisabilitySubtypePepsEnum](docs/DisabilitySubtypePepsEnum.md)
 - [EnrollmentList](docs/EnrollmentList.md)
 - [Error](docs/Error.md)
 - [SportSubtypePepsEnum](docs/SportSubtypePepsEnum.md)
 - [TypePepsEnum](docs/TypePepsEnum.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_learning_unit_enrollment_sdk.apis and osis_learning_unit_enrollment_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_learning_unit_enrollment_sdk.api.default_api import DefaultApi`
- `from osis_learning_unit_enrollment_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_learning_unit_enrollment_sdk
from osis_learning_unit_enrollment_sdk.apis import *
from osis_learning_unit_enrollment_sdk.models import *
```

