# -*- coding: utf-8 -*-
import requests
import xmltodict

headers = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Mi-4c MIUI/V8.1.3.0.LXKCNDI)',
    'Content-Type': 'application/x-www-form-urlencoded'
}

form = {
    'ent_name': '京东',
    'pageNo': '1',
    'verify_code': 'CCFECE22700A022D8D8CD60A5D68DEB5',
    'reg_no': '京东',
    'net_type': 'Android',
    'clear': 'true'
}

url = 'http://211.94.187.236:8088/android/androidAction!tb1.dhtml'

response = requests.post(url, data=form, headers=headers)
data = xmltodict.parse(response.text, process_namespaces=True, encoding='UTF-8')
print(data['qylist'])
