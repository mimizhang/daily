# 打开网络链接图片
from PIL import Image
from io import BytesIO
from urllib.request import urlopen

from requests import get


url = 'http://image.58.com/showphone.aspx?t=v55&v=EDF873EC49396CD0D16AC5BFCE65B435B'
# urllib
image_bytes = urlopen(url).read()
# requests
image_bytes = get(url).content
data_stream = BytesIO(image_bytes)
pil_image = Image.open(data_stream)
print(pil_image.size)
