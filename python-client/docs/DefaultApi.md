# swagger_client.DefaultApi

All URIs are relative to *https://api.pbxdom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calls_get**](DefaultApi.md#calls_get) | **GET** /Calls | 
[**features_charts_get**](DefaultApi.md#features_charts_get) | **GET** /Features/charts | 
[**features_reports_get**](DefaultApi.md#features_reports_get) | **GET** /Features/reports | 
[**features_widget_get**](DefaultApi.md#features_widget_get) | **GET** /Features/widget | 


# **calls_get**
> list[InlineResponse200] calls_get(rpt_type, rpt_id, start=start, limit=limit, sort_by=sort_by, sort_type=sort_type, from_date=from_date, to_date=to_date, duration=duration, phone=phone, phone1=phone1, co=co, ext=ext, pbx_id=pbx_id, call_source=call_source, call_type=call_type, direction=direction, caller_name=caller_name, did=did, dnis=dnis, acc=acc, ring=ring, cost=cost, group=group)



Gets `Calls` info. 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpt_type** | **float**| Report type. (0 report, 1 widget, 2 chart). | 
 **rpt_id** | **float**| Report id. | 
 **start** | **float**| Start offset. | [optional] 
 **limit** | **float**| Number of results to return. Max 10K. | [optional] 
 **sort_by** | **str**| Sort column. | [optional] 
 **sort_type** | **str**| Sort mode asc/desc. | [optional] 
 **from_date** | **str**| Start date time. | [optional] 
 **to_date** | **str**| End date time. | [optional] 
 **duration** | **float**| Duration range. | [optional] 
 **phone** | **str**| List of caller phone. | [optional] 
 **phone1** | **str**| List of dialled phones. | [optional] 
 **co** | **str**| List of trunk/co. | [optional] 
 **ext** | **str**| list of extensions. | [optional] 
 **pbx_id** | **float**| list of PBX Ids. | [optional] 
 **call_source** | **float**| list of callsource. | [optional] 
 **call_type** | **float**| list of call type signatures.(5 Unanswered Calls, 7 Transfered Calls, 8 Forwarded Calls) | [optional] 
 **direction** | **float**| list of direction.(0 incoming, 1 outgoing, 2 internal) | [optional] 
 **caller_name** | **str**| list of caller name. | [optional] 
 **did** | **str**| list of did. | [optional] 
 **dnis** | **str**| list of dnis. | [optional] 
 **acc** | **str**| list of account code. | [optional] 
 **ring** | **float**| Ring range.Seconds unit. | [optional] 
 **cost** | **float**| Cost range. | [optional] 
 **group** | **float**| Department/Group id. | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **features_charts_get**
> list[InlineResponse200] features_charts_get()



Gets `Charts` list. 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.features_charts_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->features_charts_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **features_reports_get**
> list[InlineResponse200] features_reports_get()



Gets `Reports` list. 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.features_reports_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->features_reports_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **features_widget_get**
> list[InlineResponse200] features_widget_get()



Gets `Widgets` list. 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.features_widget_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->features_widget_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

