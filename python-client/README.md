# swagger_client

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.1.0
- Package version: 1.0.0
- Build date: 2016-06-25T14:20:30.264Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.DefaultApi
rpt_type = 1.2 # float | Report type. (0 report, 1 widget, 2 chart).
rpt_id = 1.2 # float | Report id.
start = 3.4 # float | Start offset. (optional)
limit = 3.4 # float | Number of results to return. Max 10K. (optional)
sort_by = 'sort_by_example' # str | Sort column. (optional)
sort_type = 'sort_type_example' # str | Sort mode asc/desc. (optional)
from_date = 'from_date_example' # str | Start date time. (optional)
to_date = 'to_date_example' # str | End date time. (optional)
duration = 3.4 # float | Duration range. (optional)
phone = 'phone_example' # str | List of caller phone. (optional)
phone1 = 'phone1_example' # str | List of dialled phones. (optional)
co = 'co_example' # str | List of trunk/co. (optional)
ext = 'ext_example' # str | list of extensions. (optional)
pbx_id = 3.4 # float | list of PBX Ids. (optional)
call_source = 3.4 # float | list of callsource. (optional)
call_type = 3.4 # float | list of call type signatures.(5 Unanswered Calls, 7 Transfered Calls, 8 Forwarded Calls) (optional)
direction = 3.4 # float | list of direction.(0 incoming, 1 outgoing, 2 internal) (optional)
caller_name = 'caller_name_example' # str | list of caller name. (optional)
did = 'did_example' # str | list of did. (optional)
dnis = 'dnis_example' # str | list of dnis. (optional)
acc = 'acc_example' # str | list of account code. (optional)
ring = 3.4 # float | Ring range.Seconds unit. (optional)
cost = 3.4 # float | Cost range. (optional)
group = 3.4 # float | Department/Group id. (optional)

try:
    api_response = api_instance.calls_get(rpt_type, rpt_id, start=start, limit=limit, sort_by=sort_by, sort_type=sort_type, from_date=from_date, to_date=to_date, duration=duration, phone=phone, phone1=phone1, co=co, ext=ext, pbx_id=pbx_id, call_source=call_source, call_type=call_type, direction=direction, caller_name=caller_name, did=did, dnis=dnis, acc=acc, ring=ring, cost=cost, group=group)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->calls_get: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.pbxdom.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**calls_get**](docs/DefaultApi.md#calls_get) | **GET** /Calls | 
*DefaultApi* | [**features_charts_get**](docs/DefaultApi.md#features_charts_get) | **GET** /Features/charts | 
*DefaultApi* | [**features_reports_get**](docs/DefaultApi.md#features_reports_get) | **GET** /Features/reports | 
*DefaultApi* | [**features_widget_get**](docs/DefaultApi.md#features_widget_get) | **GET** /Features/widget | 


## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


