# https://github.com/kennethreitz/grequests/blob/master/README.rst
import grequests
import time


def exception_handler(request, exception):
    print('Request failed')


urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]

rs = (grequests.get(u) for u in urls)
start = time.time()
a = grequests.imap(rs, exception_handler=exception_handler)
for a_ in a:
    print(a_.status_code)

end = time.time()
print(end - start)
