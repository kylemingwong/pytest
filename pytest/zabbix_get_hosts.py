import requests
import json

ZABIX_ROOT = 'http://192.168.1.150/zabbix'
url = ZABIX_ROOT + '/api_jsonrpc.php'

# user.login
payload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        'user': 'Admin',
        'password': 'zabbix',
    },
    "auth": None,
    "id": 0,
}
headers = { 'content-type': 'application/json', }
req = requests.post(url, json=payload, headers=headers)
auth = req.json()

# host.get
payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        'output': [
            'hostid',
            'name'],
    },
    "auth": auth['result'],
    "id": 2,
}
res2 = requests.post(url, data=json.dumps(payload), headers=headers)
res2 = res2.json()

for host in res2['result']:
    print host['hostid'] + '\t' + host['name'] + '\n'
