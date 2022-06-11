# -*- coding: utf-8 -*-
#!/usr/bin/env python

import aop
import aop.api
import json
import requests
import os
import sys

apiKey = sys.argv[1]
apiSecurity = sys.argv[2]
dataSourceId = sys.argv[3]
appVersion = sys.argv[4]
mappingFilePath = sys.argv[5]

# 设置网关域名
aop.set_default_server('gateway.open.umeng.com')

# 设置apiKey和apiSecurity
aop.set_default_appinfo(apiKey, apiSecurity)

# 构造Request和访问协议是否是https
req = aop.api.UmengQuickbirdSymUploadRequest()

# 发起Api请求
try:
    resp = req.get_response(None, dataSourceId=dataSourceId, appVersion=appVersion, fileType=1, fileName="mapping.txt")
    print(resp)
    # print(resp['callback'])
    # print(resp['accessKeyId'])
    # print(resp['policy'])
    # print(resp['key'])
    # print(resp['signature'])
    # print(resp['uploadAddress'])

    r = requests.post(resp['uploadAddress'], files={
        'file': open(mappingFilePath, 'rb')
    }, data={
        'OSSAccessKeyId': resp['accessKeyId'],
        'key': resp['key'],
        'policy': resp['policy'],
        'signature': resp['signature'],
        'callback': resp['callback']
    })
    rjson = r.json()
    print(rjson)

except aop.ApiError as e:
    # Api网关返回的异常
    print(e)
except aop.AopError as e:
    # 客户端Api网关请求前的异常
    print(e)
except Exception as e:
    # 其它未知异常
    print(e)