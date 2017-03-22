# 爬取http://www.gatherproxy.com/zh/proxylist/anonymity/?t=Elite代理
# 需要下载驱动chromedriver，然后将驱动文件路径配置在环境变量/usr/local/bin中即可。
# 不错的总结
# http://www.zhangzewen.net/posts/2016/Sep/25/seleniumphantomjsshi-yong-zong-jie/#seleniumphantomjsshi-yong-zong-jie
# browser.execute_script(newwindow) 可以执行js
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
import re


dcap = DesiredCapabilities.PHANTOMJS.copy()
# 设置超时时间
dcap['phantomjs.page.settings.resourceTimeout'] = 5
# 是否加载图片
dcap['phantomjs.page.settings.loadImages'] = False
dcap[
    'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# 设置Referer
dcap['phantomjs.page.customHeaders.Referer'] = 'http://www.gatherproxy.com/zh/proxylist/anonymity/?t=Elite'

driver = webdriver.PhantomJS(desired_capabilities=dcap)

driver.get('http://www.gatherproxy.com/zh/proxylist/anonymity/?t=Elite')
driver.find_element_by_css_selector('.button').click()
# 页面还是在loading其他东西，一般保险的做法就是等上一段时间
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'footer')))

ips = []
for i in range(1, 11):
    index = str(i)
    # try:
    if i == 1:
        html = pq(driver.page_source)
    else:
        driver.find_element_by_css_selector(f'.pagenavi a:nth-child({index})').click()
        html = pq(driver.page_source)

    for i, elem in enumerate(html('.proxy-list').items(selector='tr')):
        if (i > 1):
            ip = re.sub(r'document\.write\([^\s]*\)\s', '', elem('td').eq(1).text())
            port = re.sub(r'document\.write\([^\s]*\)\s', '', elem('td').eq(2).text())
            type = 'http'
            ips.append((ip, port, type))

print(ips)
# finally:
# 关闭浏览器
driver.quit()
