# -*- coding: utf-8 -*-
# 自建IP代理池
from pyquery import PyQuery as pq
import requests
import time
# 线程
from multiprocessing.dummy import Pool as ThreadPool


# 进程
# from multiprocessing import Pool, cpu_count


# 设置头
def set_headers():
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    return headers


# 验证ip有效性
def verify_ip(ip_e):
    headers = set_headers()
    proxy = {'%s' % (ip_e[2]): '%s://%s:%s' % (ip_e[2], ip_e[0], ip_e[1])}
    test_url = 'http://ip.cn/'
    # test_url = 'https://www.baidu.com/s?wd=ip'

    try:
        response = requests.get(url=test_url, headers=headers, proxies=proxy)
        if response.status_code == 200:
            code = pq(response.text)('code').eq(0).text()
            # code = pq(response.text)('.c-span21')('span').eq(0).text().replace('本机IP: ', '')
            # print(code)
            if code == ip_e[0]:
                print(proxy)
                # 有效ip保存到agent_pool.txt文件
                # with open('agent_pool.txt', 'a') as f:
                #     f.write(ip + u':' + port)
                #     f.write('\n')
                # 上传到队列
                requests.post('http://****:****/?charset=utf-8&name=agent_pool&opt=put&check=BSC258',
                              data=ip_e[2] + u'://' + ip_e[0] + u':' + ip_e[1])

        else:
            print('not ok')
    except:
        print('not ok')


# 爬取代理IP
def crawl(param_e, i):
    ips = []
    response = requests.get(param_e['head'] + str(i) + param_e['tail'], headers=param_e['headers'])
    text = response.text
    table = pq(text)(param_e['selector'])

    for j, tr in enumerate(table.items(selector='tr')):
        if j is not 0:
            ip = tr('td').eq(param_e['ip']).text()
            port = tr('td').eq(param_e['port']).text()
            type = tr('td').eq(param_e['type']).text().lower()
            ips.append((ip, port, type))

    return ips


# http://www.gatherproxy.com/
def crawl2():
    ips = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': 'http://www.gatherproxy.com/zh/proxylist/anonymity/?t=Elite',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '20',
        'Origin': 'http: // www.gatherproxy.com',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'ASP.NET_SessionId=rbkatxgvtidoklacegszyllo; session_depth=www.gatherproxy.com%3D2%7C563749776%3D2; _gat=1; _lang=zh-CN; _ga=GA1.2.1064384249.1488818198'
    }
    response = requests.post('http://www.gatherproxy.com/zh/proxylist/anonymity/?t=Elite', headers=headers,
                             data='Type=elite&PageIdx=' + str(i) + '&Uptime=0')
    data = {
        'Type':'elite',
        'PageIdx': '2'
    }


# 参数
param = [
    {
        'head': 'http://www.xicidaili.com/nn/',
        'ip': 1,
        'port': 2,
        'type': 5,
        'tail': '',
        'selector': '#ip_list',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    },
    # 快代理cookie会过期,而且代理IP质量差
    {
        'head': 'http://www.kuaidaili.com/free/inha/',
        'ip': 0,
        'port': 1,
        'type': 3,
        'tail': '/',
        'selector': '#list',
        'headers': {
            'Cookie': '_ydclearance=9c854a7b42e96e7f2270b114-6089-447a-bb15-06fd5dcfaafc-1488986138; channelid=0; sid=1488978519592487; _ga=GA1.2.1368528244.1488819329; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488819329; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488978942',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Host': 'www.kuaidaili.com'
        }
    },
    {
        'head': 'http://www.kuaidaili.com/free/outha/',
        'ip': 0,
        'port': 1,
        'type': 3,
        'tail': '/',
        'selector': '#list',
        'headers': {
            'Cookie': '_ydclearance=9c854a7b42e96e7f2270b114-6089-447a-bb15-06fd5dcfaafc-1488986138; channelid=0; sid=1488978519592487; _ga=GA1.2.1368528244.1488819329; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488819329; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488978942',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Host': 'www.kuaidaili.com'
        }
    }
]

if __name__ == '__main__':
    for i in range(1, 4):
        for param_e in param:
            ip_list = crawl(param_e, i)
            # print(ip_list)
            p = ThreadPool(4)
            start = time.time()
            p.map(verify_ip, ip_list)
            p.close()
            p.join()
            end = time.time()
            print('耗时 : ' + str(end - start) + ' s')
