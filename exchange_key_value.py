from pprint import pprint


def exchange_k_v(dict):
    result = {v: k for k, v in dict.items()}
    return result


json = {
    "certNum": "证书编号",
    "serScope": "服务范围",
    "entName": "单位名称",
    "leRep": "法定代表人",
    "addr": "单位地址",
    "province": "省份",
    "websiteName": "网站名称",
    "ip": "IP地址",
    "domain": "域名",
    "issDate": "发证日期",
    "endDate": "有效截至日期",
    "postcode": "邮编"
}
pprint(exchange_k_v(json))
