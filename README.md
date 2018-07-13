# pytest
some python learning code!<br>
``some bg text here!``<br>

some code here!<br>
```
from aliyunsdkcore import client
from aliyunsdkcms.request.v20170301 import QueryMetricLastRequest
import time
import datetime

clt = client.AcsClient('ak','sk','cn-hangzhou')
request = QueryMetricLastRequest.QueryMetricLastRequest()
request.set_accept_format('json')
request.set_Project('acs_ecs_dashboard')
request.set_Metric('memory_freeutilization')
##start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
##timestamp_start = int(time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))) * 1000
##request.set_StartTime(timestamp_start)
#request.set_Dimensions("{'instanceId':'instanceid'}")
##request.set_Period('60')
result = clt.do_action_with_exception(request)
##print datetime.datetime.now()
print result
```
